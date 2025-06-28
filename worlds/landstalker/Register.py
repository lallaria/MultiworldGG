from . import LandstalkerWorld, LandstalkerWeb
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version

"""
Landstalker - The Treasures of King Nole World Registration

This file contains the metadata and class references for the landstalker world.
"""

# Required metadata
WORLD_NAME = "landstalker"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = LandstalkerWorld
WEB_WORLD_CLASS = LandstalkerWeb
CLIENT_FUNCTION = None
