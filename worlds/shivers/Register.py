from . import ShiversWorld
from . import ShiversWeb

"""
Shivers World Registration

This file contains the metadata and class references for the shivers world.
"""

# Required metadata
WORLD_NAME = "shivers"
GAME_NAME = "Shivers"
IGDB_ID = 12477
AUTHOR = "GodlFire & korydondzila"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = ShiversWorld
WEB_WORLD_CLASS = ShiversWeb
CLIENT_FUNCTION = None
