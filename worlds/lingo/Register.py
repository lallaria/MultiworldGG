from . import LingoWorld, LingoWebWorld
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version

"""
Lingo World Registration

This file contains the metadata and class references for the lingo world.
"""

# Required metadata
WORLD_NAME = "lingo"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = LingoWorld
WEB_WORLD_CLASS = LingoWebWorld
CLIENT_FUNCTION = None
