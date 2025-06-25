from . import SMWorld
from . import SMWeb

"""
Super Metroid World Registration

This file contains the metadata and class references for the sm world.
"""

# Required metadata
WORLD_NAME = "sm"
GAME_NAME = "Super Metroid"
IGDB_ID = 0
AUTHOR = "lordlou"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = SMWorld
WEB_WORLD_CLASS = SMWeb
CLIENT_FUNCTION = None
