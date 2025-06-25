from . import ResidentEvil3Remake, ResidentEvil3RemakeWeb

"""
Residentevil3Remake World Registration

This file contains the metadata and class references for the residentevil3remake world.
"""

# Required metadata
WORLD_NAME = "residentevil3remake"
GAME_NAME = "Resident Evil 3 Remake"
IGDB_ID = 115115
AUTHOR = "TheRealSolidusSnake"
VERSION = "0.2.3"

# Plugin entry points
WORLD_CLASS = ResidentEvil3Remake
WEB_WORLD_CLASS = ResidentEvil3RemakeWeb
CLIENT_FUNCTION = None
