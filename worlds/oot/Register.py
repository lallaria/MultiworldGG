from . import OOTWorld
from . import OOTWeb

"""
The Legend of Zelda: Ocarina of Time is a 3D action/adventure game. Travel through Hyrule in two time periods, World Registration

This file contains the metadata and class references for the oot world.
"""

# Required metadata
WORLD_NAME = "oot"
GAME_NAME = "The Legend of Zelda: Ocarina of Time is a 3D action/adventure game. Travel through Hyrule in two time periods,"
IGDB_ID = 1029
AUTHOR = "espeon65536 (currenty unmaintained)"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = OOTWorld
WEB_WORLD_CLASS = OOTWeb
CLIENT_FUNCTION = None
