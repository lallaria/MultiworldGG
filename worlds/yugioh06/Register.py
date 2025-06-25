from . import Yugioh06World
from . import Yugioh06Web

"""
Yu-Gi-Oh! 2006 World Registration

This file contains the metadata and class references for the yugioh06 world.
"""

# Required metadata
WORLD_NAME = "yugioh06"
GAME_NAME = "Yu-Gi-Oh! 2006"
IGDB_ID = 49377
AUTHOR = "Rensen3"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = Yugioh06World
WEB_WORLD_CLASS = Yugioh06Web
CLIENT_FUNCTION = None
