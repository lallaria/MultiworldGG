import sys, tempfile, os, subprocess, requests, struct
import logging
from Utils import normalize_tag, tuplize_version

GITHUB_OWNER = "MultiworldGG"
GITHUB_REPO  = "MultiworldGG"
GITHUB_API_LATEST = (
    f"https://api.github.com/repos/{GITHUB_OWNER}/{GITHUB_REPO}/releases/latest"
)

def select_installer_asset(assets: list[dict]) -> dict:
    # 1) filter to only .exe assets
    exe_assets = [a for a in assets if a["name"].lower().endswith(".exe")]
    if not exe_assets:
        raise RuntimeError("No .exe installer found in release assets")

    # 2) detect local pointer size → 64 vs 32
    bits = struct.calcsize("P") * 8  # 64 or 32

    # 3) look for the asset whose name contains "64" (or "32")
    for a in exe_assets:
        name = a["name"].lower()
        if f"{bits}" in name or f"{bits}-bit" in name or f"{bits}bit" in name:
            return a

    # 4) fallback to the first exe we found
    return exe_assets[0]

def get_latest_release_info() -> tuple:
    resp = requests.get(GITHUB_API_LATEST, headers={"Accept":"application/vnd.github.v3+json"})
    resp.raise_for_status()
    data = resp.json()

    tag = normalize_tag(data["tag_name"])
    installer = select_installer_asset(data["assets"])
    download_url = installer["browser_download_url"]
    logging.info(f"latest release {tag} under url {download_url}")
    return tuplize_version(tag), download_url

def download_and_install(url: str):
    fd, path = tempfile.mkstemp(suffix=".exe")
    os.close(fd)
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(path, "wb") as f:
            for chunk in r.iter_content(8192):
                f.write(chunk)
    subprocess.Popen([path, "/SILENT", "/SUPPRESSMSGBOXES", "/RESTARTAPPLICATIONS", "/TASKS=deletelib"], shell=False)
    os._exit(0)