from typing import NamedTuple, Union
import logging
from Utils import instance_name

from BaseClasses import Item, Tutorial, ItemClassification

from ..AutoWorld import World, WebWorld
from NetUtils import SlotType

from Register import GAME_NAME, AUTHOR, IGDB_ID, VERSION

__all__ = ['WORLD_CLASS', 'WEB_WORLD_CLASS']

class GenericWeb(WebWorld):
    display_name = instance_name
    advanced_settings = Tutorial('Advanced YAML Guide',
                                 'A guide to reading YAML files and editing them to fully customize your game.',
                                 'English', 'advanced_settings_en.md', 'advanced_settings/en',
                                 ['alwaysintreble', 'Alchav'])
    commands = Tutorial('MultiworldGG Server and Client Commands',
                        'A guide detailing the commands available to the user when participating in an MultiworldGG session.',
                        'English', 'commands_en.md', 'commands/en', ['jat2980', 'Ijwu'])
    mac = Tutorial('MultiworldGG Setup Guide for Mac', 'A guide detailing how to run MultiworldGG clients on macOS.', 
                   'English', 'mac_en.md','mac/en', ['Bicoloursnake'])
    plando = Tutorial('MultiworldGG Plando Guide', 'A guide to understanding and using plando for your game.',
                      'English', 'plando_en.md', 'plando/en', ['alwaysintreble', 'Alchav'])
    setup = Tutorial('Getting Started',
                     'A guide to setting up the MultiworldGG software, and generating, hosting, and connecting to '
                     'multiworld games.',
                     'English', 'setup_en.md', 'setup/en', ['alwaysintreble'])
    triggers = Tutorial('MultiworldGG Triggers Guide', 'A guide to setting up and using triggers in your game settings.',
                        'English', 'triggers_en.md', 'triggers/en', ['alwaysintreble'])
    tutorials = [setup, mac, commands, advanced_settings, triggers, plando]


class GenericWorld(World):
    game = GAME_NAME
    author = AUTHOR
    igdb_id = IGDB_ID
    version = VERSION
    topology_present = False
    item_name_to_id = {
        "Nothing": -1
    }
    location_name_to_id = {
        "Cheat Console": -1,
        "Server": -2
    }
    hidden = True
    web = GenericWeb()

    def generate_early(self):
        self.multiworld.player_types[self.player] = SlotType.spectator  # mark as spectator

    def create_item(self, name: str) -> Item:
        if name == "Nothing":
            return Item(name, ItemClassification.filler, -1, self.player)
        raise KeyError(name)


class PlandoItem(NamedTuple):
    item: str
    location: str
    world: Union[bool, str] = False  # False -> own world, True -> not own world
    from_pool: bool = True  # if item should be removed from item pool
    force: str = 'silent'  # false -> warns if item not successfully placed. true -> errors out on failure to place item.

    def warn(self, warning: str):
        if self.force in ['true', 'fail', 'failure', 'none', 'false', 'warn', 'warning']:
            logging.warning(f'{warning}')
        else:
            logging.debug(f'{warning}')

    def failed(self, warning: str, exception=Exception):
        if self.force in ['true', 'fail', 'failure']:
            raise exception(warning)
        else:
            self.warn(warning)
