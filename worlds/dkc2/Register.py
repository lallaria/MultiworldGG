from . import DKC2World
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version
from . import DKC2Web

"""
Donkey Kong Country 2 World Registration

This file contains the metadata and class references for the dkc2 world.
"""

# Required metadata
WORLD_NAME = "dkc2"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = DKC2World
WEB_WORLD_CLASS = DKC2Web
CLIENT_FUNCTION = None
