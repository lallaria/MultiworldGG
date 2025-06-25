from . import L2ACWorld
from . import L2ACWeb

"""
The Ancient Cave is a roguelike dungeon crawling game built into World Registration

This file contains the metadata and class references for the lufia2ac world.
"""

# Required metadata
WORLD_NAME = "lufia2ac"
GAME_NAME = "The Ancient Cave is a roguelike dungeon crawling game built into"
IGDB_ID = 0
AUTHOR = "el-u & word_fcuk"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = L2ACWorld
WEB_WORLD_CLASS = L2ACWeb
CLIENT_FUNCTION = None
