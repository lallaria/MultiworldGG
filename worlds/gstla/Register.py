from . import GSTLAWorld
from . import GSTLAWeb

"""
Golden Sun The Lost Age World Registration

This file contains the metadata and class references for the gstla world.
"""

# Required metadata
WORLD_NAME = "gstla"
GAME_NAME = "Golden Sun The Lost Age"
IGDB_ID = 1173
AUTHOR = "Dragion"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = GSTLAWorld
WEB_WORLD_CLASS = GSTLAWeb
CLIENT_FUNCTION = None
