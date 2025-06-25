from . import DKC3World
from . import DKC3Web

"""
Donkey Kong Country 3 is an action platforming game. World Registration

This file contains the metadata and class references for the dkc3 world.
"""

# Required metadata
WORLD_NAME = "dkc3"
GAME_NAME = "Donkey Kong Country 3 is an action platforming game."
IGDB_ID = 1094
AUTHOR = "PoryGone"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = DKC3World
WEB_WORLD_CLASS = DKC3Web
CLIENT_FUNCTION = None
