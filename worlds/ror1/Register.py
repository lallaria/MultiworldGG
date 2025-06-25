from . import RoR1World
from . import RiskOfWeb

"""
Risk of Rain World Registration

This file contains the metadata and class references for the ror1 world.
"""

# Required metadata
WORLD_NAME = "ror1"
GAME_NAME = "Risk of Rain"
IGDB_ID = 3173
AUTHOR = "studkid"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = RoR1World
WEB_WORLD_CLASS = RiskOfWeb
CLIENT_FUNCTION = None
