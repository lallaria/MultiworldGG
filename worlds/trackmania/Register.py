from . import TrackmaniaWorld, TrackmaniaWeb, launch_client

"""
Trackmania World Registration

This file contains the metadata and class references for the trackmania world.
"""

# Required metadata
WORLD_NAME = "trackmania"
GAME_NAME = "Trackmania"
IGDB_ID = 0
AUTHOR = "SerialBoxes"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = TrackmaniaWorld
WEB_WORLD_CLASS = TrackmaniaWeb
CLIENT_FUNCTION = launch_client
