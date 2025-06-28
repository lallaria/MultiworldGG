from . import GenericWorld
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version
from . import GenericWeb

"""
Generic World Registration

This file contains the metadata and class references for the generic world.
"""

# Required metadata
WORLD_NAME = "generic"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = GenericWorld
WEB_WORLD_CLASS = GenericWeb
CLIENT_FUNCTION = None
