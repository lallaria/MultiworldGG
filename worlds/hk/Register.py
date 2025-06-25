from . import HKWorld
from . import HKWeb

"""
Hollow Knight World Registration

This file contains the metadata and class references for the hk world.
"""

# Required metadata
WORLD_NAME = "hk"
GAME_NAME = "Hollow Knight"
IGDB_ID = 0
AUTHOR = "BadMagic"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = HKWorld
WEB_WORLD_CLASS = HKWeb
CLIENT_FUNCTION = None
