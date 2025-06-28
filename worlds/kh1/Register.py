from . import KH1World
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version
from . import KH1Web

"""
Kingdom Hearts World Registration

This file contains the metadata and class references for the kh1 world.
"""

# Required metadata
WORLD_NAME = "kh1"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = KH1World
WEB_WORLD_CLASS = KH1Web
CLIENT_FUNCTION = None
