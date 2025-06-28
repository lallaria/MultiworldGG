from . import PseudoregaliaWorld, PseudoregaliaWeb
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version

"""
Pseudoregalia World Registration

This file contains the metadata and class references for the pseudoregalia world.
"""

# Required metadata
WORLD_NAME = "pseudoregalia"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = PseudoregaliaWorld
WEB_WORLD_CLASS = PseudoregaliaWeb
CLIENT_FUNCTION = None
