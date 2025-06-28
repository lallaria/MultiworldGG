from . import DLCqworld, DLCqwebworld
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version

"""
Dlcquest World Registration

This file contains the metadata and class references for the dlcquest world.
"""

# Required metadata
WORLD_NAME = "dlcquest"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = DLCqworld
WEB_WORLD_CLASS = DLCqwebworld
CLIENT_FUNCTION = None
