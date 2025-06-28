from . import SonicAdventureDXWorld
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version
from . import SonicAdventureDXWeb

"""
Sonic Adventure DX World Registration

This file contains the metadata and class references for the sadx world.
"""

# Required metadata
WORLD_NAME = "sadx"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = SonicAdventureDXWorld
WEB_WORLD_CLASS = SonicAdventureDXWeb
CLIENT_FUNCTION = None
