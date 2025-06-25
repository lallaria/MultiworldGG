from . import DSRWorld
from . import DSRWeb

"""
Dark Souls is a game where you die. World Registration

This file contains the metadata and class references for the dsr world.
"""

# Required metadata
WORLD_NAME = "dsr"
GAME_NAME = "Dark Souls is a game where you die."
IGDB_ID = 81085
AUTHOR = "ArsonAssassin"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = DSRWorld
WEB_WORLD_CLASS = DSRWeb
CLIENT_FUNCTION = None
