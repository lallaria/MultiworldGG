from . import PokemonCrystalWorld, PokemonCrystalWebWorld

"""
Pokemon Crystal World Registration

This file contains the metadata and class references for the pokemon_crystal world.
"""

# Required metadata
WORLD_NAME = "pokemon_crystal"
GAME_NAME = "Pokemon Crystal"
IGDB_ID = 1514
AUTHOR = "James"
VERSION = "4.0.3"

# Plugin entry points
WORLD_CLASS = PokemonCrystalWorld
WEB_WORLD_CLASS = PokemonCrystalWebWorld
CLIENT_FUNCTION = None
