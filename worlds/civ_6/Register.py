from . import CivVIWorld
from . import CivVIWeb

"""
Civilization VI World Registration

This file contains the metadata and class references for the civ_6 world.
"""

# Required metadata
WORLD_NAME = "civ_6"
GAME_NAME = "Civilization VI"
IGDB_ID = 293
AUTHOR = "hesto2"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = CivVIWorld
WEB_WORLD_CLASS = CivVIWeb
CLIENT_FUNCTION = None
