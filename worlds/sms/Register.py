from . import SmsWebWorld
from .Constants import GAME_NAME as game_name, AUTHOR as author, IGDB_ID as igdb_id, VERSION as version

"""
Super Mario Sunshine World Registration

This file contains the metadata and class references for the sms world.
"""

# Required metadata
WORLD_NAME = "sms"
GAME_NAME = game_name
IGDB_ID = igdb_id
AUTHOR = author
VERSION = version

# Plugin entry points
WORLD_CLASS = SmsWebWorld
WEB_WORLD_CLASS = None
CLIENT_FUNCTION = None
