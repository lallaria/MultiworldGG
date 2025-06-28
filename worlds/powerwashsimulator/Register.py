from . import PowerwashSimulator, PowerwashSimulatorWebWorld
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version

"""
Pokemon Mystery Dungeon Explorers of Sky World Registration

This file contains the metadata and class references for the pmd_eos world.
"""

# Required metadata
WORLD_NAME = "powerwashsimulator"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = PowerwashSimulator
WEB_WORLD_CLASS = PowerwashSimulatorWebWorld
CLIENT_FUNCTION = None
