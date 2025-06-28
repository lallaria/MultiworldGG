from . import PokemonEmeraldWorld, PokemonEmeraldWebWorld
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version

"""
Pokemon Emerald World Registration

This file contains the metadata and class references for the pokemon_emerald world.
"""

# Required metadata
WORLD_NAME = "pokemon_emerald"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = PokemonEmeraldWorld
WEB_WORLD_CLASS = PokemonEmeraldWebWorld
CLIENT_FUNCTION = None
