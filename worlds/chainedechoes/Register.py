from . import ChainedEchoesWorld
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version
from . import ChainedEchoesWeb

"""
Chained Echoes World Registration

This file contains the metadata and class references for the chainedechoes world.
"""

# Required metadata
WORLD_NAME = "chainedechoes"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = ChainedEchoesWorld
WEB_WORLD_CLASS = ChainedEchoesWeb
CLIENT_FUNCTION = None
