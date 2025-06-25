from . import DKC2World
from . import DKC2Web

"""
Donkey Kong Country 2 World Registration

This file contains the metadata and class references for the dkc2 world.
"""

# Required metadata
WORLD_NAME = "dkc2"
GAME_NAME = "Donkey Kong Country 2"
IGDB_ID = 1092
AUTHOR = "lx5"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = DKC2World
WEB_WORLD_CLASS = DKC2Web
CLIENT_FUNCTION = None
