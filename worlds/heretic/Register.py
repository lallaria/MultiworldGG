from . import HereticWorld, HereticWeb

"""
Heretic World Registration

This file contains the metadata and class references for the heretic world.
"""

# Required metadata
WORLD_NAME = "heretic"
GAME_NAME = "Heretic"
IGDB_ID = 6362
AUTHOR = "Daivuk & Kaito Sinclaire"
VERSION = "0.5.0"

# Plugin entry points
WORLD_CLASS = HereticWorld
WEB_WORLD_CLASS = HereticWeb
CLIENT_FUNCTION = None
