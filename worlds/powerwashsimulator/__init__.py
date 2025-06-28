import math
from typing import Dict, Any, ClassVar, List
from worlds.AutoWorld import World, WebWorld
from BaseClasses import Location, Region, Item, ItemClassification, Tutorial
from .Items import raw_items, PowerwashSimulatorItem, item_table, create_items, unlock_items, filler_items
from .Locations import location_dict, raw_location_dict, locations_percentages, land_vehicles, objectsanity_dict
from .Options import PowerwashSimulatorOptions, PowerwashSimulatorSettings, check_options

uuid_offset = 0x3AF4F1BC

class PowerwashSimulatorWebWorld(WebWorld):
    setup_en = Tutorial(
        tutorial_name="Start Guide",
        description="A guide to playing Powerwash Simulator in MultiworldGG.",
        language="English",
        file_name="setup_en.md",
        link="setup/en",
        authors=["SW_CreeperKing"]
    )

    tutorials = [setup_en]

class PowerwashSimulator(World):
    """
    Powerwash Simulator
    """
    game = "Powerwash Simulator"
    author: str = "SW_CreeperKing"
    web = PowerwashSimulatorWebWorld()
    options_dataclass = PowerwashSimulatorOptions
    options: PowerwashSimulatorOptions
    settings: ClassVar[PowerwashSimulatorSettings]
    location_name_to_id = {value: location_dict.index(value) + uuid_offset for value in location_dict}
    item_name_to_id = {value: raw_items.index(value) + uuid_offset for value in raw_items}
    starting_location = land_vehicles[0]
    mcguffin_requirement = 0
    item_steps: Dict[str, int] = {}
    filler_locations: List[str] = []
    goal_levels: List[str] = ["None"]
    goal_level_count: int = -1
    item_name_groups = {
        "unlocks": unlock_items
    }

    def generate_early(self) -> None:
        option_locations = self.options.get_locations()
        check_options(self)

        option_location_count = len(option_locations)
        percentsanity = self.options.percentsanity

        self.item_steps["total"] = 0
        self.item_steps["percentsanity"] = (len(range(percentsanity, 100, percentsanity)) + 1) * option_location_count
        self.item_steps["objectsanity"] = sum(len(objectsanity_dict[loc]) for loc in option_locations)

        if self.options.has_percentsanity():
            self.item_steps["total"] += self.item_steps["percentsanity"]

        if self.options.has_objectsanity():
            self.item_steps["total"] += self.item_steps["objectsanity"]

        self.item_steps["unlocks"] = option_location_count - 1
        self.item_steps["raw mcguffins"] = option_location_count if self.options.goal_type == 0 else 0
        self.item_steps["progression before added"] = self.item_steps["unlocks"] + self.item_steps["raw mcguffins"]

        self.item_steps["added mcguffins"] = math.floor(
            (self.item_steps["total"] - self.item_steps[
                "progression before added"]) * .075) if self.options.goal_type == 0 else 0

        self.item_steps["total mcguffins"] = self.item_steps["raw mcguffins"] + self.item_steps["added mcguffins"]

        self.item_steps["total progression"] = self.item_steps["progression before added"] + self.item_steps[
            "added mcguffins"]

        self.item_steps["filler"] = math.floor(
            (self.item_steps["total"] - self.item_steps["total progression"]) * self.options.local_fill / 100.0)

        if self.options.goal_type == 1:
            amount_to_goal: int = self.options.amount_of_levels_to_goal
            levels = self.options.get_goal_levels()
            level_count = len(levels)
            if amount_to_goal == 0 or amount_to_goal == level_count:
                self.goal_levels = levels
            elif 0 < amount_to_goal <= len(levels):
                self.goal_levels = self.random.sample(levels, amount_to_goal)
            else:
                amount_to_goal = self.random.randint(1, min(7, level_count))
                self.goal_levels = self.random.sample(levels, amount_to_goal)
            self.goal_level_count = amount_to_goal

    def create_regions(self) -> None:
        option_locations = self.options.get_locations()
        menu_region = Region("Menu", self.player, self.multiworld)
        self.multiworld.regions.append(menu_region)
        option_location_count = len(option_locations)
        percentsanity = self.options.percentsanity

        for location in option_locations:
            location_list: List[str] = []
            next_region = Region(f"Clean the {location}", self.player, self.multiworld)
            self.multiworld.regions.append(next_region)

            if self.options.has_percentsanity():
                for i in range(percentsanity, 100, percentsanity):
                    location_list.append(self.make_location(f"{location} {i}%", next_region).name)

                location_list.append(self.make_location(f"{location} 100%", next_region).name)

            if self.options.has_objectsanity():
                for part in objectsanity_dict[location]:
                    location_list.append(self.make_location(part, next_region).name)

            level_completion_loc = Location(self.player, f"Urge to clean the {location}", None, next_region)
            level_completion_loc.place_locked_item(
                Item(f"Cleaned the {location}", ItemClassification.progression, None, self.player))
            next_region.locations.append(level_completion_loc)

            if location == self.starting_location:
                menu_region.connect(next_region)
            else:
                menu_region.connect(next_region,
                                    rule=lambda state, location_lock=location: state.has(f"{location_lock} Unlock",
                                                                                         self.player))

            next_region.connect(menu_region)
            self.random.shuffle(location_list)
            location_list.pop()
            location_list.pop()
            for loc in location_list:
                self.filler_locations.append(loc)

        self.mcguffin_requirement = max(
            min(math.floor(self.item_steps["total"] * .05), self.item_steps["total"] - option_location_count * 2),
            len(option_locations))

    def create_item(self, name: str) -> PowerwashSimulatorItem:
        return PowerwashSimulatorItem(name, item_table[name], self.item_name_to_id[name], self.player)

    def create_items(self) -> None:
        create_items(self)

    def set_rules(self) -> None:
        if self.options.goal_type == 0:
            self.multiworld.completion_condition[self.player] = lambda state: state.has("A Job Well Done", self.player,
                                                                                        self.mcguffin_requirement)
        else:
            level_requirements = [f"Cleaned the {loc}" for loc in self.goal_levels]
            level_amount_requirements = len(level_requirements)
            self.multiworld.completion_condition[self.player] = lambda state, reqs=level_requirements,amount=level_amount_requirements: len(
                [True for item in reqs if state.has(item, self.player)]) == amount

    def pre_fill(self) -> None:
        location_map: Dict[str, Location] = {loc.name: loc for loc in
                                             self.multiworld.get_unfilled_locations(self.player)}
        for _ in range(self.item_steps["filler"]):
            location_map[self.filler_locations.pop()].place_locked_item(
                self.create_item(self.random.choice(filler_items)))

    def fill_slot_data(self) -> Dict[str, Any]:
        slot_data: Dict[str, Any] = {
            "starting_location": str(self.starting_location),
            "jobs_done": int(self.mcguffin_requirement),
            "objectsanity": bool("Objectsanity" in self.options.sanities),
            "percentsanity": bool("Percentsanity" in self.options.sanities),
            "goal_levels": str(self.goal_levels),
            "goal_level_amount": int(self.goal_level_count)
        }

        return slot_data

    def make_location(self, location_name, region) -> Location:
        location = Location(self.player, location_name, self.location_name_to_id[location_name], region)
        region.locations.append(location)
        return location
