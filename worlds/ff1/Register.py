from . import FF1World
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version
from . import FF1Web

"""
Final Fantasy World Registration

This file contains the metadata and class references for the ff1 world.
"""

# Required metadata
WORLD_NAME = "ff1"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = FF1World
WEB_WORLD_CLASS = FF1Web
CLIENT_FUNCTION = None
