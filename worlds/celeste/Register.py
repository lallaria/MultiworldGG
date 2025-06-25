from . import CelesteWebWorld, CelesteWorld

"""
Celeste World Registration

This file contains the metadata and class references for the celeste world.
"""

# Required metadata
WORLD_NAME = "celeste"
GAME_NAME = "Celeste"
IGDB_ID = 26226
AUTHOR = "doshyw"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = CelesteWorld
WEB_WORLD_CLASS = CelesteWebWorld
CLIENT_FUNCTION = None
