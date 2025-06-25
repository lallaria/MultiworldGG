from . import Sims4World
from . import Sims4Web

"""
The Sims 4 World Registration

This file contains the metadata and class references for the sims4 world.
"""

# Required metadata
WORLD_NAME = "sims4"
GAME_NAME = "The Sims 4"
IGDB_ID = 0
AUTHOR = "bennydreamly"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = Sims4World
WEB_WORLD_CLASS = Sims4Web
CLIENT_FUNCTION = None
