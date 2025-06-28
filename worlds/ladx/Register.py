from . import LinksAwakeningWorld, LinksAwakeningWebWorld
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version
from .LinksAwakeningClient import launch

"""
Link World Registration

This file contains the metadata and class references for the ladx world.
"""

# Required metadata
WORLD_NAME = "ladx"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = LinksAwakeningWorld
WEB_WORLD_CLASS = LinksAwakeningWebWorld
CLIENT_FUNCTION = launch
