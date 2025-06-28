from . import Z2World
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version
from . import Z2Web

"""
Zelda II: The Adventure of Link World Registration

This file contains the metadata and class references for the zelda2 world.
"""

# Required metadata
WORLD_NAME = "zelda2"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = Z2World
WEB_WORLD_CLASS = Z2Web
CLIENT_FUNCTION = None
