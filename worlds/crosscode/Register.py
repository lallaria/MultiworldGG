from .world import CrossCodeWorld, CrossCodeWebWorld

"""
Crosscode World Registration

This file contains the metadata and class references for the crosscode world.
"""

# Required metadata
WORLD_NAME = "crosscode"
GAME_NAME = "CrossCode"
IGDB_ID = 35282
AUTHOR = "CodeTriangle"
VERSION = "0.5"

# Plugin entry points
WORLD_CLASS = CrossCodeWorld
WEB_WORLD_CLASS = CrossCodeWebWorld
CLIENT_FUNCTION = None
