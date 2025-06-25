from . import ApeEscapeWorld
from . import ApeEscapeWeb

"""
Ape Escape World Registration

This file contains the metadata and class references for the apeescape world.
"""

# Required metadata
WORLD_NAME = "apeescape"
GAME_NAME = "Ape Escape"
IGDB_ID = 3762
AUTHOR = "Thedragon005"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = ApeEscapeWorld
WEB_WORLD_CLASS = ApeEscapeWeb
CLIENT_FUNCTION = None
