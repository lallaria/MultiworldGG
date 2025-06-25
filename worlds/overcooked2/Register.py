from . import Overcooked2World
from . import Overcooked2Web

"""
Overcooked! 2 World Registration

This file contains the metadata and class references for the overcooked2 world.
"""

# Required metadata
WORLD_NAME = "overcooked2"
GAME_NAME = "Overcooked! 2"
IGDB_ID = 103341
AUTHOR = "toasterparty"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = Overcooked2World
WEB_WORLD_CLASS = Overcooked2Web
CLIENT_FUNCTION = None
