from .world import ZorkGrandInquisitorWorld, ZorkGrandInquisitorWebWorld
from .client import main

"""
Zork Grand Inquisitor World Registration

This file contains the metadata and class references for the zork_grand_inquisitor world.
"""

# Required metadata
WORLD_NAME = "zork_grand_inquisitor"
GAME_NAME = "Zork Grand Inquisitor"
IGDB_ID = 1955
AUTHOR = "nbrochu"
VERSION = "0.6.0"

# Plugin entry points
WORLD_CLASS = ZorkGrandInquisitorWorld
WEB_WORLD_CLASS = ZorkGrandInquisitorWebWorld
CLIENT_FUNCTION = main
