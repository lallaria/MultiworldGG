from . import ShiversWorld
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version
from . import ShiversWeb

"""
Shivers World Registration

This file contains the metadata and class references for the shivers world.
"""

# Required metadata
WORLD_NAME = "shivers"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = ShiversWorld
WEB_WORLD_CLASS = ShiversWeb
CLIENT_FUNCTION = None
