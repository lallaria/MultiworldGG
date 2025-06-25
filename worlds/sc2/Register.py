from . import Starcraft2WebWorld

"""
Starcraft 2 World Registration

This file contains the metadata and class references for the sc2 world.
"""

# Required metadata
WORLD_NAME = "sc2"
GAME_NAME = "Starcraft 2"
IGDB_ID = 239
AUTHOR = "Ziktofel"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = Starcraft2WebWorld
WEB_WORLD_CLASS = None
CLIENT_FUNCTION = None
