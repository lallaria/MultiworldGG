from . import HKWorld
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version
from . import HKWeb

"""
Hollow Knight World Registration

This file contains the metadata and class references for the hk world.
"""

# Required metadata
WORLD_NAME = "hk"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = HKWorld
WEB_WORLD_CLASS = HKWeb
CLIENT_FUNCTION = None
