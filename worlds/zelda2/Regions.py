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
        create_region(world, world.player, locations_per_region, "Great Palace"),
    ]

    multiworld.regions += regions
    connect_menu_region(world)

    multiworld.get_region("Northwestern Hyrule", player).add_exits(["Western Hyrule", "Parapa Palace"],
                                                           {"Onett": lambda state: state.has("Onett Teleport", player)})


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
    world.starting_region = "Northwestern Hyrule" # This will change eventually
    world.multiworld.get_region("Menu", world.player).add_exits([world.starting_region, "Northwestern Hyrule"])
    