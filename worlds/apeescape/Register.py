from . import ApeEscapeWorld
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version
from . import ApeEscapeWeb

"""
Ape Escape World Registration

This file contains the metadata and class references for the apeescape world.
"""

# Required metadata
WORLD_NAME = "apeescape"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = ApeEscapeWorld
WEB_WORLD_CLASS = ApeEscapeWeb
CLIENT_FUNCTION = None
