from . import MeritousWorld
from . import MeritousWeb

"""
Meritous Gaiden is a procedurally generated bullet-hell dungeon crawl game. World Registration

This file contains the metadata and class references for the meritous world.
"""

# Required metadata
WORLD_NAME = "meritous"
GAME_NAME = "Meritous Gaiden is a procedurally generated bullet-hell dungeon crawl game."
IGDB_ID = 78479
AUTHOR = "FelicitusNeko"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = MeritousWorld
WEB_WORLD_CLASS = MeritousWeb
CLIENT_FUNCTION = None
