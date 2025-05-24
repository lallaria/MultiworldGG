# world/mygame/__init__.py

import os
from typing import Tuple, List, Set

import settings
import typing
import threading
from BaseClasses import Region, Location, Entrance, Item, ItemClassification, MultiWorld, Tutorial
from worlds.AutoWorld import WebWorld, World
from .Logic import stage_clear_round_gates_included, stage_clear_progressive_unlocks_included, \
    stage_clear_individual_unlocks_included, get_starting_puzzle_level
from .Options import TetrisAttackOptions, StarterPack, PuzzleGoal, PuzzleInclusion, \
    PuzzleMode  # the options we defined earlier
from .Items import item_table, get_items, filler_item_names, \
    get_starter_item_names  # data used below to add items to the World
from .Locations import get_locations, location_table, TetrisAttackLocation  # same as above
from .Regions import init_areas
from .Rom import get_base_rom_path, patch_rom, TATKProcedurePatch, USAHASH
from .Rules import set_stage_clear_rules, set_goal_rules, set_puzzle_rules
from .Client import TetrisAttackSNIClient


class TetrisAttackItem(Item):
    game = "Tetris Attack"


class TetrisAttackSettings(settings.Group):
    class RomFile(settings.SNESRomPath):
        """File name of the Tetris Attack (USA) 1.0 ROM"""
        description = "Tetris Attack (USA) (En,Ja).sfc ROM File"
        copy_to = "TetrisAttack.sfc"
        md5s = [USAHASH]

    rom_file: RomFile = RomFile("Tetris Attack (USA) (En,Ja).sfc")

class TetrisAttackWebWorld(WebWorld):
    theme = "grass"

    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Tetris Attack randomizer connected to an MultiworldGG Multiworld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["AgStarRay"]
    )

    tutorials = [setup_en]

class TetrisAttackWorld(World):
    """Tetris Attack is a frantic rising blocks puzzle game. Match 3 or more same-colored panels in a row horizontally or vertically to clear them.
    Match 4 or more simultaneously for a Combo. Match more panels after the previous ones clear out for a Chain.
    In Stage Clear, each round has a set of successive stages.
    In Puzzle, all panels in each board must be fully cleared out using limited moves.
    In Vs, perform Chains and Combos to attack."""
    game = "Tetris Attack"  # name of the game/world
    author: str = "AgStarRay"
    igdb_id = 133313
    options_dataclass = TetrisAttackOptions  # options the player can set
    options: TetrisAttackOptions  # typing hints for option results
    settings: typing.ClassVar[TetrisAttackSettings]  # will be automatically assigned from type hint
    topology_present = True  # show path to required location checks in spoiler

    item_name_to_id = {item: item_table[item].code for item in item_table if item_table[item].code is not None}
    location_name_to_id = {location: location_table[location].code for location in location_table if
                           location_table[location].code is not None}

    # Items can be grouped using their names to allow easy checking if any item
    # from that group has been collected. Group names can also be used for !hint
    item_name_groups = {
    }
    
    web = TetrisAttackWebWorld()

    rom_name: bytearray
    world_version: int = 2

    def __init__(self, multiworld: MultiWorld, player: int):
        self.rom_name_available_event = threading.Event()
        super().__init__(multiworld, player)

    def generate_early(self) -> None:
        starter_item_names = get_starter_item_names(self)
        for n in starter_item_names:
            self.multiworld.push_precollected(self.create_item(n))

    def generate_output(self, output_directory: str) -> None:
        try:
            patch = TATKProcedurePatch(player=self.player, player_name=self.player_name)
            patch_rom(self, patch)

            self.rom_name = patch.name

            patch.write(os.path.join(output_directory,
                                     f"{self.multiworld.get_out_file_name_base(self.player)}{patch.patch_file_ending}"))
        except Exception:
            raise
        finally:
            self.rom_name_available_event.set()  # make sure threading continues and errors are collected

    def modify_multidata(self, multidata: dict):
        import base64
        # wait for self.rom_name to be available.
        self.rom_name_available_event.wait()
        rom_name = getattr(self, "rom_name", None)
        # we skip in case of error, so that the original error in the output thread is the one that gets raised
        if rom_name:
            new_name = base64.b64encode(bytes(self.rom_name)).decode()
            multidata["connect_names"][new_name] = multidata["connect_names"][self.multiworld.player_name[self.player]]

    def create_regions(self) -> None:
        init_areas(self, get_locations(self))

    def get_item_pool(self) -> List[Item]:
        pool: List[Item] = []

        item_data_dict = get_items(self)
        for name, data in item_data_dict.items():
            for _ in range(data.amount):
                item = self.create_item(name)
                pool.append(item)

        return pool

    def create_items(self) -> None:
        pool = self.get_item_pool()
        self.generate_filler(pool)
        self.multiworld.itempool += pool

    def generate_filler(self, pool: List[Item]) -> None:
        unfilled_locations = self.multiworld.get_unfilled_locations(self.player)
        deficit = 1 if self.options.starter_pack == StarterPack.option_stage_clear_round_6 else 0
        for _ in range(len(unfilled_locations) - len(pool) - deficit):
            item = self.create_item(self.get_filler_item_name())
            pool.append(item)

    def get_filler_item_name(self) -> str:
        return self.multiworld.random.choice(filler_item_names)

    def fill_hook(self,
                  progitempool: List["Item"],
                  usefulitempool: List["Item"],
                  filleritempool: List["Item"],
                  fill_locations: List["Location"]) -> None:
        # This is mainly to make some tests pass more often
        if self.multiworld.players > 1:
            return  # Solo multiworlds have too many local progression items
        if (self.options.puzzle_goal == PuzzleGoal.option_no_puzzle
                and self.options.puzzle_inclusion == PuzzleInclusion.option_no_puzzle
                and not self.options.stage_clear_goal and not self.options.stage_clear_inclusion):
            return  # Only seems to be a problem with Puzzle mode
        match self.options.puzzle_mode:
            case PuzzleMode.option_individual_stages:
                # Force another level onto the starting level
                starting_level = get_starting_puzzle_level(self)
                base_name = "Puzzle"
                if starting_level > 6:
                    starting_level -= 6
                    base_name = "Secret Puzzle"
                intermediate_level_unlocks = [item for item in progitempool
                                              if "Level 6" not in item.name
                                              and item.player == self.player]
                item_to_add = self.random.choice(intermediate_level_unlocks)
                items_to_add = [item for item in progitempool
                                if item.name == item_to_add.name]
                starting_level_locations = [loc for loc in fill_locations
                                            if (f"{base_name} {starting_level}-" in loc.name
                                                or f"{base_name} Round {starting_level} Clear" in loc.name)
                                            and (base_name == "Secret Puzzle" or "Secret" not in loc.name)
                                            and loc.player == self.player]
                while len(items_to_add) > 0 and len(starting_level_locations) > 0:
                    i = self.random.choice(items_to_add)
                    loc = self.random.choice(starting_level_locations)
                    loc.place_locked_item(i)
                    progitempool.remove(i)
                    fill_locations.remove(loc)
                    items_to_add.remove(i)
                    intermediate_level_unlocks.remove(i)
                    starting_level_locations.remove(loc)
                if len(starting_level_locations) > 0:
                    extra_item = self.random.choice(intermediate_level_unlocks)
                    loc = self.random.choice(starting_level_locations)
                    loc.place_locked_item(extra_item)
                    progitempool.remove(extra_item)
                    fill_locations.remove(loc)
                    intermediate_level_unlocks.remove(extra_item)
                    index = item_to_add.name.index("Unlock")
                    next_level = int(item_to_add.name[index - 2: index - 1])
                    if "Secret Puzzle" in item_to_add.name:
                        base_name = "Secret Puzzle"
                    else:
                        base_name = "Puzzle"
                    remaining_unlocks = [item for item in progitempool
                                         if extra_item.name == item.name
                                         and item.player == self.player]
                    next_level_locations = [loc for loc in fill_locations
                                            if (f"{base_name} {next_level}-" in loc.name
                                                or f"{base_name} Round {next_level} Clear" in loc.name)
                                            and (base_name == "Secret Puzzle" or "Secret" not in loc.name)
                                            and loc.player == self.player]
                    while len(remaining_unlocks) > 0 and len(next_level_locations) > 0:
                        i = self.random.choice(remaining_unlocks)
                        loc = self.random.choice(next_level_locations)
                        loc.place_locked_item(i)
                        progitempool.remove(i)
                        fill_locations.remove(loc)
                        remaining_unlocks.remove(i)
                        intermediate_level_unlocks.remove(i)
                        next_level_locations.remove(loc)
                    if len(next_level_locations) > 0:
                        last_to_add = self.random.choice(intermediate_level_unlocks)
                        remaining_unlocks = [item for item in progitempool
                                             if last_to_add.name == item.name
                                             and item.player == self.player]
                        while len(next_level_locations) > 0 and len(remaining_unlocks) > 0:
                            i = self.random.choice(remaining_unlocks)
                            loc = self.random.choice(next_level_locations)
                            loc.place_locked_item(i)
                            progitempool.remove(i)
                            fill_locations.remove(loc)
                            remaining_unlocks.remove(i)
                            next_level_locations.remove(loc)

    def create_item(self, name: str) -> TetrisAttackItem:
        data = item_table[name]
        return TetrisAttackItem(name, data.classification, data.code, self.player)

    def create_event(self, event: str) -> TetrisAttackItem:
        data = item_table[event]
        return TetrisAttackItem(event, data.classification, None, self.player)

    def set_rules(self) -> None:
        set_stage_clear_rules(self)
        set_puzzle_rules(self)
        set_goal_rules(self)
