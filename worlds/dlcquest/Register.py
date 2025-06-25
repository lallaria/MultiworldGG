from . import DLCqworld, DLCqwebworld

"""
Dlcquest World Registration

This file contains the metadata and class references for the dlcquest world.
"""

# Required metadata
WORLD_NAME = "dlcquest"
GAME_NAME = "DLCQuest"
IGDB_ID = 3004
AUTHOR = "axe-y & Kaito Kid"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = DLCqworld
WEB_WORLD_CLASS = DLCqwebworld
CLIENT_FUNCTION = None
