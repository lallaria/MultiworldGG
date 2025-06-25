from . import Z2World
from . import Z2Web

"""
Zelda II: The Adventure of Link World Registration

This file contains the metadata and class references for the zelda2 world.
"""

# Required metadata
WORLD_NAME = "zelda2"
GAME_NAME = "Zelda II: The Adventure of Link"
IGDB_ID = 1025
AUTHOR = "Pink Switch"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = Z2World
WEB_WORLD_CLASS = Z2Web
CLIENT_FUNCTION = None
