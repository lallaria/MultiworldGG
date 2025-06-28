from . import CV64World
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version
from . import CV64Web

"""
Castlevania 64 World Registration

This file contains the metadata and class references for the cv64 world.
"""

# Required metadata
WORLD_NAME = "cv64"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = CV64World
WEB_WORLD_CLASS = CV64Web
CLIENT_FUNCTION = None
