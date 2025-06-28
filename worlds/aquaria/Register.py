from . import AquariaWorld
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version
from . import AquariaWeb

"""
Aquaria is a side-scrolling action-adventure game. It follows Naija, an World Registration

This file contains the metadata and class references for the aquaria world.
"""

# Required metadata
WORLD_NAME = "aquaria"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = AquariaWorld
WEB_WORLD_CLASS = AquariaWeb
CLIENT_FUNCTION = None
