from . import SpireWorld
from . import SpireWeb

"""
Slay the Spire World Registration

This file contains the metadata and class references for the spire world.
"""

# Required metadata
WORLD_NAME = "spire"
GAME_NAME = "Slay the Spire"
IGDB_ID = 296831
AUTHOR = "KonoTyran"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = SpireWorld
WEB_WORLD_CLASS = SpireWeb
CLIENT_FUNCTION = None
