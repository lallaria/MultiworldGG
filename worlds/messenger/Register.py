from . import MessengerWorld
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version
from . import MessengerWeb

"""
The Messenger World Registration

This file contains the metadata and class references for the messenger world.
"""

# Required metadata
WORLD_NAME = "messenger"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = MessengerWorld
WEB_WORLD_CLASS = MessengerWeb
CLIENT_FUNCTION = None
