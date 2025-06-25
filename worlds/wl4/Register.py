from . import WL4World
from . import WL4Web

"""
A golden pyramid has been discovered deep in the jungle, and Wario has set World Registration

This file contains the metadata and class references for the wl4 world.
"""

# Required metadata
WORLD_NAME = "wl4"
GAME_NAME = "A golden pyramid has been discovered deep in the jungle, and Wario has set"
IGDB_ID = 0
AUTHOR = "lil David"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = WL4World
WEB_WORLD_CLASS = WL4Web
CLIENT_FUNCTION = None
