from . import FFMQWebWorld

"""
Final Fantasy Mystic Quest World Registration

This file contains the metadata and class references for the ffmq world.
"""

# Required metadata
WORLD_NAME = "ffmq"
GAME_NAME = "Final Fantasy Mystic Quest"
IGDB_ID = 415
AUTHOR = "Alchav"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = FFMQWebWorld
WEB_WORLD_CLASS = None
CLIENT_FUNCTION = None
