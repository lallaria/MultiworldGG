from . import UFO50World
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version
from . import UFO50Web

"""
UFO 50 World Registration

This file contains the metadata and class references for the ufo50 world.
"""

# Required metadata
WORLD_NAME = "ufo50"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = UFO50World
WEB_WORLD_CLASS = UFO50Web
CLIENT_FUNCTION = None
