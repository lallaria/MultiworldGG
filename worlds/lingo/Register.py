from . import LingoWorld, LingoWebWorld

"""
Lingo World Registration

This file contains the metadata and class references for the lingo world.
"""

# Required metadata
WORLD_NAME = "lingo"
GAME_NAME = "Lingo"
IGDB_ID = 189169
AUTHOR = "hatkirby"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = LingoWorld
WEB_WORLD_CLASS = LingoWebWorld
CLIENT_FUNCTION = None
