from . import FaxanaduWorld
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version
from . import FaxanaduWeb

"""
Faxanadu World Registration

This file contains the metadata and class references for the faxanadu world.
"""

# Required metadata
WORLD_NAME = "faxanadu"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = FaxanaduWorld
WEB_WORLD_CLASS = FaxanaduWeb
CLIENT_FUNCTION = None
