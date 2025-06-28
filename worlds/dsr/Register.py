from . import DSRWorld
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version
from . import DSRWeb

"""
Dark Souls is a game where you die. World Registration

This file contains the metadata and class references for the dsr world.
"""

# Required metadata
WORLD_NAME = "dsr"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = DSRWorld
WEB_WORLD_CLASS = DSRWeb
CLIENT_FUNCTION = None
