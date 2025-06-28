from . import PaintWorld, PaintWebWorld
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version

"""
Paint World Registration

This file contains the metadata and class references for the paint world.
"""

# Required metadata
WORLD_NAME = "paint"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = PaintWorld
WEB_WORLD_CLASS = PaintWebWorld
CLIENT_FUNCTION = None
