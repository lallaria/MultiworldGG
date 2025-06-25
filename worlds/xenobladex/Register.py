from . import XenobladeXWorld
from . import XenobladeXWeb

"""
Xenoblade X World Registration

This file contains the metadata and class references for the xenobladex world.
"""

# Required metadata
WORLD_NAME = "xenobladex"
GAME_NAME = "Xenoblade X"
IGDB_ID = 2366
AUTHOR = "Maragon"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = XenobladeXWorld
WEB_WORLD_CLASS = XenobladeXWeb
CLIENT_FUNCTION = None
