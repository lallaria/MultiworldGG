from . import AnimalWellWorld
from . import AnimalWellWeb

"""
ANIMAL WELL World Registration

This file contains the metadata and class references for the animal_well world.
"""

# Required metadata
WORLD_NAME = "animal_well"
GAME_NAME = "ANIMAL WELL"
IGDB_ID = 191435
AUTHOR = "ScipioWright, RoobyRoo, Franklesby & Dicene"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = AnimalWellWorld
WEB_WORLD_CLASS = AnimalWellWeb
CLIENT_FUNCTION = None
