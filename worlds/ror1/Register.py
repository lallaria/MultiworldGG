from . import RoR1World
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version
from . import RiskOfWeb

"""
Risk of Rain World Registration

This file contains the metadata and class references for the ror1 world.
"""

# Required metadata
WORLD_NAME = "ror1"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = RoR1World
WEB_WORLD_CLASS = RiskOfWeb
CLIENT_FUNCTION = None
