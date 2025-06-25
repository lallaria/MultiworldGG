from . import TheBindingOfIsaacRepentanceWorld
from . import TheBindingOfIsaacRepentanceWeb

"""
The Binding of Isaac Repentance World Registration

This file contains the metadata and class references for the tboir world.
"""

# Required metadata
WORLD_NAME = "tboir"
GAME_NAME = "The Binding of Isaac Repentance"
IGDB_ID = 310643
AUTHOR = "Cyb3R"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = TheBindingOfIsaacRepentanceWorld
WEB_WORLD_CLASS = TheBindingOfIsaacRepentanceWeb
CLIENT_FUNCTION = None
