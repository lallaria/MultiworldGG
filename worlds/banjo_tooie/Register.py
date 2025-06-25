from . import BanjoTooieWorld
from . import BanjoTooieWeb

"""
Banjo-Tooie is a single-player platform game in which the protagonists are controlled from a third-person perspective. World Registration

This file contains the metadata and class references for the banjo_tooie world.
"""

# Required metadata
WORLD_NAME = "banjo_tooie"
GAME_NAME = "Banjo-Tooie is a single-player platform game in which the protagonists are controlled from a third-person perspective."
IGDB_ID = 0
AUTHOR = "jjjj12212"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = BanjoTooieWorld
WEB_WORLD_CLASS = BanjoTooieWeb
CLIENT_FUNCTION = None
