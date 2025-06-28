from . import RaftWorld, RaftWeb
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version

"""
Raft World Registration

This file contains the metadata and class references for the raft world.
"""

# Required metadata
WORLD_NAME = "raft"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = RaftWorld
WEB_WORLD_CLASS = RaftWeb
CLIENT_FUNCTION = None
