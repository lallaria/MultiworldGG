from . import L2ACWorld
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version
from . import L2ACWeb

"""
The Ancient Cave is a roguelike dungeon crawling game built into World Registration

This file contains the metadata and class references for the lufia2ac world.
"""

# Required metadata
WORLD_NAME = "lufia2ac"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = L2ACWorld
WEB_WORLD_CLASS = L2ACWeb
CLIENT_FUNCTION = None
