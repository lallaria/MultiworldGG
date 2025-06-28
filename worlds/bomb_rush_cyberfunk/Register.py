from . import BombRushCyberfunkWorld
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version
from . import BombRushCyberfunkWeb

"""
Bomb Rush Cyberfunk World Registration

This file contains the metadata and class references for the bomb_rush_cyberfunk world.
"""

# Required metadata
WORLD_NAME = "bomb_rush_cyberfunk"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = BombRushCyberfunkWorld
WEB_WORLD_CLASS = BombRushCyberfunkWeb
CLIENT_FUNCTION = None
