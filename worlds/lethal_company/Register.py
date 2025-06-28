from . import LethalCompanyWorld
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version
from . import LethalCompanyWeb

"""
Lethal Company World Registration

This file contains the metadata and class references for the lethal_company world.
"""

# Required metadata
WORLD_NAME = "lethal_company"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = LethalCompanyWorld
WEB_WORLD_CLASS = LethalCompanyWeb
CLIENT_FUNCTION = None
