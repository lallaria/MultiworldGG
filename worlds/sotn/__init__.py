import pkgutil
from typing import ClassVar, Dict, Tuple, Any, List

import settings, typing, os
from worlds.AutoWorld import WebWorld, World
from BaseClasses import Tutorial, MultiWorld, ItemClassification, Item
from Options import AssembleOptions

from .Items import SotnItem, items, relic_table, item_id_to_name
from .Locations import locations, SotnLocation
from .Regions import create_regions, create_regions_no_logic
from .Rules import set_rules, set_no_logic_rules
from .Options import SOTNOptions, sotn_option_groups
from .Rom import SotnProcedurePatch, write_tokens
from .client import SotNClient
#from .test_client import SotNTestClient


# Thanks for Fuzzy for Archipelago Manual it all started there
# Thanks for Wild Mouse for it´s randomizer and a lot of stuff over here
# Thanks for TalicZealot with a lot of rom addresses
# Thanks for all decomp folks
# I wish I have discovered most of those earlier, would save me a lot of RAM searches
# Thanks for all the help from the folks at Long Library and AP Discords.

class SotnSettings(settings.Group):
    class RomFile(settings.UserFilePath):
        """File name of the SOTN US rom"""
        description = "Symphony of the Night (SLU067) ROM File"
        copy_to = "Castlevania - Symphony of the Night (USA) (Track 1).bin"
        md5s = [SotnProcedurePatch.hash]

    rom_file: RomFile = RomFile(RomFile.copy_to)

    class AudioFile(settings.UserFilePath):
        """File name of the SOTN Track 2"""
        description = "Symphony of the Night (SLU067) Audio File"
        copy_to = "Castlevania - Symphony of the Night (USA) (Track 2).bin"

    audio_file: AudioFile = AudioFile(AudioFile.copy_to)


class SotnWeb(WebWorld):
    display_name = "Castlevania - Symphony of the Night"
    setup = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Symphony of the Night for MultiWorld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["FDelduque"]
    )

    tutorials = [setup]
    option_groups = sotn_option_groups


class SotnWorld(World):
    """
    Symphony of the Night is a metroidvania developed by Konami
    and released for Sony Playstation and Sega Saturn in 1997.
    """
    game: ClassVar[str] = "Symphony of the Night"
    author: ClassVar[str] = "Lockmau"
    web: ClassVar[WebWorld] = SotnWeb()
    settings_key = "sotn_settings"
    settings: ClassVar[SotnSettings]
    options_dataclass = SOTNOptions
    options: SOTNOptions
    data_version: ClassVar[int] = 1
    required_client_version: Tuple[int, int, int] = (0, 4, 5)
    extra_add = ["Duplicator", "Crissaegrim", "Ring of varda", "Mablung sword", "Masamune", "Marsil", "Yasutsuna"]

    item_name_to_id: ClassVar[Dict[str, int]] = {name: data["id"] for name, data in items.items()}
    location_name_to_id: ClassVar[Dict[str, int]] = {name: data["ap_id"] for name, data in locations.items()}

    def __init__(self, world: MultiWorld, player: int):
        super().__init__(world, player)

    @classmethod
    def stage_assert_generate(cls, _multiworld: MultiWorld) -> None:
        pass

    def generate_early(self) -> None:
        pass

    def create_item(self, name: str) -> Item:
        data = items[name]
        return SotnItem(name, data["classification"], data["id"], self.player)

    def create_items(self) -> None:
        added_items = 1  # "Reverse Center Cube - Kill Dracula"
        itempool: typing.List[SotnItem] = []
        active_locations = self.multiworld.get_unfilled_locations(self.player)
        total_location = len(active_locations)

        enemysanity = self.options.enemysanity.value
        fs_enemysanity = self.options.enemy_scroll.value

        if enemysanity and fs_enemysanity:
            items["Faerie scroll"]["classification"] = ItemClassification.progression

        loc = self.multiworld.get_location("Reverse Center Cube - Kill Dracula", self.player)
        loc.place_locked_item(self.create_event("Victory"))

        self.multiworld.completion_condition[self.player] = lambda state: state.has("Victory", self.player)

        # Add progression items
        itempool += [self.create_item("Spike breaker")]
        itempool += [self.create_item("Holy glasses")]
        itempool += [self.create_item("Gold ring")]
        itempool += [self.create_item("Silver ring")]
        added_items += 4
        added_list = ["Spike breaker", "Holy glasses", "Gold ring", "Silver ring"]
        vanilla_list = []

        # Add relics
        for r in relic_table.keys():
            itempool += [self.create_item(r)]
            added_items += 1
            added_list.append(r)

        for loc in active_locations:
            if loc.name == "Reverse Center Cube - Kill Dracula":
                continue
            if "Enemysanity" in loc.name:
                continue

            vanilla_item = locations[loc.name]["vanilla_item"]
            vanilla_list.append(vanilla_item)

        for added in added_list:
            vanilla_list.remove(added)

        if self.options.powerful_items.value:
            while len(vanilla_list) and len(self.extra_add):
                vanilla_list.pop(self.random.randrange(len(vanilla_list)))
                vanilla_list.append(self.extra_add.pop(self.random.randrange(len(self.extra_add))))

        for item in vanilla_list:
            itempool += [self.create_item(item)]
            added_items += 1

        if self.options.enemysanity.value:
            # Enemysanity adds 141 locations.
            # TODO: Add an option to customize extra locations
            extra_vessels = 0
            extra_equips = 0
            if self.options.difficult.value == 0:
                extra_vessels = 50
                extra_equips = 50
                itempool += [self.create_item("Spike breaker")]
                itempool += [self.create_item("Holy glasses")]
                itempool += [self.create_item("Gold ring")]
                itempool += [self.create_item("Silver ring")]
                added_items += 4

                for r in relic_table.keys():
                    itempool += [self.create_item(r)]
                    added_items += 1
            elif self.options.difficult.value == 1:
                extra_equips = 35
                extra_vessels = 35
                itempool += [self.create_item("Spike breaker")]
                itempool += [self.create_item("Holy glasses")]
                itempool += [self.create_item("Gold ring")]
                itempool += [self.create_item("Silver ring")]
                added_items += 4
            elif self.options.difficult.value == 2:
                extra_equips = 15
                extra_vessels = 15

            added_equip = 0
            while added_items < total_location and added_equip < extra_equips:
                rng_item = self.random.choice([i for i in range(1, 259) if i not in [126, 169, 195, 217, 226]])
                itempool += [self.create_item(item_id_to_name[rng_item])]
                added_items += 1
                added_equip += 1

            added_vessel = 0
            while added_items < total_location and added_vessel < extra_vessels:
                rng_vessel = self.random.choice([412, 423])
                itempool += [self.create_item(item_id_to_name[rng_vessel])]
                added_items += 1
                added_vessel += 1

        # Still have space? Add junk items
        itempool += [self.create_random_junk() for _ in range(total_location - added_items)]

        self.multiworld.itempool += itempool

    def create_random_junk(self) -> SotnItem:
        junk_list = ["Orange", "Apple", "Banana", "Grapes", "Strawberry", "Pineapple", "Peanuts", "Toadstool"]
        rng_junk = self.multiworld.random.choice(junk_list)
        data = items[rng_junk]
        return SotnItem(rng_junk, data["classification"], data["id"], self.player)

    def create_regions(self) -> None:
        if self.options.no_logic.value:
            create_regions_no_logic(self.multiworld, self.player, self.options)
        else:
            create_regions(self.multiworld, self.player, self.options)

    def create_event(self, name: str) -> Item:
        return SotnItem(name, ItemClassification.progression, None, self.player)

    def set_rules(self):
        if self.options.no_logic.value:
            set_no_logic_rules(self.multiworld, self.player, self.options)
        else:
            set_rules(self.multiworld, self.player, self.options)

    def fill_slot_data(self) -> Dict[str, Any]:
        option_names: List[str] = [option_name for option_name in self.options_dataclass.type_hints
                                   if option_name != "plando_items"]
        slot_data = self.options.as_dict(*option_names)
        return slot_data

    def generate_output(self, output_directory: str) -> None:
        patch = SotnProcedurePatch(player=self.player, player_name=self.player_name)

        write_tokens(self, patch)

        out_file_name = self.multiworld.get_out_file_name_base(self.player)
        patch.write(os.path.join(output_directory, f"{out_file_name}{patch.patch_file_ending}"))
