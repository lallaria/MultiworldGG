from . import DKCWorld
from . import DKCWeb

"""
Donkey Kong Country World Registration

This file contains the metadata and class references for the dkc world.
"""

# Required metadata
WORLD_NAME = "dkc"
GAME_NAME = "Donkey Kong Country"
IGDB_ID = 1090
AUTHOR = "lx5"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = DKCWorld
WEB_WORLD_CLASS = DKCWeb
CLIENT_FUNCTION = None
