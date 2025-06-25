from . import BrotatoWorld
from . import BrotatoWeb

"""
Brotato is a top-down arena shooter roguelite where you play a potato wielding up to World Registration

This file contains the metadata and class references for the brotato world.
"""

# Required metadata
WORLD_NAME = "brotato"
GAME_NAME = "Brotato"
IGDB_ID = 199116
AUTHOR = "RampagingHippy"
VERSION = "0.1.0"

# Plugin entry points
WORLD_CLASS = BrotatoWorld
WEB_WORLD_CLASS = BrotatoWeb
CLIENT_FUNCTION = None
