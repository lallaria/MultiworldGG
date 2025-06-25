from . import SavingPrincessWorld
from . import SavingPrincessWeb

"""
Explore a space station crawling with rogue machines and even rival bounty hunters World Registration

This file contains the metadata and class references for the saving_princess world.
"""

# Required metadata
WORLD_NAME = "saving_princess"
GAME_NAME = "Explore a space station crawling with rogue machines and even rival bounty hunters"
IGDB_ID = 0
AUTHOR = "LeonarthCG"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = SavingPrincessWorld
WEB_WORLD_CLASS = SavingPrincessWeb
CLIENT_FUNCTION = None
