from . import CatQuestWorld, CatQuestWeb

"""
Cat Quest World Registration

This file contains the metadata and class references for the cat_quest world.
"""

# Required metadata
WORLD_NAME = "cat_quest"
GAME_NAME = "Cat Quest"
IGDB_ID = 36597
AUTHOR = "Nikkilite"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = CatQuestWorld
WEB_WORLD_CLASS = CatQuestWeb
CLIENT_FUNCTION = None
