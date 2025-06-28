from . import MomodoraWorld
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version
from . import MomodoraWeb

"""
Momodora Moonlit Farewell World Registration

This file contains the metadata and class references for the momodoramoonlitfarewell world.
"""

# Required metadata
WORLD_NAME = "momodoramoonlitfarewell"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = MomodoraWorld
WEB_WORLD_CLASS = MomodoraWeb
CLIENT_FUNCTION = None
