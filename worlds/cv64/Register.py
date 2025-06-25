from . import CV64World
from . import CV64Web

"""
Castlevania 64 World Registration

This file contains the metadata and class references for the cv64 world.
"""

# Required metadata
WORLD_NAME = "cv64"
GAME_NAME = "Castlevania 64"
IGDB_ID = 1130
AUTHOR = "LiquidCat64"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = CV64World
WEB_WORLD_CLASS = CV64Web
CLIENT_FUNCTION = None
