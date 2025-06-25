from . import FactorioWorld, FactorioWeb
from .Client import main

"""
Factorio Saws World Registration

This file contains the metadata and class references for the factorio_saws world.
"""

# Required metadata
WORLD_NAME = "factorio_saws"
GAME_NAME = "Factorio Space Age Without Space"
IGDB_ID = 263344
AUTHOR = "Alchav & Berserker66"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = FactorioWorld
WEB_WORLD_CLASS = FactorioWeb
CLIENT_FUNCTION = main
