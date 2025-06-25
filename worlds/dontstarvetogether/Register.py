from . import DSTWorld
from . import DSTWeb

"""
Don World Registration

This file contains the metadata and class references for the dontstarvetogether world.
"""

# Required metadata
WORLD_NAME = "dontstarvetogether"
GAME_NAME = "Don"
IGDB_ID = 17832
AUTHOR = "Dragon Wolf Leo"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = DSTWorld
WEB_WORLD_CLASS = DSTWeb
CLIENT_FUNCTION = None
