from . import PokemonCrystalWorld, PokemonCrystalWebWorld
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version

"""
Pokemon Crystal World Registration

This file contains the metadata and class references for the pokemon_crystal world.
"""

# Required metadata
WORLD_NAME = "pokemon_crystal"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = PokemonCrystalWorld
WEB_WORLD_CLASS = PokemonCrystalWebWorld
CLIENT_FUNCTION = None
