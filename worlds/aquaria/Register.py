from . import AquariaWorld
from . import AquariaWeb

"""
Aquaria is a side-scrolling action-adventure game. It follows Naija, an World Registration

This file contains the metadata and class references for the aquaria world.
"""

# Required metadata
WORLD_NAME = "aquaria"
GAME_NAME = "Aquaria"
IGDB_ID = 7406
AUTHOR = "tioui"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = AquariaWorld
WEB_WORLD_CLASS = AquariaWeb
CLIENT_FUNCTION = None
