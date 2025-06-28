from BaseClasses import Tutorial
from ..AutoWorld import World, WebWorld
from .Constants import GAME_NAME, AUTHOR, IGDB_ID
from worlds.LauncherComponents import Component, components, launch_subprocess, Type
from functools import partial
from typing import cast, ClassVar
from .Slot import generate_slot_data
from .Regions import init_region
from .Items import xenobladeXItems, create_items, create_item, XenobladeXItem
from .Rules import set_rules
from .Locations import create_locations, xenobladeXLocations
from .Options import XenobladeXOptions
from .Settings import XenobladeXSettings


def launch_client(*args):
    from .Client import launch
    launch_subprocess(partial(launch, *args), name="XenobladeXClient")


components.append(Component("Xenoblade X Client", func=launch_client, component_type=Type.CLIENT,
                            game_name="Xenoblade X", supports_uri=True))


class XenobladeXWeb(WebWorld):
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Xenoblade Chronicles X for Multiworld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Maragon"]
    )]


class XenobladeXWorld(World):
    """
     Xenoblade Chronicles X another 100+ hour game. Sounds like fun?
    """

    game = GAME_NAME
    author: str = AUTHOR
    igdb_id = IGDB_ID
    topology_present = True
    web = XenobladeXWeb()

    data_version = 0
    base_id: int = 4100000

    options_dataclass = XenobladeXOptions

    settings: ClassVar[XenobladeXSettings]  # type: ignore

    item_name_to_id = (lambda b_id: {item.get_item(): b_id + item.id
                                     for item in xenobladeXItems if item.id is not None})(base_id)
    location_name_to_id = (lambda b_id: {location.get_location(): b_id + location.id
                                         for location in xenobladeXLocations if location.id is not None})(base_id)

    def create_regions(self):
        init_region(self.multiworld, self.player, "Menu")
        create_locations(self.multiworld, self.player, self.base_id)

    def create_items(self):
        create_items(self.multiworld, self.player, self.base_id, self.options, self.item_name_to_id)

    def create_item(self, name: str) -> XenobladeXItem:
        return create_item(name, self.player, self.item_name_to_id[name])

    def set_rules(self):
        set_rules(self.multiworld, self.player, self.item_name_to_id)

    def generate_early(self):
        pass

    def generate_basic(self):
        pass

    def fill_slot_data(self) -> dict[str, object]:
        return generate_slot_data(cast(XenobladeXOptions, self.options))
