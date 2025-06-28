from . import EarthBoundWorld
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version
from . import EBWeb

"""
EarthBound World Registration

This file contains the metadata and class references for the earthbound world.
"""

# Required metadata
WORLD_NAME = "earthbound"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = EarthBoundWorld
WEB_WORLD_CLASS = EBWeb
CLIENT_FUNCTION = None
