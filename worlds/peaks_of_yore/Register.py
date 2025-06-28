from . import PeaksOfWorld
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version
from . import PeaksOfWeb

"""
Peaks of Yore World Registration

This file contains the metadata and class references for the peaks_of_yore world.
"""

# Required metadata
WORLD_NAME = "peaks_of_yore"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = PeaksOfWorld
WEB_WORLD_CLASS = PeaksOfWeb
CLIENT_FUNCTION = None
