from . import BalatroWebWorld, BalatroWorld
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version

"""
Balatro World Registration

This file contains the metadata and class references for the balatro world.
"""

# Required metadata
WORLD_NAME = "balatro"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = BalatroWorld
WEB_WORLD_CLASS = BalatroWebWorld
CLIENT_FUNCTION = None
