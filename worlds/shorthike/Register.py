from . import ShortHikeWorld
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version
from . import ShortHikeWeb

"""
A Short Hike World Registration

This file contains the metadata and class references for the shorthike world.
"""

# Required metadata
WORLD_NAME = "shorthike"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = ShortHikeWorld
WEB_WORLD_CLASS = ShortHikeWeb
CLIENT_FUNCTION = None
