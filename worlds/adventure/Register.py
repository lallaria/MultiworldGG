from . import AdventureWorld
from . import AdventureWeb

"""
Adventure for the Atari 2600 is an early graphical adventure game. World Registration

This file contains the metadata and class references for the adventure world.
"""

# Required metadata
WORLD_NAME = "adventure"
GAME_NAME = "Adventure"
IGDB_ID = 12239
AUTHOR = "JusticePS"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = AdventureWorld
WEB_WORLD_CLASS = AdventureWeb
CLIENT_FUNCTION = None
