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
        LocationData("Parapa Palace", "Parapa Palace: 1F West Hall", 0x07),
        LocationData("Parapa Palace", "Parapa Palace: Pedestal Item", 0x08),
        LocationData("Parapa Palace", "Parapa Palace: Crumbling Bridge", 0x09),
        LocationData("Parapa Palace", "Parapa Palace: Stairwell", 0x0A),
        LocationData("Parapa Palace", "Parapa Palace: Guarded Item", 0x0B),
        LocationData("Parapa Palace", "Parapa Palace: Horsehead Drop", 0x0C),

        LocationData("Western Hyrule", "Western Swamp Cave", 0x0D),
        LocationData("Western Hyrule", "Western Swamp Hidden Item", 0x0E),
        LocationData("Western Hyrule", "Gift from Bagu", 0x0F),
        LocationData("Western Hyrule", "Midoro Swamp Pathway Item", 0x10),
        LocationData("Western Hyrule", "Midoro Swamp Hidden Item", 0x11),
        LocationData("Western Hyrule", "Clear Cave South of Rauru", 0x12),
        LocationData("Western Hyrule", "Blocked Cave South of Rauru", 0x013),
        LocationData("Western Hyrule", "Sage of Saria", 0x14),
        LocationData("Western Hyrule", "Forest Near Saria", 0x15),

        LocationData("Midoro Palace", "Midoro Palace: B2F Hall", 0x16),
        LocationData("Midoro Palace", "Midoro Palace: Lava Blocks Item", 0x17),
        LocationData("Midoro Palace", "Midoro Palace: Floating Block Hall", 0x18),
        LocationData("Midoro Palace", "Midoro Palace: Falling Blocks Item", 0x19),
        LocationData("Midoro Palace", "Midoro Palace: Pedestal Item", 0x1A),
        LocationData("Midoro Palace", "Midoro Palace: Guarded Item", 0x1B),
        LocationData("Midoro Palace", "Midoro Palace: Crumbling Blocks", 0x1C),
        LocationData("Midoro Palace", "Midoro Palace: Helmethead Drop", 0x1D),

        LocationData("Parapa Palace", "Parapa Palace: Statue", None),
        LocationData("Great Palace", "Dark Link", None)
    ]

    return location_table

static_locations = {
    "Northern Desert Cave": 0x01,
    "Northwestern Forest Item": 0x02,
    "North Castle Cave": 0x03,
    "Sage of Rauru": 0x04,
    "Sage of Ruto": 0x05,
    "Parapa Coast Item": 0x06,
    "Parapa Palace - West Hall Key": ?,

}