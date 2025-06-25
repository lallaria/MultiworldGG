from . import EarthBoundWorld
from . import EBWeb

"""
EarthBound World Registration

This file contains the metadata and class references for the earthbound world.
"""

# Required metadata
WORLD_NAME = "earthbound"
GAME_NAME = "EarthBound"
IGDB_ID = 2899
AUTHOR = "Pink Switch"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = EarthBoundWorld
WEB_WORLD_CLASS = EBWeb
CLIENT_FUNCTION = None
