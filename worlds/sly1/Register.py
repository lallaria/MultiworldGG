from . import Sly1World
from . import Sly1Web

"""
Sly Cooper and the Thievius Raccoonus World Registration

This file contains the metadata and class references for the sly1 world.
"""

# Required metadata
WORLD_NAME = "sly1"
GAME_NAME = "Sly Cooper and the Thievius Raccoonus"
IGDB_ID = 0
AUTHOR = "Philiard"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = Sly1World
WEB_WORLD_CLASS = Sly1Web
CLIENT_FUNCTION = None
