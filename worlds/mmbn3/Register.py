from . import MMBN3World
from . import MMBN3Web

"""
MegaMan Battle Network 3 World Registration

This file contains the metadata and class references for the mmbn3 world.
"""

# Required metadata
WORLD_NAME = "mmbn3"
GAME_NAME = "MegaMan Battle Network 3"
IGDB_ID = 0
AUTHOR = "digiholic"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = MMBN3World
WEB_WORLD_CLASS = MMBN3Web
CLIENT_FUNCTION = None
