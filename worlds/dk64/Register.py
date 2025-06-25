from . import DK64World
from . import DK64Web

"""
Donkey Kong 64 is a 3D collectathon platforming game. World Registration

This file contains the metadata and class references for the dk64 world.
"""

# Required metadata
WORLD_NAME = "dk64"
GAME_NAME = "Donkey Kong 64 is a 3D collectathon platforming game."
IGDB_ID = 0
AUTHOR = "2dos, Killklli, & Ballaam"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = DK64World
WEB_WORLD_CLASS = DK64Web
CLIENT_FUNCTION = None
