from . import UltrakillWorld
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version
from . import UltrakillWeb

"""
ULTRAKILL World Registration

This file contains the metadata and class references for the ultrakill world.
"""

# Required metadata
WORLD_NAME = "ultrakill"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = UltrakillWorld
WEB_WORLD_CLASS = UltrakillWeb
CLIENT_FUNCTION = None
