from . import DoronkoWankoWorld
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version
from . import DoronkoWankoWeb

"""
DORONKO WANKO World Registration

This file contains the metadata and class references for the doronko_wanko world.
"""

# Required metadata
WORLD_NAME = "doronko_wanko"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = DoronkoWankoWorld
WEB_WORLD_CLASS = DoronkoWankoWeb
CLIENT_FUNCTION = None
