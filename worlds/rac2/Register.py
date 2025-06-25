from . import Rac2World
from . import Rac2Web

"""
Ratchet & Clank 2 World Registration

This file contains the metadata and class references for the rac2 world.
"""

# Required metadata
WORLD_NAME = "rac2"
GAME_NAME = "Ratchet & Clank 2"
IGDB_ID = 1770
AUTHOR = "Evilwb"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = Rac2World
WEB_WORLD_CLASS = Rac2Web
CLIENT_FUNCTION = None
