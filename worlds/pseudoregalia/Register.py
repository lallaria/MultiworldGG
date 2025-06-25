from . import PseudoregaliaWorld, PseudoregaliaWeb

"""
Pseudoregalia World Registration

This file contains the metadata and class references for the pseudoregalia world.
"""

# Required metadata
WORLD_NAME = "pseudoregalia"
GAME_NAME = "Pseudoregalia"
IGDB_ID = 259465
AUTHOR = "LittleMeowMeow & qwint"
VERSION = "0.7.0"

# Plugin entry points
WORLD_CLASS = PseudoregaliaWorld
WEB_WORLD_CLASS = PseudoregaliaWeb
CLIENT_FUNCTION = None
