from . import ShortHikeWorld
from . import ShortHikeWeb

"""
A Short Hike World Registration

This file contains the metadata and class references for the shorthike world.
"""

# Required metadata
WORLD_NAME = "shorthike"
GAME_NAME = "A Short Hike"
IGDB_ID = 0
AUTHOR = "chandler05 & BrandenEK"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = ShortHikeWorld
WEB_WORLD_CLASS = ShortHikeWeb
CLIENT_FUNCTION = None
