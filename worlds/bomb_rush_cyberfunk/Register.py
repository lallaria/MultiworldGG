from . import BombRushCyberfunkWorld
from . import BombRushCyberfunkWeb

"""
Bomb Rush Cyberfunk World Registration

This file contains the metadata and class references for the bomb_rush_cyberfunk world.
"""

# Required metadata
WORLD_NAME = "bomb_rush_cyberfunk"
GAME_NAME = "Bomb Rush Cyberfunk"
IGDB_ID = 135940
AUTHOR = "CookieCat45"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = BombRushCyberfunkWorld
WEB_WORLD_CLASS = BombRushCyberfunkWeb
CLIENT_FUNCTION = None
