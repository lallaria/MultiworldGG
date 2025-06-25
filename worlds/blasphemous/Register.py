from . import BlasphemousWorld, BlasphemousWeb

"""
Blasphemous World Registration

This file contains the metadata and class references for the blasphemous world.
"""

# Required metadata
WORLD_NAME = "blasphemous"
GAME_NAME = "Blasphemous"
IGDB_ID = 26820
AUTHOR = "TRPG"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = BlasphemousWorld
WEB_WORLD_CLASS = BlasphemousWeb
CLIENT_FUNCTION = None
