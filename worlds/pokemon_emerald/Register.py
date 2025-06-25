from . import PokemonEmeraldWorld, PokemonEmeraldWebWorld

"""
Pokemon Emerald World Registration

This file contains the metadata and class references for the pokemon_emerald world.
"""

# Required metadata
WORLD_NAME = "pokemon_emerald"
GAME_NAME = "Pokemon Emerald"
IGDB_ID = 1517
AUTHOR = "Zunawe"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = PokemonEmeraldWorld
WEB_WORLD_CLASS = PokemonEmeraldWebWorld
CLIENT_FUNCTION = None
