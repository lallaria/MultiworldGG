from . import CVCotMWorld
from . import CVCotMWeb

"""
Castlevania - Circle of the Moon World Registration

This file contains the metadata and class references for the cvcotm world.
"""

# Required metadata
WORLD_NAME = "cvcotm"
GAME_NAME = "Castlevania - Circle of the Moon"
IGDB_ID = 1132
AUTHOR = "LiquidCat64"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = CVCotMWorld
WEB_WORLD_CLASS = CVCotMWeb
CLIENT_FUNCTION = None
