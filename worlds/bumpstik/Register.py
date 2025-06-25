from . import BumpStikWorld
from . import BumpStikWeb

"""
Bumper Stickers World Registration

This file contains the metadata and class references for the bumpstik world.
"""

# Required metadata
WORLD_NAME = "bumpstik"
GAME_NAME = "Bumper Stickers"
IGDB_ID = 271950
AUTHOR = "FelicitusNeko"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = BumpStikWorld
WEB_WORLD_CLASS = BumpStikWeb
CLIENT_FUNCTION = None
