from . import HuniePop, HuniePopWeb
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version

"""
Huniepop World Registration

This file contains the metadata and class references for the huniepop world.
"""

# Required metadata
WORLD_NAME = "huniepop"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = HuniePop
WEB_WORLD_CLASS = HuniePopWeb
CLIENT_FUNCTION = None
