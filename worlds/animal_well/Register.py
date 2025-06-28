from . import AnimalWellWorld
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version
from . import AnimalWellWeb

"""
ANIMAL WELL World Registration

This file contains the metadata and class references for the animal_well world.
"""

# Required metadata
WORLD_NAME = "animal_well"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = AnimalWellWorld
WEB_WORLD_CLASS = AnimalWellWeb
CLIENT_FUNCTION = None
