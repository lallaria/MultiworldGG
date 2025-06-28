from . import CivVIWorld
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version
from . import CivVIWeb

"""
Civilization VI World Registration

This file contains the metadata and class references for the civ_6 world.
"""

# Required metadata
WORLD_NAME = "civ_6"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = CivVIWorld
WEB_WORLD_CLASS = CivVIWeb
CLIENT_FUNCTION = None
