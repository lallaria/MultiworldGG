from . import DS2World
from . import DarkSouls2Web

"""
Dark Souls II World Registration

This file contains the metadata and class references for the dark_souls_2 world.
"""

# Required metadata
WORLD_NAME = "dark_souls_2"
GAME_NAME = "Dark Souls II"
IGDB_ID = 2368
AUTHOR = "WildBunnie"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = DS2World
WEB_WORLD_CLASS = DarkSouls2Web
CLIENT_FUNCTION = None
