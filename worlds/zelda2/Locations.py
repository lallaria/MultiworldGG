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

        LocationData("Death Mountain", "Death Mountain Platforms", 0x1D),
        LocationData("Death Mountain", "Death Mountain Staircase", 0x1E),
        LocationData("Death Mountain", "Death Mountain Boulder Pit", 0x1F),
        LocationData("Death Mountain", "Death Mountain Ending Item", 0x20),
        LocationData("Death Mountain", "Death Mountain East-Facing Dead End", 0x21),

        LocationData("Western Coast", "Graveyard Item", 0x22),
        LocationData("Western Coast", "Graveyard Beach Secret", 0x23),
        LocationData("Western Coast", "Sage of Mido", 0x24),
        LocationData("Western Coast", "Mido Swordsman", 0x25),

        LocationData("Island Palace", "Island Palace: Buried Item Left", 0x26),
        LocationData("Island Palace", "Island Palace: Buried Item Right", 0x27),
        LocationData("Island Palace", "Island Palace: Outside", 0x28),
        LocationData("Island Palace", "Island Palace: Buried Item", 0x29),
        LocationData("Island Palace", "Island Palace: Precarious Item", 0x2A),
        LocationData("Island Palace", "Island Palace: Pedestal Item", 0x2B),
        LocationData("Island Palace", "Island Palace: Enclosed Item", 0x2C),
        LocationData("Island Palace", "Island Palace: Pillar Item", 0x2D),
        LocationData("Island Palace", "Island Palace: Guarded by Iron Knuckles", 0x2E),
        LocationData("Island Palace", "Island Palace: Rebonack Drop", 0x2F),

        LocationData("Eastern Hyrule", "Eastern Forest", 0x30),
        LocationData("Eastern Hyrule", "Sage of Nabooru", 0x31),
        LocationData("Eastern Hyrule", "Eastern Cave", 0x32),
        LocationData("Eastern Hyrule", "Eastern Peninsula Secret", 0x33),
        LocationData("Eastern Hyrule", "Eastern Beach Secret", 0x34),
        LocationData("Eastern Hyrule", "Ocean Item", 0x35),

        LocationData("Northeastern Hyrule", "Sage of Darunia", 0x36),
        LocationData("Northeastern Hyrule", "Darunia Swordsman", 0x37),
        LocationData("Northeastern Hyrule", "Northeastern Beach", 0x38),
        LocationData("Northeastern Hyrule", "Maze Island Left Hole", 0x39),
        LocationData("Northeastern Hyrule", "Maze Island Path", 0x3A),
        LocationData("Northeastern Hyrule", "Maze Island Right Hole", 0x3B),

        LocationData("Maze Palace", "Maze Palace: Nook Item", 0x3B),
        LocationData("Maze Palace", "Maze Palace: Sealed Item", 0x3B),
        LocationData("Maze Palace", "Maze Palace: Block Mountain Left", 0x3B),
        LocationData("Maze Palace", "Maze Palace: Block Mountain Right", 0x3B),
        LocationData("Maze Palace", "Maze Palace: West Hall of Fire", 0x3B),
        LocationData("Maze Palace", "Maze Palace: East Hall of Fire", 0x3B),
        LocationData("Maze Palace", "Maze Palace: Basement Hall of Fire", 0x3B),
        LocationData("Maze Palace", "Maze Palace: Block Mountain Basement", 0x3B),
        LocationData("Maze Palace", "Maze Palace: Pillar Item", 0x3B),
        LocationData("Maze Palace", "Maze Palace: Pedestal Item", 0x3B),
        LocationData("Maze Palace", "Maze Palace: Rebonack Drop", 0x3B),

        LocationData("Palace on the Sea", "Palace on the Sea: Ledge Item", 0x34),
        LocationData("Palace on the Sea", "Palace on the Sea: Crumbling Bridge", 0x34),
        LocationData("Palace on the Sea", "Palace on the Sea: Falling Blocks", 0x34),
        LocationData("Palace on the Sea", "Palace on the Sea: Above Elevator", 0x34),
        LocationData("Palace on the Sea", "Palace on the Sea: Block Alcove", 0x34),
        LocationData("Palace on the Sea", "Palace on the Sea: Knuckle Alcove", 0x34),
        LocationData("Palace on the Sea", "Palace on the Sea: Pedestal Item", 0x34),
        LocationData("Palace on the Sea", "Palace on the Sea: Skeleton Key", 0x34),
        LocationData("Palace on the Sea", "Palace on the Sea: West Wing", 0x34),
        LocationData("Palace on the Sea", "Palace on the Sea: Block Line", 0x34),
        LocationData("Palace on the Sea", "Palace on the Sea: West Knuckle Alcove", 0x34),
        LocationData("Palace on the Sea", "Palace on the Sea: Gooma Drop", 0x34),

        LocationData("Parapa Palace", "Parapa Palace: Statue", None),
        LocationData("Midoro Palace", "Midoro Palace: Statue", None),
        LocationData("Island Palace", "Island Palace: Statue", None),
        LocationData("Maze Palace", "Maze Palace: Statue", None),
        LocationData("Palace on the Sea", "Palace on the Sea: Statue", None),
        LocationData("Three-Eye Rock Palace", "Three-Eye Rock Palace: Statue", None),
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