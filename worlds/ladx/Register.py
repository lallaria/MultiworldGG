from . import LinksAwakeningWorld, LinksAwakeningWebWorld
from .LinksAwakeningClient import launch

"""
Link World Registration

This file contains the metadata and class references for the ladx world.
"""

# Required metadata
WORLD_NAME = "ladx"
GAME_NAME = "Link's Awakening DX Beta"
IGDB_ID = 1027
AUTHOR = "threeandthree"
VERSION = "12.0"

# Plugin entry points
WORLD_CLASS = LinksAwakeningWorld
WEB_WORLD_CLASS = LinksAwakeningWebWorld
CLIENT_FUNCTION = launch
