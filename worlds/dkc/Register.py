from . import DKCWorld
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version
from . import DKCWeb

"""
Donkey Kong Country World Registration

This file contains the metadata and class references for the dkc world.
"""

# Required metadata
WORLD_NAME = "dkc"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = DKCWorld
WEB_WORLD_CLASS = DKCWeb
CLIENT_FUNCTION = None
