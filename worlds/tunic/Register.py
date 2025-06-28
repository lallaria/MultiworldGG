from . import TunicWorld
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version
from . import TunicWeb

"""
TUNIC World Registration

This file contains the metadata and class references for the tunic world.
"""

# Required metadata
WORLD_NAME = "tunic"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = TunicWorld
WEB_WORLD_CLASS = TunicWeb
CLIENT_FUNCTION = None
