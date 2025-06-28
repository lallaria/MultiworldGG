from . import TyrianWebWorld, TyrianWorld
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version

"""
Tyrian World Registration

This file contains the metadata and class references for the tyrian world.
"""

# Required metadata
WORLD_NAME = "tyrian"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = TyrianWorld
WEB_WORLD_CLASS = TyrianWebWorld
CLIENT_FUNCTION = None
