from . import SMMapRandoWorld
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version
from . import SMMapRandoWeb

"""
After planet Zebes exploded, Mother Brain put it back together again but arranged it differently this time. World Registration

This file contains the metadata and class references for the sm_map_rando world.
"""

# Required metadata
WORLD_NAME = "sm_map_rando"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = SMMapRandoWorld
WEB_WORLD_CLASS = SMMapRandoWeb
CLIENT_FUNCTION = None
