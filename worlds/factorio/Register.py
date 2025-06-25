from . import FactorioWorld, FactorioWeb
from .Client import launch

"""
Factorio World Registration

This file contains the metadata and class references for the factorio world.
"""

# Required metadata
WORLD_NAME = "factorio"
GAME_NAME = "Factorio"
IGDB_ID = 7046
AUTHOR = "Berserker66"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = FactorioWorld
WEB_WORLD_CLASS = FactorioWeb
CLIENT_FUNCTION = launch
