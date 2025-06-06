from __future__ import annotations
import pkgutil
import json
import os
from typing import TYPE_CHECKING

def postMessage(message: str) -> None:
    print(message)

def getFile(filename: str) -> bytes:
    try:
        data = pkgutil.get_data(__name__, filename)
        if data is not None:
            return data
    except Exception as e:
        print(f"[getFile] pkgutil.get_data({filename!r}) error: {e!r}")

    if os.path.isfile(filename):
        try:
            with open(filename, "rb") as f:
                return f.read()
        except Exception as e:
            print(f"[getFile] open({filename!r}, 'rb') error: {e!r}")

    fallback = os.path.join("worlds", "dk64", filename)
    if os.path.isfile(fallback):
        try:
            with open(fallback, "rb") as f:
                return f.read()
        except Exception as e:
            print(f"[getFile] open fallback({fallback!r}) error: {e!r}")

    raise FileNotFoundError(f"Could not load file: {filename}")

def getStringFile(filename: str) -> str:
    try:
        print(f"[getStringFile] trying pkgutil.get_data for {filename!r}")
        data = pkgutil.get_data(__name__, filename)
        if data is not None:
            return data.decode()
    except Exception as e:
        print(f"[getStringFile] pkgutil.get_data({filename!r}) error: {e!r}")

    print(f"[getStringFile] trying open({filename!r})")
    if os.path.isfile(filename):
        try:
            with open(filename, "r") as f:
                return f.read()
        except Exception as e:
            print(f"[getStringFile] open({filename!r}, 'r') error: {e!r}")

    print(f"[getStringFile] trying open fallback for {filename!r}")
    fallback = os.path.join("worlds", "dk64", filename)
    if os.path.isfile(fallback):
        try:
            with open(fallback, "r") as f:
                return f.read()
        except Exception as e:
            print(f"[getStringFile] open fallback({fallback!r}) error: {e!r}")

    raise FileNotFoundError(f"Could not load text file: {filename}")

def load_json_from_paths(relative_paths: list[str]) -> dict | None:
    for path in relative_paths:
        try:
            raw = pkgutil.get_data(__name__, path)
            if raw is not None:
                return json.loads(raw)
        except Exception as e:
            print(f"[load_json_from_paths] pkgutil.get_data({path!r}) error: {e!r}")

        if os.path.isfile(path):
            try:
                with open(path, "rb") as f:
                    return json.loads(f.read())
            except Exception as e:
                print(f"[load_json_from_paths] open({path!r}, 'rb') error: {e!r}")

        fallback = os.path.join("worlds", "dk64", path)
        if os.path.isfile(fallback):
            try:
                with open(fallback, "rb") as f:
                    return json.loads(f.read())
            except Exception as e:
                print(f"[load_json_from_paths] open fallback({fallback!r}) error: {e!r}")

    raise FileNotFoundError(f"Could not find any of: {relative_paths}")

try:
    pointer_addresses = load_json_from_paths([
        "static/patches/pointer_addresses.json"
    ])
    rom_symbols = load_json_from_paths([
        "static/patches/symbols.json"
    ])
except FileNotFoundError as e:
    print(f"[module import] JSON load error: {e!r}")
    pointer_addresses = None
    rom_symbols = None
