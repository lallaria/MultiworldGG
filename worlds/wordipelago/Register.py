from . import WordipelagoWebWorld, WordipelagoWorld

"""
Wordipelago World Registration

This file contains the metadata and class references for the wordipelago world.
"""

# Required metadata
WORLD_NAME = "wordipelago"
GAME_NAME = "Wordipelago"
IGDB_ID = 0
AUTHOR = "ProfDeCube"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = WordipelagoWorld
WEB_WORLD_CLASS = WordipelagoWebWorld
CLIENT_FUNCTION = None
