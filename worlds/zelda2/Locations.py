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
        LocationData("Northwestern Hyrule", "North Castle Cave", 0x03),
        LocationData("Northwestern Hyrule", "Sage of Rauru", 0x04),
        LocationData("Northwestern Hyrule", "Sage of Ruto", 0x05),
        LocationData("Northwestern Hyrule", "Parapa Coast Item", 0x06),

        LocationData("Parapa Palace", "Parapa Palace: Pedestal Item", 0x07),

        LocationData("Western Hyrule", "Western Swamp Cave", 0x07),

        LocationData("Parapa Palace", "Parapa Palace: Statue", None),
        LocationData("Great Palace", "Dark Link", None)
    ]

    return location_table

static_locations = {
    "Northern Desert Cave": 0x01,
    "Northwestern Forest Item": 0x02,
}