from . import DungeonClawlerWebWorld, DungeonClawlerWorld
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version

"""
Dungeon Clawler World Registration

This file contains the metadata and class references for the dungeon_clawler world.
"""

# Required metadata
WORLD_NAME = "dungeon_clawler"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = DungeonClawlerWorld
WEB_WORLD_CLASS = DungeonClawlerWebWorld
CLIENT_FUNCTION = None
