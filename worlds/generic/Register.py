from . import GenericWorld
from . import GenericWeb

"""
Generic World Registration

This file contains the metadata and class references for the generic world.
"""

# Required metadata
WORLD_NAME = "generic"
GAME_NAME = "Generic"
IGDB_ID = 0
AUTHOR = "Unknown"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = GenericWorld
WEB_WORLD_CLASS = GenericWeb
CLIENT_FUNCTION = None
