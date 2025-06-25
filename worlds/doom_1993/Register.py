from . import DOOM1993World
from . import DOOM1993Web

"""
DOOM 1993 World Registration

This file contains the metadata and class references for the doom_1993 world.
"""

# Required metadata
WORLD_NAME = "doom_1993"
GAME_NAME = "DOOM 1993"
IGDB_ID = 673
AUTHOR = "Daivuk & Kaito Sinclaire"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = DOOM1993World
WEB_WORLD_CLASS = DOOM1993Web
CLIENT_FUNCTION = None
