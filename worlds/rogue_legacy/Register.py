from . import RLWorld
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version
from . import RLWeb

"""
Rogue Legacy World Registration

This file contains the metadata and class references for the rogue_legacy world.
"""

# Required metadata
WORLD_NAME = "rogue_legacy"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = RLWorld
WEB_WORLD_CLASS = RLWeb
CLIENT_FUNCTION = None
