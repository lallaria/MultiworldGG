from . import RLWorld
from . import RLWeb

"""
Rogue Legacy World Registration

This file contains the metadata and class references for the rogue_legacy world.
"""

# Required metadata
WORLD_NAME = "rogue_legacy"
GAME_NAME = "Rogue Legacy"
IGDB_ID = 3221
AUTHOR = "Phar"
VERSION = "0.3.5"

# Plugin entry points
WORLD_CLASS = RLWorld
WEB_WORLD_CLASS = RLWeb
CLIENT_FUNCTION = None
