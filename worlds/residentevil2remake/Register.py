from . import ResidentEvil2Remake, ResidentEvil2RemakeWeb

"""
Residentevil2Remake World Registration

This file contains the metadata and class references for the residentevil2remake world.
"""

# Required metadata
WORLD_NAME = "residentevil2remake"
GAME_NAME = "Resident Evil 2 Remake"
IGDB_ID = 19686
AUTHOR = "Fuzzy"
VERSION = "0.2.7"

# Plugin entry points
WORLD_CLASS = ResidentEvil2Remake
WEB_WORLD_CLASS = ResidentEvil2RemakeWeb
CLIENT_FUNCTION = None
