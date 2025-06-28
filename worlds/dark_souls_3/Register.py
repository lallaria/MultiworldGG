from . import DarkSouls3World
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version
from . import DarkSouls3Web

"""
Dark Souls III World Registration

This file contains the metadata and class references for the dark_souls_3 world.
"""

# Required metadata
WORLD_NAME = "dark_souls_3"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = DarkSouls3World
WEB_WORLD_CLASS = DarkSouls3Web
CLIENT_FUNCTION = None
