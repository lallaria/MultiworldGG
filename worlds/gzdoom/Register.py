from . import GZDoomWorld
from . import GZDoomWeb

"""
gzDoom World Registration

This file contains the metadata and class references for the gzdoom world.
"""

# Required metadata
WORLD_NAME = "gzdoom"
GAME_NAME = "gzDoom"
IGDB_ID = 0
AUTHOR = "ToxicFrog"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = GZDoomWorld
WEB_WORLD_CLASS = GZDoomWeb
CLIENT_FUNCTION = None
