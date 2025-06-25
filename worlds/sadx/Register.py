from . import SonicAdventureDXWorld
from . import SonicAdventureDXWeb

"""
Sonic Adventure DX World Registration

This file contains the metadata and class references for the sadx world.
"""

# Required metadata
WORLD_NAME = "sadx"
GAME_NAME = "Sonic Adventure DX"
IGDB_ID = 192114
AUTHOR = "Classic"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = SonicAdventureDXWorld
WEB_WORLD_CLASS = SonicAdventureDXWeb
CLIENT_FUNCTION = None
