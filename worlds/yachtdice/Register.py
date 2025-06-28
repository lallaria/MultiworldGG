from . import YachtDiceWorld
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version
from . import YachtDiceWeb

"""
Yacht Dice is a straightforward game, custom-made for Archipelago, World Registration

This file contains the metadata and class references for the yachtdice world.
"""

# Required metadata
WORLD_NAME = "yachtdice"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = YachtDiceWorld
WEB_WORLD_CLASS = YachtDiceWeb
CLIENT_FUNCTION = None
