from . import HadesWorld, HadesWeb
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version
from .Client import launch

"""
Hades World Registration

This file contains the metadata and class references for the hades world.
"""

# Required metadata
WORLD_NAME = "hades"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = HadesWorld
WEB_WORLD_CLASS = HadesWeb
CLIENT_FUNCTION = launch
