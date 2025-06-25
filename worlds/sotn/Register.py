from . import SotnWorld
from . import SotnWeb

"""
Symphony of the Night is a metroidvania developed by Konami World Registration

This file contains the metadata and class references for the sotn world.
"""

# Required metadata
WORLD_NAME = "sotn"
GAME_NAME = "Symphony of the Night is a metroidvania developed by Konami"
IGDB_ID = 1128
AUTHOR = "Unknown"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = SotnWorld
WEB_WORLD_CLASS = SotnWeb
CLIENT_FUNCTION = None
