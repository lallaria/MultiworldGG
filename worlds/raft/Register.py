from . import RaftWorld, RaftWeb

"""
Raft World Registration

This file contains the metadata and class references for the raft world.
"""

# Required metadata
WORLD_NAME = "raft"
GAME_NAME = "Raft"
IGDB_ID = 27082
AUTHOR = "SunnyBat"
VERSION = "0.3.4"

# Plugin entry points
WORLD_CLASS = RaftWorld
WEB_WORLD_CLASS = RaftWeb
CLIENT_FUNCTION = None
