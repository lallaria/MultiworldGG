from . import KDL3World,KDL3WebWorld
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version

"""
Kirby World Registration

This file contains the metadata and class references for the kdl3 world.
"""

# Required metadata
WORLD_NAME = "kdl3"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = KDL3World
WEB_WORLD_CLASS = KDL3WebWorld
CLIENT_FUNCTION = None
