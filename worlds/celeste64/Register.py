from . import Celeste64WebWorld
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version

"""
Celeste 64 World Registration

This file contains the metadata and class references for the celeste64 world.
"""

# Required metadata
WORLD_NAME = "celeste64"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = Celeste64WebWorld
WEB_WORLD_CLASS = None
CLIENT_FUNCTION = None
