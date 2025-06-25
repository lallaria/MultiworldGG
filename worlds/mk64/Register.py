from . import MK64World
from . import MK64Web

"""
Mario Kart 64 World Registration

This file contains the metadata and class references for the mk64 world.
"""

# Required metadata
WORLD_NAME = "mk64"
GAME_NAME = "Mario Kart 64"
IGDB_ID = 2342
AUTHOR = "Edsploration"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = MK64World
WEB_WORLD_CLASS = MK64Web
CLIENT_FUNCTION = None
