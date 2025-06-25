from . import PaperMarioWorld
from . import PaperMarioWeb

"""
Paper Mario World Registration

This file contains the metadata and class references for the papermario world.
"""

# Required metadata
WORLD_NAME = "papermario"
GAME_NAME = "Paper Mario"
IGDB_ID = 3340
AUTHOR = "JKB"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = PaperMarioWorld
WEB_WORLD_CLASS = PaperMarioWeb
CLIENT_FUNCTION = None
