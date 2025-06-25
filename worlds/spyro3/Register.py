from . import Spyro3World
from . import Spyro3Web

"""
Spyro 3 is a game about a purple dragon who likes eggs. World Registration

This file contains the metadata and class references for the spyro3 world.
"""

# Required metadata
WORLD_NAME = "spyro3"
GAME_NAME = "Spyro 3 is a game about a purple dragon who likes eggs."
IGDB_ID = 1578
AUTHOR = "ArsonAssassin"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = Spyro3World
WEB_WORLD_CLASS = Spyro3Web
CLIENT_FUNCTION = None
