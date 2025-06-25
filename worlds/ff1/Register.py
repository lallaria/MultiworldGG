from . import FF1World
from . import FF1Web

"""
Final Fantasy World Registration

This file contains the metadata and class references for the ff1 world.
"""

# Required metadata
WORLD_NAME = "ff1"
GAME_NAME = "Final Fantasy"
IGDB_ID = 385
AUTHOR = "jtoyoda (currently unmaintained)"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = FF1World
WEB_WORLD_CLASS = FF1Web
CLIENT_FUNCTION = None
