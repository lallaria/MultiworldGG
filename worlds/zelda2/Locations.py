from typing import List, Optional, NamedTuple, TYPE_CHECKING

if TYPE_CHECKING:
    from . import EarthBoundWorld


class LocationData(NamedTuple):
    region: str
    name: str
    code: Optional[int]


def get_locations(world: "Zelda2World") -> List[LocationData]:

    location_table: List[LocationData] = [
        LocationData("Northwestern Hyrule", "Northern Desert Cave", 0x01),
        LocationData("Northwestern Hyrule", "Northwestern Forest Item", 0x02),

        LocationData("Great Palace", "Dark Link", None)
    ]
    
    return location_table

static_locations = {
    "Northern Desert Cave": 0x01,
    "Northwestern Forest Item": 0x02,
}