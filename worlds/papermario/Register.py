from . import PaperMarioWorld
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version
from . import PaperMarioWeb

"""
Paper Mario World Registration

This file contains the metadata and class references for the papermario world.
"""

# Required metadata
WORLD_NAME = "papermario"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = PaperMarioWorld
WEB_WORLD_CLASS = PaperMarioWeb
CLIENT_FUNCTION = None
