from . import DarkSouls3World
from . import DarkSouls3Web

"""
Dark Souls III World Registration

This file contains the metadata and class references for the dark_souls_3 world.
"""

# Required metadata
WORLD_NAME = "dark_souls_3"
GAME_NAME = "Dark Souls III"
IGDB_ID = 11133
AUTHOR = "Marech & nex3"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = DarkSouls3World
WEB_WORLD_CLASS = DarkSouls3Web
CLIENT_FUNCTION = None
