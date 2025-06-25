from . import BalatroWebWorld, BalatroWorld

"""
Balatro World Registration

This file contains the metadata and class references for the balatro world.
"""

# Required metadata
WORLD_NAME = "balatro"
GAME_NAME = "Balatro"
IGDB_ID = 251833
AUTHOR = "Burndi"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = BalatroWorld
WEB_WORLD_CLASS = BalatroWebWorld
CLIENT_FUNCTION = None
