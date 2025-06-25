from . import PeaksOfWorld
from . import PeaksOfWeb

"""
Peaks of Yore World Registration

This file contains the metadata and class references for the peaks_of_yore world.
"""

# Required metadata
WORLD_NAME = "peaks_of_yore"
GAME_NAME = "Peaks of Yore"
IGDB_ID = 238690
AUTHOR = "c0der23"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = PeaksOfWorld
WEB_WORLD_CLASS = PeaksOfWeb
CLIENT_FUNCTION = None
