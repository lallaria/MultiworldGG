from . import UFO50World
from . import UFO50Web

"""
UFO 50 World Registration

This file contains the metadata and class references for the ufo50 world.
"""

# Required metadata
WORLD_NAME = "ufo50"
GAME_NAME = "UFO 50"
IGDB_ID = 54555
AUTHOR = "LeonarthCG & ScipioWright"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = UFO50World
WEB_WORLD_CLASS = UFO50Web
CLIENT_FUNCTION = None
