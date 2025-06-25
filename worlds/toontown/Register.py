from . import ToontownWorld, ToontownWeb

"""
Toontown World Registration

This file contains the metadata and class references for the toontown world.
"""

# Required metadata
WORLD_NAME = "toontown"
GAME_NAME = "Toontown"
IGDB_ID = 25326
AUTHOR = "DevvyDont"
VERSION = "0.6.1"

# Plugin entry points
WORLD_CLASS = ToontownWorld
WEB_WORLD_CLASS = ToontownWeb
CLIENT_FUNCTION = None
