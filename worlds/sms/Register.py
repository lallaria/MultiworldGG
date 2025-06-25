from . import SmsWebWorld

"""
Super Mario Sunshine World Registration

This file contains the metadata and class references for the sms world.
"""

# Required metadata
WORLD_NAME = "sms"
GAME_NAME = "Super Mario Sunshine"
IGDB_ID = 1075
AUTHOR = "Joshark"
VERSION = "0.2.0"

# Plugin entry points
WORLD_CLASS = SmsWebWorld
WEB_WORLD_CLASS = None
CLIENT_FUNCTION = None
