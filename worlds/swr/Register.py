from . import SWRWorld
from . import SWRWeb

"""
Star Wars Episode I: Racer is a racing game where the player wins prize money and buys upgrades for their vehicle. World Registration

This file contains the metadata and class references for the swr world.
"""

# Required metadata
WORLD_NAME = "swr"
GAME_NAME = "Star Wars Episode I: Racer is a racing game where the player wins prize money and buys upgrades for their vehicle."
IGDB_ID = 0
AUTHOR = "Johnny Hamcobbler"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = SWRWorld
WEB_WORLD_CLASS = SWRWeb
CLIENT_FUNCTION = None
