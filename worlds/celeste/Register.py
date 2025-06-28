from . import CelesteWebWorld, CelesteWorld
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version

"""
Celeste World Registration

This file contains the metadata and class references for the celeste world.
"""

# Required metadata
WORLD_NAME = "celeste"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = CelesteWorld
WEB_WORLD_CLASS = CelesteWebWorld
CLIENT_FUNCTION = None
