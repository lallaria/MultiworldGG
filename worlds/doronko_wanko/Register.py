from . import DoronkoWankoWorld
from . import DoronkoWankoWeb

"""
DORONKO WANKO World Registration

This file contains the metadata and class references for the doronko_wanko world.
"""

# Required metadata
WORLD_NAME = "doronko_wanko"
GAME_NAME = "DORONKO WANKO"
IGDB_ID = 290647
AUTHOR = "Vendily"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = DoronkoWankoWorld
WEB_WORLD_CLASS = DoronkoWankoWeb
CLIENT_FUNCTION = None
