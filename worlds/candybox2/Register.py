from . import CandyBox2WebWorld
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version

"""
Candy Box 2 World Registration

This file contains the metadata and class references for the candybox2 world.
"""

# Required metadata
WORLD_NAME = "candybox2"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = CandyBox2WebWorld
WEB_WORLD_CLASS = None
CLIENT_FUNCTION = None
