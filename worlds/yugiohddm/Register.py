from . import YGODDMWorld
from . import YGODDMWeb

"""
Yu-Gi-Oh! Dungeon Dice Monsters is a Game Boy Advance dice-based tactics game based on an original board game World Registration

This file contains the metadata and class references for the yugiohddm world.
"""

# Required metadata
WORLD_NAME = "yugiohddm"
GAME_NAME = "Yu-Gi-Oh! Dungeon Dice Monsters"
IGDB_ID = 49211
AUTHOR = "Jumza"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = YGODDMWorld
WEB_WORLD_CLASS = YGODDMWeb
CLIENT_FUNCTION = None
