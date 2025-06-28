from . import CliqueWebWorld, CliqueWorld
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version

"""
Clique World Registration

This file contains the metadata and class references for the clique world.
"""

# Required metadata
WORLD_NAME = "clique"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = CliqueWorld
WEB_WORLD_CLASS = CliqueWebWorld
CLIENT_FUNCTION = None
