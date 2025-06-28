from . import BlasphemousWorld, BlasphemousWeb
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version

"""
Blasphemous World Registration

This file contains the metadata and class references for the blasphemous world.
"""

# Required metadata
WORLD_NAME = "blasphemous"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = BlasphemousWorld
WEB_WORLD_CLASS = BlasphemousWeb
CLIENT_FUNCTION = None
