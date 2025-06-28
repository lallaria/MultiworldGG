from . import MK64World
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version
from . import MK64Web

"""
Mario Kart 64 World Registration

This file contains the metadata and class references for the mk64 world.
"""

# Required metadata
WORLD_NAME = "mk64"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = MK64World
WEB_WORLD_CLASS = MK64Web
CLIENT_FUNCTION = None
