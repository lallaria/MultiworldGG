from . import WargrooveWorld
from . import WargrooveWeb

"""
Wargroove World Registration

This file contains the metadata and class references for the wargroove world.
"""

# Required metadata
WORLD_NAME = "wargroove"
GAME_NAME = "Wargroove"
IGDB_ID = 27441
AUTHOR = "FlySniper"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = WargrooveWorld
WEB_WORLD_CLASS = WargrooveWeb
CLIENT_FUNCTION = None
