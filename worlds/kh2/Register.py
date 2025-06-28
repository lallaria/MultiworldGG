from . import KH2World
from . import KingdomHearts2Web
from .Client import launch

"""
Kingdom Hearts 2 World Registration

This file contains the metadata and class references for the kh2 world.
"""

# Required metadata
WORLD_NAME = "kh2"
GAME_NAME = "Kingdom Hearts 2"
IGDB_ID = 1221
AUTHOR = "JaredWeakStrike & Shananas"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = KH2World
WEB_WORLD_CLASS = KingdomHearts2Web
CLIENT_FUNCTION = launch
