from . import Hylics2World
from . import Hylics2Web

"""
Hylics 2 is a surreal and unusual RPG, with a bizarre yet unique visual style. Play as Wayne, World Registration

This file contains the metadata and class references for the hylics2 world.
"""

# Required metadata
WORLD_NAME = "hylics2"
GAME_NAME = "Hylics 2 is a surreal and unusual RPG, with a bizarre yet unique visual style. Play as Wayne,"
IGDB_ID = 98469
AUTHOR = "TRPG"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = Hylics2World
WEB_WORLD_CLASS = Hylics2Web
CLIENT_FUNCTION = None
