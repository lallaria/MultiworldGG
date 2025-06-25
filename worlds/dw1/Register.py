from . import DigimonWorldWorld
from . import DigimonWorldWeb

"""
Digimon World is a game about raising digital monsters and recruiting allies to save the digital world. World Registration

This file contains the metadata and class references for the dw1 world.
"""

# Required metadata
WORLD_NAME = "dw1"
GAME_NAME = "Digimon World is a game about raising digital monsters and recruiting allies to save the digital world."
IGDB_ID = 3878
AUTHOR = "ArsonAssassin"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = DigimonWorldWorld
WEB_WORLD_CLASS = DigimonWorldWeb
CLIENT_FUNCTION = None
