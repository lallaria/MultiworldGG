from . import SubnauticaWorld, SubnauticaWeb
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version

"""
Subnautica World Registration

This file contains the metadata and class references for the subnautica world.
"""

# Required metadata
WORLD_NAME = "subnautica"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = SubnauticaWorld
WEB_WORLD_CLASS = SubnauticaWeb
CLIENT_FUNCTION = None
