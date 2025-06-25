from . import LethalCompanyWorld
from . import LethalCompanyWeb

"""
Lethal Company World Registration

This file contains the metadata and class references for the lethal_company world.
"""

# Required metadata
WORLD_NAME = "lethal_company"
GAME_NAME = "Lethal Company"
IGDB_ID = 0
AUTHOR = "T0r1nn"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = LethalCompanyWorld
WEB_WORLD_CLASS = LethalCompanyWeb
CLIENT_FUNCTION = None
