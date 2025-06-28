from . import SMWorld
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version
from . import SMWeb

"""
Super Metroid World Registration

This file contains the metadata and class references for the sm world.
"""

# Required metadata
WORLD_NAME = "sm"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = SMWorld
WEB_WORLD_CLASS = SMWeb
CLIENT_FUNCTION = None
