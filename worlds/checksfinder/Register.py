from . import ChecksFinderWorld
from . import ChecksFinderWeb

"""
ChecksFinder World Registration

This file contains the metadata and class references for the checksfinder world.
"""

# Required metadata
WORLD_NAME = "checksfinder"
GAME_NAME = "ChecksFinder"
IGDB_ID = 0
AUTHOR = "SunCatMC"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = ChecksFinderWorld
WEB_WORLD_CLASS = ChecksFinderWeb
CLIENT_FUNCTION = None
