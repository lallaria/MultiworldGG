from typing import Optional, Dict, Set
from BaseClasses import ItemClassification, Item
from .Strings import AEItem
from .RAMAddress import RAM

base_apeescape_item_id = 128000000


class ApeEscapeItem(Item):
    game: str = "Ape Escape"

GROUPED_ITEMS: Dict[str, Set[str]] = {}

# base IDs are the index in the static item data table, which is
# not the same order as the items in RAM (but offset 0 is a 16-bit address of
# location of room and position data)
item_table = {
    # Gadgets
    AEItem.Club.value: RAM.items["Club"],
    AEItem.Net.value: RAM.items["Net"],
    AEItem.Radar.value: RAM.items["Radar"],
    AEItem.Sling.value: RAM.items["Sling"],
    AEItem.Hoop.value: RAM.items["Hoop"],
    AEItem.Punch.value: RAM.items["Punch"],
    AEItem.Flyer.value: RAM.items["Flyer"],
    AEItem.Car.value: RAM.items["Car"],
    AEItem.WaterNet.value: RAM.items["WaterNet"],
    AEItem.ProgWaterNet.value: RAM.items["ProgWaterNet"],
    AEItem.WaterCatch.value: RAM.items["WaterCatch"],

    # Keys
    AEItem.Key.value: RAM.items["Key"],
    AEItem.Victory.value: RAM.items["Victory"],

    # Monkey Lamps
    AEItem.CB_Lamp.value: RAM.items["CB_Lamp"],
    AEItem.DI_Lamp.value: RAM.items["DI_Lamp"],
    AEItem.CrC_Lamp.value: RAM.items["CrC_Lamp"],
    AEItem.CP_Lamp.value: RAM.items["CP_Lamp"],
    AEItem.SF_Lamp.value: RAM.items["SF_Lamp"],
    AEItem.TVT_Lobby_Lamp.value: RAM.items["TVT_Lobby_Lamp"],
    AEItem.TVT_Tank_Lamp.value: RAM.items["TVT_Tank_Lamp"],
    AEItem.MM_Lamp.value: RAM.items["MM_Lamp"],
    AEItem.MM_DoubleDoorKey.value: RAM.items["MM_DoubleDoorKey"],

    # Other
    AEItem.Token.value: RAM.items["Token"],

    # Junk
    AEItem.Nothing.value: RAM.items["Nothing"],
    AEItem.Shirt.value: RAM.items["Shirt"],
    AEItem.Triangle.value: RAM.items["Triangle"],
    AEItem.BigTriangle.value: RAM.items["BigTriangle"],
    AEItem.BiggerTriangle.value: RAM.items["BiggerTriangle"],
    AEItem.Cookie.value: RAM.items["Cookie"],
    AEItem.FiveCookies.value: RAM.items["FiveCookies"],
    AEItem.Flash.value: RAM.items["Flash"],
    AEItem.ThreeFlash.value: RAM.items["ThreeFlash"],
    AEItem.Rocket.value: RAM.items["Rocket"],
    AEItem.ThreeRocket.value: RAM.items["ThreeRocket"],

    # Traps
    AEItem.BananaPeelTrap.value: RAM.items["BananaPeelTrap"],
    AEItem.GadgetShuffleTrap.value: RAM.items["GadgetShuffleTrap"],
}

gadgetsValues = {
    AEItem.Club.value: 0x00,
    AEItem.Net.value: 0x01,
    AEItem.Radar.value: 0x02,
    AEItem.Sling.value: 0x03,
    AEItem.Hoop.value: 0x04,
    AEItem.Punch.value: 0x05,
    AEItem.Flyer.value: 0x06,
    AEItem.Car.value: 0x07,
}

event_table = {
}

def createItemGroups():
    # Alliases for items
    GROUPED_ITEMS.setdefault("Club", []).append("Stun Club")
    GROUPED_ITEMS.setdefault("Net", []).append("Time Net")
    GROUPED_ITEMS.setdefault("Radar", []).append("Monkey Radar")
    GROUPED_ITEMS.setdefault("Slingshot", []).append("Slingback Shooter")
    GROUPED_ITEMS.setdefault("Sling", []).append("Slingback Shooter")
    GROUPED_ITEMS.setdefault("Hoop", []).append("Super Hoop")
    GROUPED_ITEMS.setdefault("Punch", []).append("Magic Punch")
    GROUPED_ITEMS.setdefault("Flyer", []).append("Sky Flyer")
    GROUPED_ITEMS.setdefault("Car", []).append("R.C. Car")

    # Removed because unit tests said having a group and item named the same is bad
    # GROUPED_ITEMS.setdefault("Water Net", []).append("Progressive Water Net")

    # Item Groups
    GROUPED_ITEMS.setdefault("Gadgets", []).append("Stun Club")
    GROUPED_ITEMS.setdefault("Gadgets", []).append("Time Net")
    GROUPED_ITEMS.setdefault("Gadgets", []).append("Monkey Radar")
    GROUPED_ITEMS.setdefault("Gadgets", []).append("Slingback Shooter")
    GROUPED_ITEMS.setdefault("Gadgets", []).append("Super Hoop")
    GROUPED_ITEMS.setdefault("Gadgets", []).append("Magic Punch")
    GROUPED_ITEMS.setdefault("Gadgets", []).append("Sky Flyer")
    GROUPED_ITEMS.setdefault("Gadgets", []).append("R.C. Car")
    GROUPED_ITEMS.setdefault("Gadgets", []).append("Water Net")
    GROUPED_ITEMS.setdefault("Gadgets", []).append("Progressive Water Net")
    GROUPED_ITEMS.setdefault("Gadgets", []).append("Water Catch")

    GROUPED_ITEMS.setdefault("Lamps", []).append(AEItem.CB_Lamp.value)
    GROUPED_ITEMS.setdefault("Lamps", []).append(AEItem.DI_Lamp.value)
    GROUPED_ITEMS.setdefault("Lamps", []).append(AEItem.CrC_Lamp.value)
    GROUPED_ITEMS.setdefault("Lamps", []).append(AEItem.CP_Lamp.value)
    GROUPED_ITEMS.setdefault("Lamps", []).append(AEItem.SF_Lamp.value)
    GROUPED_ITEMS.setdefault("Lamps", []).append(AEItem.TVT_Lobby_Lamp.value)
    GROUPED_ITEMS.setdefault("Lamps", []).append(AEItem.TVT_Tank_Lamp.value)
    GROUPED_ITEMS.setdefault("Lamps", []).append(AEItem.MM_Lamp.value)

createItemGroups()