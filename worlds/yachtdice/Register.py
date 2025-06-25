from . import YachtDiceWorld
from . import YachtDiceWeb

"""
Yacht Dice is a straightforward game, custom-made for Archipelago, World Registration

This file contains the metadata and class references for the yachtdice world.
"""

# Required metadata
WORLD_NAME = "yachtdice"
GAME_NAME = "Yacht Dice is a straightforward game, custom-made for Archipelago,"
IGDB_ID = 0
AUTHOR = "Spineraks"
VERSION = "2.2.3"

# Plugin entry points
WORLD_CLASS = YachtDiceWorld
WEB_WORLD_CLASS = YachtDiceWeb
CLIENT_FUNCTION = None
