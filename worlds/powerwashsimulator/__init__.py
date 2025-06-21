import math
from typing import Dict, Any, Union, ClassVar, List
from worlds.AutoWorld import World, WebWorld
from BaseClasses import Location, Region, LocationProgressType, Tutorial
from .Items import raw_items, PowerwashSimulatorItem, item_table, create_items, unlock_items
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
    location_counter: int = 0
    mcguffin_requirement = 0
    item_name_groups = {
        "unlocks": unlock_items
    }

    def generate_early(self) -> None:
        check_options(self)

        option_locations = self.options.get_locations()
        if self.options.start_with_van and "Van" in option_locations: return
        self.starting_location = self.random.choice(option_locations)

    def create_regions(self) -> None:
        option_locations = self.options.get_locations()
        menu_region = Region("Menu", self.player, self.multiworld)
        self.multiworld.regions.append(menu_region)
        percentsanity = self.options.percentsanity.value

        option_location_count = len(option_locations)
        percentsanity_location_count = (len(range(percentsanity, 100, percentsanity)) + 1) * option_location_count
        objectsanity_location_count = sum(len(objectsanity_dict[loc]) for loc in option_locations)
        self.location_counter = (percentsanity_location_count if self.options.has_percentsanity() else 0) + (
            objectsanity_location_count if self.options.has_objectsanity() else 0)

        important_item_count = option_location_count * 2 - 1
        added_mcguffin = math.floor((self.location_counter - important_item_count) * .075)
        important_item_count += added_mcguffin
        remaining_location_count = self.location_counter - important_item_count
        location_list: List[Location] = []

        if self.options.has_percentsanity() and self.options.has_objectsanity():
            remaining_location_count *= .97
        elif "Objectsanity" in self.options.sanities:
            remaining_location_count *= .6
        else:
            remaining_location_count *= .5


        theoretical_locations = 0

        for location in option_locations:
            next_region = Region(f"Clean the {location}", self.player, self.multiworld)
            self.multiworld.regions.append(next_region)

            if self.options.has_percentsanity():
                for i in range(percentsanity, 100, percentsanity):
                    percent_location = f"{location} {i}%"
                    percentsanity_location = Location(self.player, percent_location,
                                                      self.location_name_to_id[percent_location], next_region)
                    next_region.locations.append(percentsanity_location)
                    location_list.append(percentsanity_location)
                    theoretical_locations += 1

                percent_location = f"{location} 100%"
                percentsanity_location = Location(self.player, percent_location,
                                                  self.location_name_to_id[percent_location], next_region)
                next_region.locations.append(percentsanity_location)
                location_list.append(percentsanity_location)
                theoretical_locations += 1

            if self.options.has_objectsanity():
                for part in objectsanity_dict[location]:
                    objectsanity_location = Location(self.player, part, self.location_name_to_id[part], next_region)
                    next_region.locations.append(objectsanity_location)
                    location_list.append(objectsanity_location)
                    theoretical_locations += 1

            if location == self.starting_location:
                menu_region.connect(next_region)
            else:
                menu_region.connect(next_region,
                                    rule=lambda state, location_lock=location: state.has(f"{location_lock} Unlock",
                                                                                         self.player))
            next_region.connect(menu_region)

        self.multiworld.random.shuffle(location_list)

        for i in range(math.floor(remaining_location_count)):
            location_list[i].progress_type = LocationProgressType.EXCLUDED

        self.mcguffin_requirement = max(
            min(math.floor(self.location_counter * .05), self.location_counter - option_location_count * 2),
            len(option_locations))

        # print(f"total: [{self.location_counter}], real: [{theoretical_locations}], remain: [{remaining_location_count}], mcguffin: [{option_location_count + added_mcguffin}]/[{self.mcguffin_requirement}]")

    def create_item(self, name: str) -> PowerwashSimulatorItem:
        return PowerwashSimulatorItem(name, item_table[name], self.item_name_to_id[name], self.player)

    def create_items(self) -> None:
        create_items(self)

    def set_rules(self) -> None:
        self.multiworld.completion_condition[self.player] = lambda state: state.has("A Job Well Done", self.player, self.mcguffin_requirement)

    def fill_slot_data(self) -> Dict[str, Any]:
        slot_data: Dict[str, Any] = {
            "starting_location": str(self.starting_location),
            "jobs_done": int(self.mcguffin_requirement),
            "objectsanity": bool("Objectsanity" in self.options.sanities),
            "percentsanity": bool("Percentsanity" in self.options.sanities),
        }

        return slot_data
