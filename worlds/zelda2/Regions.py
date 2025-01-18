from typing import List, Dict, TYPE_CHECKING
from BaseClasses import Region, Location
from .Locations import LocationData
if TYPE_CHECKING:
    from . import Z2World


class Z2Location(Location):
    game: str = "Zelda II: The Adventure of Link"

    def __init__(self, player: int, name: str = " ", address: int = None, parent=None):
        super().__init__(player, name, address, parent)


def init_areas(world: "Z2World", locations: List[LocationData]) -> None:
    multiworld = world.multiworld
    player = world.player

    locations_per_region = get_locations_per_region(locations)

    regions = [
        create_region(world, world.player, locations_per_region, "Menu"),
        create_region(world, world.player, locations_per_region, "Northwestern Hyrule"),
        create_region(world, world.player, locations_per_region, "Parapa Palace"),
        create_region(world, world.player, locations_per_region, "Western Hyrule"),
        create_region(world, world.player, locations_per_region, "Midoro Palace"),
        create_region(world, world.player, locations_per_region, "Island Palace"),
        create_region(world, world.player, locations_per_region, "Eastern Hyrule"),
        create_region(world, world.player, locations_per_region, "Northeastern Hyrule"),
        create_region(world, world.player, locations_per_region, "Maze Palace"),
        create_region(world, world.player, locations_per_region, "Palace on the Sea"),
        create_region(world, world.player, locations_per_region, "Southeastern Hyrule"),
        create_region(world, world.player, locations_per_region, "Three-Eye Rock Palace"),
    ]

    multiworld.regions += regions
    connect_menu_region(world)

    multiworld.get_region("Ness's Mind", player).add_exits(["Onett", "Twoson", "Happy-Happy Village", "Threed", "Saturn Valley", "Dusty Dunes Desert", "Fourside", "Winters", "Summers", "Dalaam", "Scaraba", "Deep Darkness", "Tenda Village", "Lost Underworld", "Magicant"],
                                                           {"Onett": lambda state: state.has("Onett Teleport", player),
                                                            "Twoson": lambda state: state.has("Twoson Teleport", player),
                                                            "Happy-Happy Village": lambda state: state.has("Happy-Happy Village Teleport", player),
                                                            "Threed": lambda state: state.has("Threed Teleport", player),
                                                            "Saturn Valley": lambda state: state.has("Saturn Valley Teleport", player),
                                                            "Dusty Dunes Desert": lambda state: state.has("Dusty Dunes Teleport", player),
                                                            "Fourside": lambda state: state.has("Fourside Teleport", player),
                                                            "Winters": lambda state: state.has("Winters Teleport", player),
                                                            "Summers": lambda state: state.has("Summers Teleport", player),
                                                            "Dalaam": lambda state: state.has("Dalaam Teleport", player),
                                                            "Scaraba": lambda state: state.has("Scaraba Teleport", player),
                                                            "Deep Darkness": lambda state: state.has("Deep Darkness Teleport", player),
                                                            "Tenda Village": lambda state: state.has("Tenda Village Teleport", player),
                                                            "Lost Underworld": lambda state: state.has("Lost Underworld Teleport", player),
                                                            "Magicant": lambda state: state.has_any({"Magicant Teleport", "Magicant Unlock"}, player)})
    multiworld.get_region("Northern Onett", player).add_exits(["Onett"])


def create_location(player: int, location_data: LocationData, region: Region) -> Location:
    location = Z2Location(player, location_data.name, location_data.code, region)
    location.region = location_data.region

    return location


def create_region(world: "Z2World", player: int, locations_per_region: Dict[str, List[LocationData]], name: str) -> Region:
    region = Region(name, player, world.multiworld)

    if name in locations_per_region:
        for location_data in locations_per_region[name]:
            location = create_location(player, location_data, region)
            region.locations.append(location)

    return region


def get_locations_per_region(locations: List[LocationData]) -> Dict[str, List[LocationData]]:
    per_region: Dict[str, List[LocationData]] = {}

    for location in locations:
        per_region.setdefault(location.region, []).append(location)

    return per_region


def connect_menu_region(world: "EarthBoundWorld") -> None:
    starting_region_list = {
        0: "Northern Onett",
        1: "Onett",
        2: "Twoson",
        3: "Happy-Happy Village",
        4: "Threed",
        5: "Saturn Valley",
        6: "Fourside",
        7: "Winters",
        8: "Summers",
        9: "Dalaam",
        10: "Scaraba",
        11: "Deep Darkness",
        12: "Tenda Village",
        13: "Lost Underworld",
        14: "Magicant"
    }
    #todo; change the coordinate dict to use names instead of numbers, change start_location instead of making a new var
    world.starting_region = starting_region_list[world.start_location]
    world.multiworld.get_region("Menu", world.player).add_exits([world.starting_region, "Ness's Mind"],
                                {"Ness's Mind": lambda state: state.has_any({"Ness", "Paula", "Jeff", "Poo"}, world.player),
                                world.starting_region: lambda state: state.has_any({"Ness", "Paula", "Jeff", "Poo"}, world.player)})
    