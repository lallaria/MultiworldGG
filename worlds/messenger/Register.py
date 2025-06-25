from . import MessengerWorld
from . import MessengerWeb

"""
The Messenger World Registration

This file contains the metadata and class references for the messenger world.
"""

# Required metadata
WORLD_NAME = "messenger"
GAME_NAME = "The Messenger"
IGDB_ID = 71628
AUTHOR = "alwaysintreble"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = MessengerWorld
WEB_WORLD_CLASS = MessengerWeb
CLIENT_FUNCTION = None
