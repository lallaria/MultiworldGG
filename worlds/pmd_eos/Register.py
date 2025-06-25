from . import EOSWorld
from . import EOSWeb

"""
Pokemon Mystery Dungeon Explorers of Sky World Registration

This file contains the metadata and class references for the pmd_eos world.
"""

# Required metadata
WORLD_NAME = "pmd_eos"
GAME_NAME = "Pokemon Mystery Dungeon Explorers of Sky"
IGDB_ID = 2323
AUTHOR = "CrypticMonkey33"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = EOSWorld
WEB_WORLD_CLASS = EOSWeb
CLIENT_FUNCTION = None
