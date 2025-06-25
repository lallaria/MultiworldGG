from . import TrackerWorld, launch_client

"""
Universal Tracker World Registration

This file contains the metadata and class references for the tracker world.
"""

# Required metadata
WORLD_NAME = "tracker"
GAME_NAME = "Universal Tracker"
IGDB_ID = 0
AUTHOR = "Unknown"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = TrackerWorld
CLIENT_FUNCTION = launch_client
