from . import FaxanaduWorld
from . import FaxanaduWeb

"""
Faxanadu World Registration

This file contains the metadata and class references for the faxanadu world.
"""

# Required metadata
WORLD_NAME = "faxanadu"
GAME_NAME = "Faxanadu"
IGDB_ID = 1974
AUTHOR = "Daivuk"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = FaxanaduWorld
WEB_WORLD_CLASS = FaxanaduWeb
CLIENT_FUNCTION = None
