from . import ResidentEvil2Remake, ResidentEvil2RemakeWeb
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version

"""
Residentevil2Remake World Registration

This file contains the metadata and class references for the residentevil2remake world.
"""

# Required metadata
WORLD_NAME = "residentevil2remake"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = ResidentEvil2Remake
WEB_WORLD_CLASS = ResidentEvil2RemakeWeb
CLIENT_FUNCTION = None
