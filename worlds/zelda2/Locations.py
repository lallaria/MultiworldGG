from typing import List, Optional, NamedTuple, TYPE_CHECKING

if TYPE_CHECKING:
    from . import EarthBoundWorld


class LocationData(NamedTuple):
    region: str
    name: str
    code: Optional[int]


def set_locations(world: "Zelda2World") -> List[LocationData]:

    location_table: List[LocationData] = [
        LocationData("Northwest Hyrule", "North Castle Area: Cave", 0x01),

        LocationData("Great Palace", "Dark Link", None)
    ]

static_locations = {
    "North Castle Area: Cave": 0x01
}