from . import ChainedEchoesWorld
from . import ChainedEchoesWeb

"""
Chained Echoes World Registration

This file contains the metadata and class references for the chainedechoes world.
"""

# Required metadata
WORLD_NAME = "chainedechoes"
GAME_NAME = "Chained Echoes"
IGDB_ID = 117271
AUTHOR = "SergioAlonso"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = ChainedEchoesWorld
WEB_WORLD_CLASS = ChainedEchoesWeb
CLIENT_FUNCTION = None
