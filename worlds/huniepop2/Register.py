from . import HuniePop2, HuniePop2Web
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version

"""
Huniepop2 World Registration

This file contains the metadata and class references for the huniepop2 world.
"""

# Required metadata
WORLD_NAME = "huniepop2"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = HuniePop2
WEB_WORLD_CLASS = HuniePop2Web
CLIENT_FUNCTION = None
