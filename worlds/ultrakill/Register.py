from . import UltrakillWorld
from . import UltrakillWeb

"""
ULTRAKILL World Registration

This file contains the metadata and class references for the ultrakill world.
"""

# Required metadata
WORLD_NAME = "ultrakill"
GAME_NAME = "ULTRAKILL"
IGDB_ID = 124333
AUTHOR = "TRPG"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = UltrakillWorld
WEB_WORLD_CLASS = UltrakillWeb
CLIENT_FUNCTION = None
