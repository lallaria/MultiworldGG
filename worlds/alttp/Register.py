from . import ALTTPWorld
from . import ALTTPWeb

"""
A Link to the Past World Registration

This file contains the metadata and class references for the alttp world.
"""

# Required metadata
WORLD_NAME = "alttp"
GAME_NAME = "A Link to the Past"
IGDB_ID = 1026
AUTHOR = "Berserker66"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = ALTTPWorld
WEB_WORLD_CLASS = ALTTPWeb
CLIENT_FUNCTION = None
