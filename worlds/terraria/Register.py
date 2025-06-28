from . import TerrariaWorld
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version
from . import TerrariaWeb

"""
Terraria World Registration

This file contains the metadata and class references for the terraria world.
"""

# Required metadata
WORLD_NAME = "terraria"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = TerrariaWorld
WEB_WORLD_CLASS = TerrariaWeb
CLIENT_FUNCTION = None
