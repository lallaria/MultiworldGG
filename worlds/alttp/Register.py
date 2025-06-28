from . import ALTTPWorld
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version
from . import ALTTPWeb

"""
A Link to the Past World Registration

This file contains the metadata and class references for the alttp world.
"""

# Required metadata
WORLD_NAME = "alttp"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = ALTTPWorld
WEB_WORLD_CLASS = ALTTPWeb
CLIENT_FUNCTION = None
