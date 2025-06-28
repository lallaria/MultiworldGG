from . import DS2World
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version
from . import DarkSouls2Web

"""
Dark Souls II World Registration

This file contains the metadata and class references for the dark_souls_2 world.
"""

# Required metadata
WORLD_NAME = "dark_souls_2"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = DS2World
WEB_WORLD_CLASS = DarkSouls2Web
CLIENT_FUNCTION = None
