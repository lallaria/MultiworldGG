from . import DOOM2World
from . import DOOM2Web

"""
DOOM II World Registration

This file contains the metadata and class references for the doom_ii world.
"""

# Required metadata
WORLD_NAME = "doom_ii"
GAME_NAME = "DOOM II"
IGDB_ID = 312
AUTHOR = "Daivuk & Kaito Sinclaire"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = DOOM2World
WEB_WORLD_CLASS = DOOM2Web
CLIENT_FUNCTION = None
