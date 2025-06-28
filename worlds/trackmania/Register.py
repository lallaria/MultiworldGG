from . import TrackmaniaWorld, TrackmaniaWeb, launch_client
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version

"""
Trackmania World Registration

This file contains the metadata and class references for the trackmania world.
"""

# Required metadata
WORLD_NAME = "trackmania"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = TrackmaniaWorld
WEB_WORLD_CLASS = TrackmaniaWeb
CLIENT_FUNCTION = launch_client
