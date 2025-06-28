from . import MarioLand2WebWorld
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version

"""
Super Mario Land 2 World Registration

This file contains the metadata and class references for the marioland2 world.
"""

# Required metadata
WORLD_NAME = "marioland2"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = MarioLand2WebWorld
WEB_WORLD_CLASS = None
CLIENT_FUNCTION = None
