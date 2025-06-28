from . import TheBindingOfIsaacRepentanceWorld
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version
from . import TheBindingOfIsaacRepentanceWeb

"""
The Binding of Isaac Repentance World Registration

This file contains the metadata and class references for the tboir world.
"""

# Required metadata
WORLD_NAME = "tboir"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = TheBindingOfIsaacRepentanceWorld
WEB_WORLD_CLASS = TheBindingOfIsaacRepentanceWeb
CLIENT_FUNCTION = None
