"""
Smoke test for the git-pull world resolver.

Run from the src/ directory (dev / non-frozen mode):

    MWGG_USE_GIT_RESOLVER=1 python -m pytest test/utils/test_git_resolver.py -s -v

Or directly:

    set MWGG_USE_GIT_RESOLVER=1 && python test/utils/test_git_resolver.py

What it does
------------
1.  Confirms git_resolver_enabled() honours the env var.
2.  Tests ref-cache logic (skip re-clone when cached ref matches).
3.  Exercises the wheel-url dispatch path against a local dummy wheel file so
    no external network call is needed during CI.
4.  Exercises the git-tag and git-sha dispatch paths against
    https://github.com/nicowillis/git-resolver-smoke-test (a tiny public repo
    pinned to tag v0.1.0) — skip automatically when git is unavailable or the
    network is unreachable so CI offline runs don't break.
"""

from __future__ import annotations

import importlib
import os
import shutil
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

# Make sure we can import from src/
src_root = Path(__file__).resolve().parent.parent.parent
if str(src_root) not in sys.path:
    sys.path.insert(0, str(src_root))

import git_resolver  # noqa: E402


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_dummy_wheel(dest_dir: Path, slug: str = "test_slug") -> Path:
    """
    Create a minimal wheel that pip can install without error.
    The wheel just ships an empty worlds/<slug>/__init__.py.
    """
    wheel_name = f"worlds.{slug}-0.1.0-py3-none-any.whl"
    wheel_path = dest_dir / wheel_name

    dist_info = f"worlds.{slug}-0.1.0.dist-info"
    metadata = (
        f"Metadata-Version: 2.1\n"
        f"Name: worlds.{slug}\n"
        f"Version: 0.1.0\n"
        f"Summary: smoke test world\n"
    )
    record = (
        f"worlds/{slug}/__init__.py,,\n"
        f"{dist_info}/METADATA,,\n"
        f"{dist_info}/WHEEL,,\n"
        f"{dist_info}/RECORD,,\n"
    )
    wheel_meta = (
        "Wheel-Version: 1.0\n"
        "Generator: smoke-test\n"
        "Root-Is-Purelib: true\n"
        "Tag: py3-none-any\n"
    )

    with zipfile.ZipFile(wheel_path, "w") as zf:
        zf.writestr(f"worlds/{slug}/__init__.py", "# smoke test world\n")
        zf.writestr(f"{dist_info}/METADATA", metadata)
        zf.writestr(f"{dist_info}/WHEEL", wheel_meta)
        zf.writestr(f"{dist_info}/RECORD", record)

    return wheel_path


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestFeatureFlag(unittest.TestCase):
    def test_flag_off_by_default(self):
        env_backup = os.environ.pop(git_resolver.GIT_RESOLVER_ENV_VAR, None)
        try:
            self.assertFalse(git_resolver.git_resolver_enabled())
        finally:
            if env_backup is not None:
                os.environ[git_resolver.GIT_RESOLVER_ENV_VAR] = env_backup

    def test_flag_on(self):
        os.environ[git_resolver.GIT_RESOLVER_ENV_VAR] = "1"
        try:
            self.assertTrue(git_resolver.git_resolver_enabled())
        finally:
            del os.environ[git_resolver.GIT_RESOLVER_ENV_VAR]

    def test_flag_variants(self):
        for val in ("true", "yes", "on"):
            os.environ[git_resolver.GIT_RESOLVER_ENV_VAR] = val
            self.assertTrue(git_resolver.git_resolver_enabled(), msg=f"Expected True for {val!r}")
        del os.environ[git_resolver.GIT_RESOLVER_ENV_VAR]


class TestNullIndexEntry(unittest.TestCase):
    """resolve_world_via_git() must return None when index fields are null."""

    def test_null_upstream(self):
        result = git_resolver.resolve_world_via_git(
            "test_game",
            {"upstream_repo_url": None, "release_ref": None, "entry_point_module": None},
            sys.executable,
        )
        self.assertIsNone(result)

    def test_null_release_ref(self):
        result = git_resolver.resolve_world_via_git(
            "test_game",
            {"upstream_repo_url": "https://example.com/fake.git",
             "release_ref": None,
             "entry_point_module": "worlds.test_game"},
            sys.executable,
        )
        self.assertIsNone(result)
        self.assertEqual(
            git_resolver.get_resolver_state().get("test_game"),
            "skipped: no release_ref",
        )

    def test_empty_list_release_ref(self):
        """Empty list is semantically equivalent to null — not yet split."""
        result = git_resolver.resolve_world_via_git(
            "test_game",
            {"upstream_repo_url": "https://example.com/fake.git",
             "release_ref": [],
             "entry_point_module": "worlds.test_game"},
            sys.executable,
        )
        self.assertIsNone(result)
        self.assertEqual(
            git_resolver.get_resolver_state().get("test_game"),
            "skipped: no release_ref",
        )

    def test_unknown_ref_kind_single_dict(self):
        """Legacy single-dict with unknown kind ends up in failed state."""
        result = git_resolver.resolve_world_via_git(
            "test_game",
            {"upstream_repo_url": "https://example.com/fake.git",
             "release_ref": {"kind": "svn-revision", "value": "42"},
             "entry_point_module": "worlds.test_game"},
            sys.executable,
        )
        self.assertIsNone(result)
        state = git_resolver.get_resolver_state().get("test_game", "")
        self.assertTrue(state.startswith("failed:"), f"Unexpected state: {state!r}")

    def test_unknown_ref_kind_in_list(self):
        """All-unknown kinds in list produce a failed state."""
        result = git_resolver.resolve_world_via_git(
            "test_game",
            {"upstream_repo_url": "https://example.com/fake.git",
             "release_ref": [{"kind": "svn-revision", "value": "42"}],
             "entry_point_module": "worlds.test_game"},
            sys.executable,
        )
        self.assertIsNone(result)
        state = git_resolver.get_resolver_state().get("test_game", "")
        self.assertTrue(state.startswith("failed:"), f"Unexpected state: {state!r}")


class TestCustomWorldsPrecedence(unittest.TestCase):
    """Slugs in custom_worlds_slugs must be skipped by the resolver."""

    def test_custom_worlds_wins_single_dict(self):
        """Legacy single-dict ref: custom_worlds/ override still wins."""
        result = git_resolver.resolve_world_via_git(
            "my_game",
            {"upstream_repo_url": "https://example.com/repo.git",
             "release_ref": {"kind": "git-tag", "value": "v1.0"},
             "entry_point_module": "worlds.my_game"},
            sys.executable,
            custom_worlds_slugs={"my_game"},
        )
        self.assertIsNone(result)

    def test_custom_worlds_wins_list(self):
        """New list-of-refs shape: custom_worlds/ override still wins."""
        result = git_resolver.resolve_world_via_git(
            "my_game",
            {"upstream_repo_url": "https://example.com/repo.git",
             "release_ref": [{"kind": "git-tag", "value": "v1.0"}, {"kind": "git-sha", "value": "abc1234"}],
             "entry_point_module": "worlds.my_game"},
            sys.executable,
            custom_worlds_slugs={"my_game"},
        )
        self.assertIsNone(result)


class TestRefCacheLogic(unittest.TestCase):
    """Sentinel file prevents re-clone when ref is unchanged."""

    def setUp(self):
        self._tmp = tempfile.mkdtemp()
        # Monkey-patch _repos_root to an isolated temp dir
        self._orig_repos_root = git_resolver._repos_root
        git_resolver._repos_root = lambda: Path(self._tmp)

    def tearDown(self):
        git_resolver._repos_root = self._orig_repos_root
        shutil.rmtree(self._tmp, ignore_errors=True)

    def test_cached_ref_write_read(self):
        ref = {"kind": "git-tag", "value": "v1.2.3"}
        git_resolver._write_cached_ref("some_slug", ref)
        self.assertEqual(git_resolver._read_cached_ref("some_slug"), ref)

    def test_no_cached_ref_returns_none(self):
        self.assertIsNone(git_resolver._read_cached_ref("nonexistent_slug"))

    def test_stale_plain_string_sentinel_treated_as_miss(self):
        """A pre-migration sentinel containing a bare string must be ignored."""
        sf = git_resolver._sentinel_file("stale_slug")
        sf.parent.mkdir(parents=True, exist_ok=True)
        sf.write_text("v1.2.3", encoding="utf-8")  # old format
        self.assertIsNone(git_resolver._read_cached_ref("stale_slug"))


class TestWheelUrlDispatch(unittest.TestCase):
    """
    Exercise the wheel-url path using a locally constructed dummy wheel.
    This avoids any network call and is safe for offline CI.
    """

    def setUp(self):
        self._tmp = Path(tempfile.mkdtemp())
        self._orig_repos_root = git_resolver._repos_root
        git_resolver._repos_root = lambda: self._tmp / "repos"
        self._wheel = _make_dummy_wheel(self._tmp, slug="smoke_whl")

    def tearDown(self):
        git_resolver._repos_root = self._orig_repos_root
        shutil.rmtree(str(self._tmp), ignore_errors=True)

    def test_wheel_url_installs(self):
        """
        Patch _download_wheel to return our local dummy wheel so no HTTP is made,
        then verify _pip_install_local succeeds and the sentinel is written.
        The sentinel must now be a dict ({"kind": "wheel-url", "value": ...}).
        """
        wheel_path = self._wheel
        orig_download = git_resolver._download_wheel
        git_resolver._download_wheel = lambda url, slug: wheel_path
        ref_url = "https://fake.example.com/smoke_whl-0.1.0.whl"

        try:
            entry = git_resolver.resolve_world_via_git(
                "smoke_whl",
                {
                    "upstream_repo_url": "https://fake.example.com/repo.git",
                    "release_ref": {"kind": "wheel-url", "value": ref_url},
                    "entry_point_module": "worlds.smoke_whl",
                },
                sys.executable,
            )
        finally:
            git_resolver._download_wheel = orig_download

        # entry_point_module is returned on success
        self.assertEqual(entry, "worlds.smoke_whl")
        # Sentinel is now a dict encoding both kind and value
        self.assertEqual(
            git_resolver._read_cached_ref("smoke_whl"),
            {"kind": "wheel-url", "value": ref_url},
        )

    def test_wheel_url_cached_ref_skips_download(self):
        """Second call with same ref must skip download entirely."""
        wheel_path = self._wheel
        download_calls = []
        orig_download = git_resolver._download_wheel

        def counting_download(url, slug):
            download_calls.append(url)
            return wheel_path

        git_resolver._download_wheel = counting_download
        ref_url = "https://fake.example.com/smoke_whl-0.1.0.whl"

        try:
            # First call — downloads
            git_resolver.resolve_world_via_git(
                "smoke_whl",
                {"upstream_repo_url": "x", "release_ref": {"kind": "wheel-url", "value": ref_url},
                 "entry_point_module": "worlds.smoke_whl"},
                sys.executable,
            )
            first_calls = len(download_calls)

            # Second call — same ref, should skip
            git_resolver.resolve_world_via_git(
                "smoke_whl",
                {"upstream_repo_url": "x", "release_ref": {"kind": "wheel-url", "value": ref_url},
                 "entry_point_module": "worlds.smoke_whl"},
                sys.executable,
            )
        finally:
            git_resolver._download_wheel = orig_download

        self.assertEqual(first_calls, 1, "Expected exactly one download on first call")
        self.assertEqual(len(download_calls), 1, "Expected no download on second call (cached ref)")

    def test_wheel_url_list_installs_first_entry(self):
        """List-shaped release_ref: first wheel-url entry succeeds and caches."""
        wheel_path = self._wheel
        download_calls = []
        orig_download = git_resolver._download_wheel

        def counting_download(url, slug):
            download_calls.append(url)
            return wheel_path

        git_resolver._download_wheel = counting_download
        ref_url = "https://fake.example.com/smoke_whl-list-0.1.0.whl"

        try:
            entry = git_resolver.resolve_world_via_git(
                "smoke_whl_list",
                {
                    "upstream_repo_url": "x",
                    "release_ref": [
                        {"kind": "wheel-url", "value": ref_url},
                        {"kind": "wheel-url", "value": "https://fake.example.com/fallback-0.1.0.whl"},
                    ],
                    "entry_point_module": "worlds.smoke_whl",
                },
                sys.executable,
            )
        finally:
            git_resolver._download_wheel = orig_download

        self.assertEqual(entry, "worlds.smoke_whl")
        self.assertEqual(len(download_calls), 1, "Expected only first ref to be tried on success")
        self.assertEqual(download_calls[0], ref_url)
        self.assertEqual(
            git_resolver._read_cached_ref("smoke_whl_list"),
            {"kind": "wheel-url", "value": ref_url},
        )


class TestMultiRefFallback(unittest.TestCase):
    """
    Unit tests for the ordered-fallback behaviour over a list of refs.
    No real git or network calls; pip installs use the actual executable but
    against a local dummy wheel, so they are safe in CI.
    """

    def setUp(self):
        self._tmp = Path(tempfile.mkdtemp())
        self._orig_repos_root = git_resolver._repos_root
        git_resolver._repos_root = lambda: self._tmp / "repos"
        self._wheel = _make_dummy_wheel(self._tmp, slug="fallback_test")

    def tearDown(self):
        git_resolver._repos_root = self._orig_repos_root
        shutil.rmtree(str(self._tmp), ignore_errors=True)

    def test_fallback_to_second_on_first_failure(self):
        """When the first ref fails, the second ref is attempted and succeeds."""
        calls = []
        good_ref = "https://fake.example.com/fallback_test-0.1.0.whl"
        wheel = self._wheel

        def download_dispatch(url, slug):
            calls.append(url)
            if url == "https://fake.example.com/bad.whl":
                raise OSError("simulated download failure")
            return wheel

        orig = git_resolver._download_wheel
        git_resolver._download_wheel = download_dispatch
        try:
            entry = git_resolver.resolve_world_via_git(
                "fallback_test",
                {
                    "upstream_repo_url": "x",
                    "release_ref": [
                        {"kind": "wheel-url", "value": "https://fake.example.com/bad.whl"},
                        {"kind": "wheel-url", "value": good_ref},
                    ],
                    "entry_point_module": "worlds.fallback_test",
                },
                sys.executable,
            )
        finally:
            git_resolver._download_wheel = orig

        self.assertEqual(entry, "worlds.fallback_test", "Expected second ref to succeed")
        self.assertEqual(calls, ["https://fake.example.com/bad.whl", good_ref])
        state = git_resolver.get_resolver_state().get("fallback_test", "")
        self.assertIn(state, ("resolved", "cached"), f"Unexpected state: {state!r}")
        # Sentinel records the winning ref
        self.assertEqual(
            git_resolver._read_cached_ref("fallback_test"),
            {"kind": "wheel-url", "value": good_ref},
        )

    def test_all_refs_fail_produces_failed_state(self):
        """When every ref in the list fails, state starts with 'failed:'."""
        orig = git_resolver._download_wheel
        git_resolver._download_wheel = lambda url, slug: (_ for _ in ()).throw(OSError("always fails"))
        try:
            result = git_resolver.resolve_world_via_git(
                "allfail_test",
                {
                    "upstream_repo_url": "x",
                    "release_ref": [
                        {"kind": "wheel-url", "value": "https://fake.example.com/a.whl"},
                        {"kind": "wheel-url", "value": "https://fake.example.com/b.whl"},
                    ],
                    "entry_point_module": "worlds.allfail_test",
                },
                sys.executable,
            )
        finally:
            git_resolver._download_wheel = orig

        self.assertIsNone(result)
        state = git_resolver.get_resolver_state().get("allfail_test", "")
        self.assertTrue(state.startswith("failed:"), f"Unexpected state: {state!r}")
        self.assertIn("2", state, "State message should mention the count (2 refs)")

    def test_reordered_list_invalidates_cache(self):
        """If the winning ref changes position the cached dict no longer matches and re-runs."""
        wheel = self._wheel
        calls = []
        ref_a = {"kind": "wheel-url", "value": "https://fake.example.com/a.whl"}
        ref_b = {"kind": "wheel-url", "value": "https://fake.example.com/b.whl"}

        def download_dispatch(url, slug):
            calls.append(url)
            return wheel

        orig = git_resolver._download_wheel
        git_resolver._download_wheel = download_dispatch
        try:
            # First run: [ref_a, ref_b] — ref_a wins
            git_resolver.resolve_world_via_git(
                "reorder_test",
                {"upstream_repo_url": "x", "release_ref": [ref_a, ref_b],
                 "entry_point_module": "worlds.reorder_test"},
                sys.executable,
            )
            calls_after_first = list(calls)

            # Second run: [ref_b, ref_a] — ref_a is no longer the cached winner
            git_resolver.resolve_world_via_git(
                "reorder_test",
                {"upstream_repo_url": "x", "release_ref": [ref_b, ref_a],
                 "entry_point_module": "worlds.reorder_test"},
                sys.executable,
            )
        finally:
            git_resolver._download_wheel = orig

        self.assertEqual(calls_after_first, [ref_a["value"]], "First run should download ref_a")
        # Second run: ref_b is tried first and is NOT the cached winner, so it downloads
        self.assertEqual(len(calls), 2, "Second run should attempt ref_b (cache miss)")
        self.assertEqual(calls[1], ref_b["value"])

    def test_backwards_compat_single_dict(self):
        """Legacy single-dict release_ref is treated identically to a 1-element list."""
        wheel = self._wheel
        orig = git_resolver._download_wheel
        git_resolver._download_wheel = lambda url, slug: wheel
        ref_url = "https://fake.example.com/compat-0.1.0.whl"
        try:
            entry = git_resolver.resolve_world_via_git(
                "compat_test",
                {"upstream_repo_url": "x",
                 "release_ref": {"kind": "wheel-url", "value": ref_url},
                 "entry_point_module": "worlds.compat_test"},
                sys.executable,
            )
        finally:
            git_resolver._download_wheel = orig

        self.assertEqual(entry, "worlds.compat_test")
        self.assertEqual(
            git_resolver._read_cached_ref("compat_test"),
            {"kind": "wheel-url", "value": ref_url},
        )


@unittest.skipUnless(shutil.which("git"), "git not found on PATH")
class TestGitTagDispatch(unittest.TestCase):
    """
    Network test: clones a tiny public repo and checks out a pinned tag.
    Skipped automatically when git is absent or network is unreachable.
    """

    SMOKE_REPO = "https://github.com/nicowillis/git-resolver-smoke-test.git"
    SMOKE_TAG = "v0.1.0"
    SLUG = "git_smoke_tag"

    def setUp(self):
        self._tmp = Path(tempfile.mkdtemp())
        self._orig_repos_root = git_resolver._repos_root
        git_resolver._repos_root = lambda: self._tmp / "repos"

    def tearDown(self):
        git_resolver._repos_root = self._orig_repos_root
        shutil.rmtree(str(self._tmp), ignore_errors=True)

    def _network_reachable(self) -> bool:
        import urllib.request
        try:
            urllib.request.urlopen("https://github.com", timeout=5)
            return True
        except Exception:
            return False

    def test_git_tag_clone_and_checkout(self):
        if not self._network_reachable():
            self.skipTest("Network unreachable — skipping live git test")

        # We only test clone+checkout here, not pip install, to avoid polluting
        # the dev venv with a fake package.
        repo_dir = git_resolver._clone_or_update(self.SMOKE_REPO, self.SLUG, self.SMOKE_TAG)
        self.assertTrue((repo_dir / ".git").exists(), "Repo directory should contain .git")
        self.assertEqual(git_resolver._read_cached_ref(self.SLUG), self.SMOKE_TAG)

        # Second call with same ref must not re-clone (sentinel check is enough)
        repo_dir2 = git_resolver._clone_or_update(self.SMOKE_REPO, self.SLUG, self.SMOKE_TAG)
        self.assertEqual(repo_dir, repo_dir2)


# ---------------------------------------------------------------------------
# Tests for _pick_world_source precedence policy (ModuleUpdate)
# ---------------------------------------------------------------------------

class TestPickWorldSource(unittest.TestCase):
    """
    Unit tests for ModuleUpdate._pick_world_source().

    All tests are offline — no pip, no filesystem side-effects.
    We monkey-patch _parse_apworld_version so no real .apworld file is needed.
    """

    def setUp(self):
        # Ensure ModuleUpdate is importable from src/
        import importlib
        try:
            import ModuleUpdate as _mu
        except ImportError:
            self.skipTest("ModuleUpdate not importable from this working directory")
        self._mu = _mu
        self._orig_parse = _mu._parse_apworld_version

    def tearDown(self):
        self._mu._parse_apworld_version = self._orig_parse

    def _v(self, major, minor, build):
        from BaseUtils import Version
        return Version(major, minor, build)

    def _patch_apworld_ver(self, ver):
        self._mu._parse_apworld_version = lambda path: ver

    # ------------------------------------------------------------------
    # No installed wheel
    # ------------------------------------------------------------------

    def test_no_wheel_always_picks_apworld(self):
        """When no wheel is installed, always pick the .apworld regardless of its version."""
        self._patch_apworld_ver(self._v(0, 0, 0))
        result = self._mu._pick_world_source("game_x", Path("game_x.apworld"), None)
        self.assertEqual(result, "apworld")

    def test_no_wheel_nonzero_version_picks_apworld(self):
        self._patch_apworld_ver(self._v(1, 2, 3))
        result = self._mu._pick_world_source("game_x", Path("game_x.apworld"), None)
        self.assertEqual(result, "apworld")

    # ------------------------------------------------------------------
    # apworld_version > wheel_version
    # ------------------------------------------------------------------

    def test_apworld_newer_picks_apworld(self):
        self._patch_apworld_ver(self._v(2, 0, 0))
        result = self._mu._pick_world_source("game_x", Path("game_x.apworld"), self._v(1, 9, 9))
        self.assertEqual(result, "apworld")

    def test_apworld_minor_bump_picks_apworld(self):
        self._patch_apworld_ver(self._v(1, 1, 0))
        result = self._mu._pick_world_source("game_x", Path("game_x.apworld"), self._v(1, 0, 9))
        self.assertEqual(result, "apworld")

    # ------------------------------------------------------------------
    # apworld_version == wheel_version (tiebreak: wheel)
    # ------------------------------------------------------------------

    def test_equal_versions_tiebreak_to_wheel(self):
        self._patch_apworld_ver(self._v(1, 0, 0))
        result = self._mu._pick_world_source("game_x", Path("game_x.apworld"), self._v(1, 0, 0))
        self.assertEqual(result, "wheel")

    def test_both_zero_tiebreak_to_wheel(self):
        """Both missing world_version → 0.0.0 → tiebreak → wheel."""
        self._patch_apworld_ver(self._v(0, 0, 0))
        result = self._mu._pick_world_source("game_x", Path("game_x.apworld"), self._v(0, 0, 0))
        self.assertEqual(result, "wheel")

    # ------------------------------------------------------------------
    # apworld_version < wheel_version
    # ------------------------------------------------------------------

    def test_apworld_older_picks_wheel(self):
        self._patch_apworld_ver(self._v(1, 0, 0))
        result = self._mu._pick_world_source("game_x", Path("game_x.apworld"), self._v(2, 0, 0))
        self.assertEqual(result, "wheel")

    def test_apworld_zero_wheel_nonzero_picks_wheel(self):
        """apworld 0.0.0 (missing manifest) vs a real wheel version → wheel wins."""
        self._patch_apworld_ver(self._v(0, 0, 0))
        result = self._mu._pick_world_source("game_x", Path("game_x.apworld"), self._v(0, 0, 1))
        self.assertEqual(result, "wheel")

    # ------------------------------------------------------------------
    # Return type is always the literal string, not a bool
    # ------------------------------------------------------------------

    def test_return_is_literal_string(self):
        self._patch_apworld_ver(self._v(5, 0, 0))
        r1 = self._mu._pick_world_source("s", Path("s.apworld"), None)
        self.assertIsInstance(r1, str)
        self._patch_apworld_ver(self._v(0, 0, 0))
        r2 = self._mu._pick_world_source("s", Path("s.apworld"), self._v(1, 0, 0))
        self.assertIsInstance(r2, str)


if __name__ == "__main__":
    # Enable feature flag so the resolver code paths actually run
    os.environ.setdefault(git_resolver.GIT_RESOLVER_ENV_VAR, "1")
    unittest.main(verbosity=2)
