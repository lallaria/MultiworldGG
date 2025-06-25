from . import ZillionWebWorld, ZillionWorld

"""
Zillion World Registration

This file contains the metadata and class references for the zillion world.
"""

# Required metadata
WORLD_NAME = "zillion"
GAME_NAME = "Zillion"
IGDB_ID = 18141
AUTHOR = "beauxq"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = ZillionWorld
WEB_WORLD_CLASS = ZillionWebWorld
CLIENT_FUNCTION = None
