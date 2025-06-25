from . import DungeonClawlerWebWorld, DungeonClawlerWorld

"""
Dungeon Clawler World Registration

This file contains the metadata and class references for the dungeon_clawler world.
"""

# Required metadata
WORLD_NAME = "dungeon_clawler"
GAME_NAME = "Dungeon Clawler"
IGDB_ID = 290897
AUTHOR = "Kaito Kid"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = DungeonClawlerWorld
WEB_WORLD_CLASS = DungeonClawlerWebWorld
CLIENT_FUNCTION = None
