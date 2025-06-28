from . import GSTLAWorld
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version
from . import GSTLAWeb

"""
Golden Sun The Lost Age World Registration

This file contains the metadata and class references for the gstla world.
"""

# Required metadata
WORLD_NAME = "gstla"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = GSTLAWorld
WEB_WORLD_CLASS = GSTLAWeb
CLIENT_FUNCTION = None
