from . import SMWWorld
from . import SMWWeb

"""
Super Mario World is an action platforming game. World Registration

This file contains the metadata and class references for the smw world.
"""

# Required metadata
WORLD_NAME = "smw"
GAME_NAME = "Super Mario World is an action platforming game."
IGDB_ID = 1070
AUTHOR = "PoryGone"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = SMWWorld
WEB_WORLD_CLASS = SMWWeb
CLIENT_FUNCTION = None
