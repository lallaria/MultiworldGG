from . import SotnWorld
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version
from . import SotnWeb

"""
Symphony of the Night is a metroidvania developed by Konami World Registration

This file contains the metadata and class references for the sotn world.
"""

# Required metadata
WORLD_NAME = "sotn"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = SotnWorld
WEB_WORLD_CLASS = SotnWeb
CLIENT_FUNCTION = None
