"""
git_resolver.py — Git-pull world resolver for MultiworldGG.

This module provides resolve_world_via_git(), which is called by ModuleUpdate
when MWGG_USE_GIT_RESOLVER=1 is set.  It reads upstream_repo_url / release_ref
/ entry_point_module from the mwgg_igdb index and clones/installs the world
into mwgg_venv so that worlds/__init__.py's __path__ extension keeps finding it.

Feature flag:  MWGG_USE_GIT_RESOLVER=1   (default: off)

Cache layout:  <write_path>/mwgg_world_repos/<slug>/
  Each checkout also stores a sentinel file ".mwgg_resolved_ref" containing a
  JSON object with the ref that last succeeded, e.g.:
      {"kind": "git-tag", "value": "v1.2.3"}
  This encodes both kind and value so a re-ordered or differently-typed list
  invalidates the cache and triggers a fresh attempt.

release_ref field schema (mwgg_igdb v2):
  - null or []                 — not yet split; resolver skips.
  - [{"kind": ..., "value": ...}, ...]  — ordered list; tried in sequence.
  - {"kind": ..., "value": ...}         — legacy single-dict; wrapped to [ref].
"""

from __future__ import annotations

import json
import logging
import os
import subprocess
import tempfile
import urllib.request
from pathlib import Path
from typing import Optional

logger = logging.getLogger("GitResolver")

# ---------------------------------------------------------------------------
# Resolver state — populated during resolve_world_via_git() calls so that
# external consumers (e.g. the launcher console panel) can query per-slug
# status without reading sentinel files.
#
# Keys  : slug strings
# Values: one of "resolved", "cached", "failed: <reason>", "skipped: <reason>"
#
# get_resolver_state() returns a shallow copy so callers cannot mutate this.
# When the feature flag is off the resolver never runs and this dict stays
# empty; get_resolver_state() returns {} as documented.
# ---------------------------------------------------------------------------

_resolver_state: dict[str, str] = {}


def get_resolver_state() -> dict[str, str]:
    """Return a snapshot of per-slug resolver status strings.

    Possible values per slug:
      "resolved"           — freshly installed/updated this session
      "cached"             — already at the correct ref, nothing done
      "failed: <reason>"  — an error prevented installation
      "skipped: <reason>" — intentionally not processed (custom_worlds
                            override, missing index data, unknown ref kind)

    Returns an empty dict when the git resolver has not run (feature flag off
    or resolve_worlds_via_git() has not been called yet).
    """
    return dict(_resolver_state)

# ---------------------------------------------------------------------------
# Runtime-flags loader — runs once at module import time.
# Reads mwgg_runtime_flags.ini written by build_exe.py next to the executable
# (or source root in dev) and pushes KEY=value pairs into os.environ via
# setdefault so an explicit env var always wins.
# ---------------------------------------------------------------------------

def _load_runtime_flags() -> None:
    try:
        from BaseUtils import local_path
        flags_path = Path(local_path("mwgg_runtime_flags.ini"))
        if not flags_path.is_file():
            return
        for line in flags_path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, _, value = line.partition("=")
            os.environ.setdefault(key.strip(), value.strip())
    except Exception as exc:
        logger.warning(f"[git-resolver] Could not load mwgg_runtime_flags.ini: {exc}")

_load_runtime_flags()

# ---------------------------------------------------------------------------
# Feature flag
# ---------------------------------------------------------------------------

GIT_RESOLVER_ENV_VAR = "MWGG_USE_GIT_RESOLVER"


def git_resolver_enabled() -> bool:
    """Return True when the env-var opt-in flag is set."""
    return os.environ.get(GIT_RESOLVER_ENV_VAR, "0").strip() in ("1", "true", "yes", "on")


# ---------------------------------------------------------------------------
# Path helpers  (mirror install_path() logic from ModuleUpdate without import)
# ---------------------------------------------------------------------------

def _write_root() -> Path:
    """Return the per-user MultiworldGG data root (same root as mwgg_venv)."""
    import sys
    if sys.platform in ("win32", "cygwin", "msys"):
        return Path.home() / "AppData" / "Local" / "MultiworldGG"
    elif sys.platform == "darwin":
        return Path.home() / "Library" / "Application Support" / "MultiworldGG"
    else:
        return Path.home() / ".local" / "share" / "MultiworldGG"


def _repos_root() -> Path:
    return _write_root() / "mwgg_world_repos"


def _repo_dir(slug: str) -> Path:
    return _repos_root() / slug


def _sentinel_file(slug: str) -> Path:
    return _repo_dir(slug) / ".mwgg_resolved_ref"


# ---------------------------------------------------------------------------
# Ref helpers
# ---------------------------------------------------------------------------

def _read_cached_ref(slug: str) -> Optional[dict]:
    """Return the last-successful ref dict, or None if not present / unreadable.

    The sentinel now stores JSON so both kind and value are preserved.  Old
    sentinels that contain a plain string (pre-migration) are treated as a
    cache miss so they are naturally overwritten on the next successful run.
    """
    sf = _sentinel_file(slug)
    try:
        raw = sf.read_text(encoding="utf-8").strip()
        parsed = json.loads(raw)
        if isinstance(parsed, dict) and "kind" in parsed and "value" in parsed:
            return parsed
        # Stale plain-string sentinel from old code — treat as miss
        return None
    except (FileNotFoundError, json.JSONDecodeError, TypeError):
        return None


def _write_cached_ref(slug: str, ref_dict: dict) -> None:
    """Persist *ref_dict* as the winning ref for *slug*."""
    sf = _sentinel_file(slug)
    sf.parent.mkdir(parents=True, exist_ok=True)
    sf.write_text(json.dumps(ref_dict), encoding="utf-8")


# ---------------------------------------------------------------------------
# Git helpers
# ---------------------------------------------------------------------------

def _run_git(*args: str, cwd: Optional[Path] = None, check: bool = True) -> subprocess.CompletedProcess:
    cmd = ["git"] + list(args)
    logger.debug(f"git {' '.join(args)}")
    return subprocess.run(cmd, capture_output=True, text=True, cwd=cwd, check=check)


def _clone_or_update(repo_url: str, slug: str, ref_dict: dict) -> Path:
    """
    Ensure repo_dir contains a checkout at ref_dict["value"].
    *ref_dict* is the full {"kind": ..., "value": ...} entry so the sentinel
    stores both fields and can detect kind changes as well as value changes.
    Returns the repo_dir path.
    """
    ref_value: str = ref_dict["value"]
    repo_dir = _repo_dir(slug)
    cached_ref = _read_cached_ref(slug)

    if repo_dir.exists() and (repo_dir / ".git").exists():
        if cached_ref == ref_dict:
            logger.info(f"[git-resolver] {slug}: cached ref {ref_dict!r} matches — skipping re-clone")
            return repo_dir
        logger.info(f"[git-resolver] {slug}: ref changed {cached_ref!r} -> {ref_dict!r}, fetching")
        _run_git("fetch", "--tags", "--force", cwd=repo_dir)
    else:
        logger.info(f"[git-resolver] {slug}: cloning {repo_url}")
        repo_dir.mkdir(parents=True, exist_ok=True)
        _run_git("clone", "--no-checkout", repo_url, str(repo_dir))

    _run_git("checkout", ref_value, cwd=repo_dir)
    _write_cached_ref(slug, ref_dict)
    return repo_dir


# ---------------------------------------------------------------------------
# Wheel download helper
# ---------------------------------------------------------------------------

def _download_wheel(wheel_url: str, slug: str) -> Path:
    """Download a wheel to a temp location and return its path."""
    dest_dir = _repo_dir(slug)
    dest_dir.mkdir(parents=True, exist_ok=True)
    filename = wheel_url.split("/")[-1].split("?")[0] or f"{slug}.whl"
    dest = dest_dir / filename
    logger.info(f"[git-resolver] {slug}: downloading wheel from {wheel_url}")
    urllib.request.urlretrieve(wheel_url, dest)
    return dest


# ---------------------------------------------------------------------------
# pip install helper
# ---------------------------------------------------------------------------

def _pip_install_local(target: Path, python_cmd) -> bool:
    """
    Install a local directory (editable-less) or wheel into mwgg_venv.
    Uses --no-deps to keep the resolver orthogonal to the main dep solver.
    Returns True on success.
    """
    cmd = [str(python_cmd), "-m", "pip", "install", "--no-deps", "--upgrade", str(target)]
    logger.info(f"[git-resolver] pip install {target}")
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        logger.error(f"[git-resolver] pip install failed:\n{result.stderr}")
        return False
    logger.info(f"[git-resolver] installed {target}")
    return True


# ---------------------------------------------------------------------------
# Public entry point
# ---------------------------------------------------------------------------

def _normalize_release_ref(release_ref) -> Optional[list]:
    """Normalise *release_ref* to a list of ref dicts, or None when absent.

    Handles three legal shapes from the index:
      - null / None / []          → None  (not yet split)
      - dict  {"kind":…,"value":…}  → [ref]   (legacy single-ref, backwards compat)
      - list  [{…}, …]             → list as-is
    """
    if not release_ref:
        return None
    if isinstance(release_ref, dict):
        # Legacy single-dict shape — wrap so the rest of the code is uniform.
        return [release_ref]
    if isinstance(release_ref, list):
        return release_ref if release_ref else None
    return None


def resolve_world_via_git(
    slug: str,
    index_entry: dict,
    python_cmd,
    *,
    custom_worlds_slugs: Optional[set] = None,
) -> Optional[str]:
    """
    Attempt to resolve and install a world for *slug* using the git-pull path.

    Parameters
    ----------
    slug:
        The mwgg_igdb slug (key in GAMES_DATA).
    index_entry:
        The dict returned by GameIndex.get_game(slug).
    python_cmd:
        Path-like pointing at the mwgg_venv Python executable (same object
        used everywhere else in ModuleUpdate).
    custom_worlds_slugs:
        Set of slugs already satisfied by custom_worlds/ — if *slug* is in
        this set, we skip and return None so the caller keeps the custom path.

    Returns
    -------
    The entry_point_module string (e.g. "worlds.alttp") on success, or None on
    any failure / skip.  The caller should fall through to the pypi path when
    None is returned and MWGG_USE_GIT_RESOLVER is off; when the flag is on, a
    None return means the world is unavailable.

    release_ref handling
    --------------------
    The index field may be null, a single dict (legacy), or a list of dicts.
    Each entry is tried in order; the first success wins.  If all entries fail
    the final failure reason is recorded in _resolver_state.
    """
    if custom_worlds_slugs and slug in custom_worlds_slugs:
        logger.info(f"[git-resolver] {slug}: custom_worlds/ override present — skipping git path")
        _resolver_state[slug] = "skipped: custom_worlds override"
        return None

    upstream_repo_url: Optional[str] = index_entry.get("upstream_repo_url")
    raw_release_ref = index_entry.get("release_ref")
    entry_point_module: Optional[str] = index_entry.get("entry_point_module")

    if not upstream_repo_url:
        logger.debug(f"[git-resolver] {slug}: upstream_repo_url is null — not yet split, skipping")
        _resolver_state[slug] = "skipped: no upstream_repo_url"
        return None

    ref_list = _normalize_release_ref(raw_release_ref)
    if ref_list is None:
        logger.debug(f"[git-resolver] {slug}: release_ref is null/empty — not yet split, skipping")
        _resolver_state[slug] = "skipped: no release_ref"
        return None

    if not entry_point_module:
        logger.warning(f"[git-resolver] {slug}: entry_point_module is null — cannot register world after install")
        # Still attempt to install; caller may discover via pip metadata.

    # --- iterate refs in order, stop at first success ---
    attempt_reasons: list[str] = []
    total = len(ref_list)

    for idx, ref_entry in enumerate(ref_list):
        ref_kind: str = ref_entry.get("kind", "") if isinstance(ref_entry, dict) else ""
        ref_value: str = ref_entry.get("value", "") if isinstance(ref_entry, dict) else ""

        if not ref_kind or not ref_value:
            reason = f"malformed ref at index {idx}: {ref_entry!r}"
            logger.debug(f"[git-resolver] {slug}: {reason} — skipping this entry")
            attempt_reasons.append(reason)
            continue

        logger.debug(f"[git-resolver] {slug}: trying ref {idx + 1}/{total}: kind={ref_kind!r} value={ref_value!r}")

        try:
            if ref_kind in ("git-tag", "git-sha"):
                repo_dir = _clone_or_update(upstream_repo_url, slug, ref_entry)
                cached_ref = _read_cached_ref(slug)
                # _clone_or_update writes the sentinel on a fresh checkout;
                # if we got here without re-cloning cached_ref == ref_entry.
                _is_cached = (cached_ref == ref_entry) and repo_dir.exists()
                success = _pip_install_local(repo_dir, python_cmd)
                if not success:
                    reason = f"pip install error (ref {idx + 1}/{total}: {ref_kind} {ref_value!r})"
                    attempt_reasons.append(reason)
                    logger.debug(f"[git-resolver] {slug}: {reason}")
                    continue

            elif ref_kind == "wheel-url":
                cached_ref = _read_cached_ref(slug)
                if cached_ref == ref_entry:
                    logger.info(f"[git-resolver] {slug}: wheel ref {ref_value!r} already installed — cached")
                    _resolver_state[slug] = "cached"
                    return entry_point_module
                wheel_path = _download_wheel(ref_value, slug)
                _is_cached = False
                success = _pip_install_local(wheel_path, python_cmd)
                if not success:
                    reason = f"pip install error (ref {idx + 1}/{total}: wheel-url {ref_value!r})"
                    attempt_reasons.append(reason)
                    logger.debug(f"[git-resolver] {slug}: {reason}")
                    continue
                _write_cached_ref(slug, ref_entry)

            else:
                reason = f"unknown ref_kind {ref_kind!r} at index {idx}"
                logger.debug(f"[git-resolver] {slug}: {reason} — skipping this entry")
                attempt_reasons.append(reason)
                continue

        except Exception as exc:
            reason = f"exception on ref {idx + 1}/{total} ({ref_kind} {ref_value!r}): {exc}"
            logger.debug(f"[git-resolver] {slug}: {reason}", exc_info=True)
            attempt_reasons.append(reason)
            continue

        # Reached here — this ref succeeded.
        _resolver_state[slug] = "cached" if _is_cached else "resolved"
        from importlib import invalidate_caches
        invalidate_caches()
        return entry_point_module

    # All refs exhausted without success.
    last = attempt_reasons[-1] if attempt_reasons else "no refs attempted"
    final_reason = f"failed: all {total} ref(s) failed; last: {last}"
    logger.error(f"[git-resolver] {slug}: {final_reason}")
    _resolver_state[slug] = final_reason
    return None


# ---------------------------------------------------------------------------
# Batch helper called from ModuleUpdate
# ---------------------------------------------------------------------------

def resolve_worlds_via_git(
    slugs_needing_install: list[str],
    python_cmd,
    *,
    custom_worlds_slugs: Optional[set] = None,
) -> dict[str, Optional[str]]:
    """
    Resolve a batch of slugs.  Returns a mapping slug -> entry_point_module
    (None means the slug failed or was skipped and should fall through to pypi).
    """
    from mwgg_igdb import GameIndex  # late import to avoid circular at module load

    results: dict[str, Optional[str]] = {}
    for slug in slugs_needing_install:
        index_entry = GameIndex.get_game(slug)
        if not index_entry:
            logger.debug(f"[git-resolver] {slug}: not found in GameIndex")
            _resolver_state[slug] = "skipped: not in index"
            results[slug] = None
            continue
        results[slug] = resolve_world_via_git(
            slug, index_entry, python_cmd,
            custom_worlds_slugs=custom_worlds_slugs,
        )

    resolved = [s for s, m in results.items() if m is not None]
    skipped = [s for s, m in results.items() if m is None]
    logger.info(f"[git-resolver] resolved={resolved}  skipped/fallthrough={skipped}")
    return results
