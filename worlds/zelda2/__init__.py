import os
import typing
import threading
import pkgutil


from typing import List, Set, Dict, TextIO
from BaseClasses import Item, MultiWorld, Location, Tutorial, ItemClassification
from worlds.AutoWorld import World, WebWorld
from Options import OptionGroup
import settings
from .Items import get_item_names_per_category, item_table
from .Locations import get_locations, static_locations
from .Regions import init_areas
from .Options import Z2Options, z2_option_groups
from .setup_game import setup_gamevars, place_static_items
from .Client import Zelda2Client
from .Rules import set_location_rules, set_region_rules
from .Rom import patch_rom, get_base_rom_path, Z2ProcPatch
from .game_data import world_version
from worlds.generic.Rules import add_item_rule, forbid_items_for_player


class Z2Settings(settings.Group):
    class RomFile(settings.SNESRomPath):
        """File name of the Zelda 2 US ROM"""
        description = "Zelda 2 ROM File"
        copy_to = "Zelda 2.nes"
        md5 = "764d36fa8a2450834da5e8194281035a"

    rom_file: RomFile = RomFile(RomFile.copy_to)


class Z2Web(WebWorld):
    theme = "grass"

    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Zelda 2 randomizer"
        "and connecting to an Archipelago server.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Pink Switch"]
    )

    tutorials = [setup_en]

    option_groups = z2_option_groups


class Z2World(World):
    """In the exciting sequel to Legend of Zelda, Link must find the Triforce of Courage in the Great Palace
       to awaken Zelda, cursed with a sleeping spell. Along the wy, he is being hunted by Ganon's followers,
       who seek to use his blood to revive their master."""
    
    game = "Zelda II: The Adventure of Link"
    option_definitions = Z2Options
    data_version = 1
    required_client_version = (0, 5, 0)

    item_name_to_id = {item: item_table[item].code for item in item_table}
    location_name_to_id = static_locations
    item_name_groups = get_item_names_per_category()

    web = Z2Web()
    settings: typing.ClassVar[Z2Settings]

    options_dataclass = Z2Options
    options: Z2Options

    locked_locations: List[str]
    location_cache: List[Location]

    def __init__(self, multiworld: MultiWorld, player: int):
        self.rom_name_available_event = threading.Event()
        super().__init__(multiworld, player)

        self.locked_locations = []
        self.location_cache = []
        self.event_count = 1
        self.world_version = world_version
        self.filler_items = []

    def generate_early(self):  # Todo: place locked items in generate_early
        setup_gamevars(self)

    def create_regions(self) -> None:
        init_areas(self, get_locations(self))
        place_static_items(self)

    def create_items(self) -> None:
        pool = self.get_item_pool(self.get_excluded_items())
        self.generate_filler(pool)

        self.multiworld.itempool += pool

    def set_rules(self) -> None:
        set_location_rules(self)
        self.multiworld.completion_condition[self.player] = lambda state: state.has("Triforce of Courage", self.player)

    def generate_output(self, output_directory: str):
        try:
            patch = EBProcPatch()
            patch.write_file("z2_base.bsdiff4", pkgutil.get_data(__name__, "z2_base.bsdiff4"))
            patch_rom(self, patch, self.player)

            self.rom_name = patch.name

            patch.write(os.path.join(output_directory,
                                     f"{self.multiworld.get_out_file_name_base(self.player)}{patch.patch_file_ending}"))
        except Exception:
            raise
        finally:
            self.rom_name_available_event.set()  # make sure threading continues and errors are collected

    def fill_slot_data(self) -> Dict[str, List[int]]:
        return {
            "early_boulder": self.early_boulder,
            "candle_logic": self.options.candle_logic
        }

    def modify_multidata(self, multidata: dict):
        import base64
        # wait for self.rom_name to be available.
        self.rom_name_available_event.wait()
        rom_name = getattr(self, "rom_name", None)
        if rom_name:
            new_name = base64.b64encode(bytes(self.rom_name)).decode()
            multidata["connect_names"][new_name] = multidata["connect_names"][self.multiworld.player_name[self.player]]

    # def write_spoiler_header(self, spoiler_handle: TextIO) -> None:

    def create_item(self, name: str) -> Item:
        data = item_table[name]
        return Item(name, data.classification, data.code, self.player)

    def get_filler_item_name(self) -> str:
        return self.random.choice(self.filler_items)

    def get_excluded_items(self) -> Set[str]:
        excluded_items: Set[str] = set()
        excluded_items.add(self.starting_character)

        if self.options.shuffle_teleports == 0:
            excluded_items.add("Onett Teleport")
            excluded_items.add("Twoson Teleport")
            excluded_items.add("Happy-Happy Village Teleport")
            excluded_items.add("Threed Teleport")
            excluded_items.add("Saturn Valley Teleport")
            excluded_items.add("Dusty Dunes Teleport")
            excluded_items.add("Fourside Teleport")
            excluded_items.add("Winters Teleport")
            excluded_items.add("Summers Teleport")
            excluded_items.add("Scaraba Teleport")
            excluded_items.add("Deep Darkness Teleport")
            excluded_items.add("Tenda Village Teleport")
            excluded_items.add("Lost Underworld Teleport")
            excluded_items.add("Magicant Teleport")
            excluded_items.add("Progressive Poo PSI")
            excluded_items.add("Dalaam Teleport")
        elif self.options.magicant_mode not in [0, 3]:
            excluded_items.add("Magicant Teleport")

        if self.options.character_shuffle == 0:
            excluded_items.add("Ness")
            excluded_items.add("Paula")
            excluded_items.add("Jeff")
            excluded_items.add("Poo")
            excluded_items.add("Flying Man")

        if self.options.progressive_weapons:
            excluded_items.add("Magicant Bat")
            excluded_items.add("Legendary Bat")
            excluded_items.add("Pop Gun")
            excluded_items.add("Stun Gun")
            excluded_items.add("Death Ray")
            excluded_items.add("Moon Beam Gun")

        if self.options.progressive_armor:
            excluded_items.add("Platinum Band")
            excluded_items.add("Diamond Band")
            excluded_items.add("Pixie's Bracelet")
            excluded_items.add("Cherub's Band")
            excluded_items.add("Goddess Band")
            excluded_items.add("Coin of Slumber")
            excluded_items.add("Souvenir Coin")
            excluded_items.add("Mr. Saturn Coin")

        if not self.options.no_free_sanctuaries:
            excluded_items.add("Tiny Key")
            excluded_items.add("Tenda Lavapants")

        return excluded_items

    def set_classifications(self, name: str) -> Item:
        data = item_table[name]
        item = Item(name, data.classification, data.code, self.player)
        return item

    def generate_filler(self, pool: List[Item]) -> None:
        for _ in range(len(self.multiworld.get_unfilled_locations(self.player)) - len(pool) - self.event_count):
            item = self.set_classifications(self.get_filler_item_name())
            pool.append(item)

    def get_item_pool(self, excluded_items: Set[str]) -> List[Item]:
        pool: List[Item] = []

        for name, data in item_table.items():
            if name not in excluded_items:
                for _ in range(data.amount):
                    item = self.set_classifications(name)
                    pool.append(item)

        return pool
