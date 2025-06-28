from . import WordipelagoWebWorld, WordipelagoWorld
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version

"""
Wordipelago World Registration

This file contains the metadata and class references for the wordipelago world.
"""

# Required metadata
WORLD_NAME = "wordipelago"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = WordipelagoWorld
WEB_WORLD_CLASS = WordipelagoWebWorld
CLIENT_FUNCTION = None
