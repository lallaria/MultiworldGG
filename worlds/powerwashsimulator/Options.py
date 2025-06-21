import logging
from typing import List, Union
from dataclasses import dataclass
from Options import Range, Toggle, PerGameCommonOptions, OptionSet, OptionError
from .Locations import land_vehicles, water_vehicles, air_vehicles, places, bonus_jobs, midgar, tomb_raider
from settings import Group, Bool


class StartWithVan(Toggle):
    """
    Start with Van as the random starting level
    """
    display_name = "Start With Van"


class LandVehicleLocations(OptionSet):
    """
    Locations:
    ["Van", "Vintage Car", "Grandpa Miller's Car", "Fire Truck", "Dirt Bike", "Golf Cart", "Motorbike and Sidecar", "SUV", "Penny Farthing", "Recreation Vehicle", "Drill", "Monster Truck"]
    "All" - adds all locations above
    """
    display_name = "Land Vehicle Locations"
    valid_keys = frozenset(land_vehicles + ["All"])
    default = "All"


class WaterVehicleLocations(OptionSet):
    """
    Locations:
    ["Frolic Boat", "Fishing Boat"]
    "All" - adds all locations above
    """
    display_name = "Water Vehicle Locations"
    valid_keys = frozenset(water_vehicles + ["All"])
    default = "All"


class AirVehicleLocations(OptionSet):
    """
    Locations:
    ["Fire Helicopter", "Private Jet", "Stunt Plane", "Recreational Vehicle (Again)"]
    "All" - adds all locations above
    """
    display_name = "Air Vehicle Locations"
    valid_keys = frozenset(air_vehicles + ["All"])
    default = "All"


class PlaceLocations(OptionSet):
    """
    Locations:
    ["Back Garden", "Bungalow", "Playground", "Detached House", "Shoe House", "Fire Station", "Skatepark", "Forest Cottage", "Mayor's Mansion", "Carousel", "Tree House", "Temple", "Washroom", "Helter Skelter", "Ferris Wheel", "Subway Platform", "Fortune Teller's Wagon", "Ancient Statue", "Ancient Monument", "Lost City Palace"]
    "All" - adds all locations above
    """
    display_name = "Place Locations"
    valid_keys = frozenset(places + ["All"])
    default = "All"


class BonusJobLocations(OptionSet):
    """
    Locations:
    ["Mars Rover", "Gnome Fountain", "Mini Golf Course", "Steam Locomotive", "Food Truck", "Satellite Dish", "Solar Station", "Paintball Arena", "Spanish Villa", "Excavator", "Aquarium", "Submarine", "Modern Mansion", "Fire Plane", "Dessert Parlor", "Subway Train", "Sculpture Park"]
    "All" - adds all locations above
    """
    display_name = "Bonus Job Locations"
    valid_keys = frozenset(bonus_jobs + ["All"])


class MidgarLocations(OptionSet):
    """
    Locations:
    ["Scorpion Sentinel", "Hardy-Daytona & Shinra Hauler", "Seventh Heaven", "Mako Energy Exhibit", "Airbuster"]
    "All" - adds all locations above
    """
    display_name = "Midgar Locations"
    valid_keys = frozenset(midgar + ["All"])


class TombRaiderLocations(OptionSet):
    """
    Locations:
    ["Croft Manor", "Lara Croft's Obstacle Course and Quad Bike", "Lara Croft's Jeep and Motorboat", "Croft Manor's Maze", "Croft Manor's Treasure Room"]
    "All" - adds all locations above
    """
    display_name = "Tomb Raider Locations"
    valid_keys = frozenset(tomb_raider + ["All"])


class Sanities(OptionSet):
    """
    Which sanities should be enabled?

    Percentsanity: every % total cleaned of a level is a check
    Objectsanity: each part of a cleanable object is a check
    """
    display_name = "Sanities"
    valid_keys = frozenset(["Percentsanity", "Objectsanity"])
    default = "Percentsanity"


class Percentsanity(Range):
    """
    What intervals of cleaned % to have checks at

    default 20: checks at 20%, 40%, 60%, 80%, and 100%
    host yaml setting `allow_percentsanity_below_7` (off by default) will allow % below 7%
    """
    default = 20
    range_end = 20
    range_start = 1


@dataclass
class PowerwashSimulatorOptions(PerGameCommonOptions):
    start_with_van: StartWithVan
    land_vehicles: LandVehicleLocations
    water_vehicles: WaterVehicleLocations
    air_vehicles: AirVehicleLocations
    places: PlaceLocations
    bonus_jobs: BonusJobLocations
    midgar: MidgarLocations
    tomb_raider: TombRaiderLocations
    sanities: Sanities
    percentsanity: Percentsanity

    def get_locations(self) -> List[str]:
        locations = (self.flatten_locations(land_vehicles, self.land_vehicles)
                     + self.flatten_locations(water_vehicles, self.water_vehicles)
                     + self.flatten_locations(air_vehicles, self.air_vehicles)
                     + self.flatten_locations(places, self.places)
                     + self.flatten_locations(bonus_jobs, self.bonus_jobs)
                     + self.flatten_locations(midgar, self.midgar)
                     + self.flatten_locations(tomb_raider, self.tomb_raider))

        if self.start_with_van and "Van" not in locations:
            locations.append("Van")

        return locations

    def has_percentsanity(self):
        return "Percentsanity" in self.sanities

    def has_objectsanity(self):
        return "Objectsanity" in self.sanities

    def flatten_locations(self, list, self_list) -> List[str]:
        return list if "All" in self_list else [loc for loc in self_list]


class PowerwashSimulatorSettings(Group):
    class AllowPercentsanityBelow7(Bool):
        """Allow players to have the Percentsanity setting to be below 7%"""

    class AllowObjectsanity(Bool):
        """Allow players to enable Objectsanity"""

    allow_percentsanity_below_7: Union[AllowPercentsanityBelow7, bool] = False
    allow_objectsanity: Union[AllowObjectsanity, bool] = False


def check_options(world):
    options: PowerwashSimulatorOptions = world.options
    settings: PowerwashSimulatorSettings = world.settings

    if options.percentsanity < 7 and not settings.allow_percentsanity_below_7:
        logging.info(
            f"Powerwash Simulator: {world.player_name} has {options.percentsanity} < 7 for percentsanity. since the host has allow_percentsanity_below_7 {settings.allow_percentsanity_below_7} percentsanity will be set to 7")
        options.percentsanity = Percentsanity(7)

    if options.has_objectsanity() and not settings.allow_objectsanity:
        RaiseYamlError(world.player_name,
                       "Objectsanity can not be enabled unless the host setting 'allow_objectsanity' is also enabled")

    if not options.has_objectsanity() and not options.has_percentsanity():
        RaiseYamlError(world.player_name, "No sanities are listed, you must have one either: `Percentsanity` or `Objectsanity`")

    if len(options.get_locations()) > 0: return
    RaiseYamlError(world.player_name, "Does not have locations listed in their yaml")


def RaiseYamlError(player_name, error):
    raise OptionError(
        f"\n\n=== Powerwash Simulator YAML ERROR ===\nPowerwash Simulator: {player_name} {error}, PLEASE FIX YOUR YAML\n\n")
