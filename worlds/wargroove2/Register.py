from . import Wargroove2World
from . import Wargroove2Web

"""
Wargroove 2 World Registration

This file contains the metadata and class references for the wargroove2 world.
"""

# Required metadata
WORLD_NAME = "wargroove2"
GAME_NAME = "Wargroove 2"
IGDB_ID = 241149
AUTHOR = "Fly Sniper"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = Wargroove2World
WEB_WORLD_CLASS = Wargroove2Web
CLIENT_FUNCTION = None
