from . import BrotatoWorld
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version
from . import BrotatoWeb

"""
Brotato is a top-down arena shooter roguelite where you play a potato wielding up to World Registration

This file contains the metadata and class references for the brotato world.
"""

# Required metadata
WORLD_NAME = "brotato"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = BrotatoWorld
WEB_WORLD_CLASS = BrotatoWeb
CLIENT_FUNCTION = None
