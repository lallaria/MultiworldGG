from . import DOOM2World
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version
from . import DOOM2Web

"""
DOOM II World Registration

This file contains the metadata and class references for the doom_ii world.
"""

# Required metadata
WORLD_NAME = "doom_ii"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = DOOM2World
WEB_WORLD_CLASS = DOOM2Web
CLIENT_FUNCTION = None
