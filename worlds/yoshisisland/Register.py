from . import YoshisIslandWorld
from . import YoshisIslandWeb

"""
Yoshi World Registration

This file contains the metadata and class references for the yoshisisland world.
"""

# Required metadata
WORLD_NAME = "yoshisisland"
GAME_NAME = "Yoshi"
IGDB_ID = 1073
AUTHOR = "Pink Switch"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = YoshisIslandWorld
WEB_WORLD_CLASS = YoshisIslandWeb
CLIENT_FUNCTION = None
