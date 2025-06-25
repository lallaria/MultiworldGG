from . import PaintWorld, PaintWebWorld

"""
Paint World Registration

This file contains the metadata and class references for the paint world.
"""

# Required metadata
WORLD_NAME = "paint"
GAME_NAME = "Paint"
IGDB_ID = 0
AUTHOR = "MairoManTAW"
VERSION = "0.5.0"

# Plugin entry points
WORLD_CLASS = PaintWorld
WEB_WORLD_CLASS = PaintWebWorld
CLIENT_FUNCTION = None
