from . import NoitaWorld, NoitaWeb
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version

"""
Noita World Registration

This file contains the metadata and class references for the noita world.
"""

# Required metadata
WORLD_NAME = "noita"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = NoitaWorld
WEB_WORLD_CLASS = NoitaWeb
CLIENT_FUNCTION = None
