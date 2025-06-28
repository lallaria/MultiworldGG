from . import HereComesNikoWebWorld
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version

"""
Here Comes Niko! World Registration

This file contains the metadata and class references for the hcniko world.
"""

# Required metadata
WORLD_NAME = "hcniko"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = HereComesNikoWebWorld
WEB_WORLD_CLASS = None
CLIENT_FUNCTION = None
