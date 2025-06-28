from . import SoEWebWorld
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version

"""
File name of the SoE US ROM World Registration

This file contains the metadata and class references for the soe world.
"""

# Required metadata
WORLD_NAME = "soe"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = SoEWebWorld
WEB_WORLD_CLASS = None
CLIENT_FUNCTION = None
