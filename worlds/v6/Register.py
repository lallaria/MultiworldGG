from . import V6World
from . import V6Web

"""
VVVVVV is a platform game all about exploring one simple mechanical idea - what if you reversed gravity instead of jumping? World Registration

This file contains the metadata and class references for the v6 world.
"""

# Required metadata
WORLD_NAME = "v6"
GAME_NAME = "VVVVVV is a platform game all about exploring one simple mechanical idea - what if you reversed gravity instead of jumping?"
IGDB_ID = 0
AUTHOR = "N00byKing"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = V6World
WEB_WORLD_CLASS = V6Web
CLIENT_FUNCTION = None
