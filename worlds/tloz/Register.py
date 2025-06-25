from . import TLoZWorld
from . import TLoZWeb

"""
The Legend of Zelda World Registration

This file contains the metadata and class references for the tloz world.
"""

# Required metadata
WORLD_NAME = "tloz"
GAME_NAME = "The Legend of Zelda"
IGDB_ID = 1022
AUTHOR = "Rosalie-A & t3hf1gm3nt"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = TLoZWorld
WEB_WORLD_CLASS = TLoZWeb
CLIENT_FUNCTION = None
