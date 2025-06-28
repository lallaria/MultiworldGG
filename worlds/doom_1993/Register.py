from . import DOOM1993World
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version
from . import DOOM1993Web

"""
DOOM 1993 World Registration

This file contains the metadata and class references for the doom_1993 world.
"""

# Required metadata
WORLD_NAME = "doom_1993"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = DOOM1993World
WEB_WORLD_CLASS = DOOM1993Web
CLIENT_FUNCTION = None
