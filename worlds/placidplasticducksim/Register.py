from . import PlacidPlasticDuckSimulator, PPDSWebWorld
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version

"""
Peaks of Yore World Registration

This file contains the metadata and class references for the peaks_of_yore world.
"""

# Required metadata
WORLD_NAME = "placidplasticducksim"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = PlacidPlasticDuckSimulator
WEB_WORLD_CLASS = PPDSWebWorld
CLIENT_FUNCTION = None
