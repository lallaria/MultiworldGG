from . import RiskOfRainWorld
from . import RiskOfWeb

"""
Risk of Rain 2 World Registration

This file contains the metadata and class references for the ror2 world.
"""

# Required metadata
WORLD_NAME = "ror2"
GAME_NAME = "Risk of Rain 2"
IGDB_ID = 28512
AUTHOR = "Sneaki"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = RiskOfRainWorld
WEB_WORLD_CLASS = RiskOfWeb
CLIENT_FUNCTION = None
