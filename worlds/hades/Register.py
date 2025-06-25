from . import HadesWorld, HadesWeb
from .Client import launch

"""
Hades World Registration

This file contains the metadata and class references for the hades world.
"""

# Required metadata
WORLD_NAME = "hades"
GAME_NAME = "Hades"
IGDB_ID = 113112
AUTHOR = "Naix"
VERSION = "0.5.0"

# Plugin entry points
WORLD_CLASS = HadesWorld
WEB_WORLD_CLASS = HadesWeb
CLIENT_FUNCTION = launch
