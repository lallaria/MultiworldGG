from . import OuterWildsWorld, OuterWildsWebWorld

"""
Outer Wilds World Registration

This file contains the metadata and class references for the outer_wilds world.
"""

# Required metadata
WORLD_NAME = "outer_wilds"
GAME_NAME = "Outer Wilds"
IGDB_ID = 11737
AUTHOR = "Ixrec"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = OuterWildsWorld
WEB_WORLD_CLASS = OuterWildsWebWorld
CLIENT_FUNCTION = None
