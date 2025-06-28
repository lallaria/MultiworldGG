from . import CatQuestWorld, CatQuestWeb
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version

"""
Cat Quest World Registration

This file contains the metadata and class references for the cat_quest world.
"""

# Required metadata
WORLD_NAME = "cat_quest"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = CatQuestWorld
WEB_WORLD_CLASS = CatQuestWeb
CLIENT_FUNCTION = None
