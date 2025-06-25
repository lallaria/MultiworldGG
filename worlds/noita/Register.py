from . import NoitaWorld, NoitaWeb

"""
Noita World Registration

This file contains the metadata and class references for the noita world.
"""

# Required metadata
WORLD_NAME = "noita"
GAME_NAME = "Noita"
IGDB_ID = 52006
AUTHOR = "ScipioWright & heinermann"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = NoitaWorld
WEB_WORLD_CLASS = NoitaWeb
CLIENT_FUNCTION = None
