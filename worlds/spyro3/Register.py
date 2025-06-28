from . import Spyro3World
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version
from . import Spyro3Web

"""
Spyro 3 is a game about a purple dragon who likes eggs. World Registration

This file contains the metadata and class references for the spyro3 world.
"""

# Required metadata
WORLD_NAME = "spyro3"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = Spyro3World
WEB_WORLD_CLASS = Spyro3Web
CLIENT_FUNCTION = None
