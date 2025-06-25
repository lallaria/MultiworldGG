from . import TerrariaWorld
from . import TerrariaWeb

"""
Terraria World Registration

This file contains the metadata and class references for the terraria world.
"""

# Required metadata
WORLD_NAME = "terraria"
GAME_NAME = "Terraria"
IGDB_ID = 1879
AUTHOR = "Seldom-SE"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = TerrariaWorld
WEB_WORLD_CLASS = TerrariaWeb
CLIENT_FUNCTION = None
