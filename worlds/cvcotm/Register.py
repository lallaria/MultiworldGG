from . import CVCotMWorld
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version
from . import CVCotMWeb

"""
Castlevania - Circle of the Moon World Registration

This file contains the metadata and class references for the cvcotm world.
"""

# Required metadata
WORLD_NAME = "cvcotm"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = CVCotMWorld
WEB_WORLD_CLASS = CVCotMWeb
CLIENT_FUNCTION = None
