from . import MMBN3World
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version
from . import MMBN3Web

"""
MegaMan Battle Network 3 World Registration

This file contains the metadata and class references for the mmbn3 world.
"""

# Required metadata
WORLD_NAME = "mmbn3"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = MMBN3World
WEB_WORLD_CLASS = MMBN3Web
CLIENT_FUNCTION = None
