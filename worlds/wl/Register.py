from . import WLWorld
from . import WLWeb

"""
Wario Land: Super Mario Land 3 is a 1994 platform game developed and published by Nintendo for the Game Boy. World Registration

This file contains the metadata and class references for the wl world.
"""

# Required metadata
WORLD_NAME = "wl"
GAME_NAME = "Wario Land: Super Mario Land 3 is a 1994 platform game developed and published by Nintendo for the Game Boy."
IGDB_ID = 0
AUTHOR = "rand0"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = WLWorld
WEB_WORLD_CLASS = WLWeb
CLIENT_FUNCTION = None
