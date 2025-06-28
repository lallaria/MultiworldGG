from . import ToontownWorld, ToontownWeb
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version

"""
Toontown World Registration

This file contains the metadata and class references for the toontown world.
"""

# Required metadata
WORLD_NAME = "toontown"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = ToontownWorld
WEB_WORLD_CLASS = ToontownWeb
CLIENT_FUNCTION = None
