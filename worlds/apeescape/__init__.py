import math
import os
import json
from typing import ClassVar, Dict, List, Tuple, Optional, TextIO

from BaseClasses import ItemClassification, MultiWorld, Tutorial, CollectionState
from logging import warning
from Options import OptionError
from worlds.AutoWorld import WebWorld, World

from .Items import item_table, ApeEscapeItem, GROUPED_ITEMS
from .Locations import location_table, base_location_id, GROUPED_LOCATIONS
from .Regions import create_regions, ApeEscapeLevel
from .Rules import set_rules, get_required_keys
from .Client import ApeEscapeClient
from .Strings import AEItem, AELocation
from .RAMAddress import RAM
from .Options import ApeEscapeOptions


class ApeEscapeWeb(WebWorld):
    theme = "stone"

    # Verify this placeholder text is accurate
    setup_en = Tutorial(
        "Ape Escape Multiworld Setup Guide",
        "A guide to setting up Ape Escape in MultiworldGG.",
        "English",
        "setup_en.md",
        "setup/en",
        ["CDRomatron, Thedragon005, IHNN"]
    )
    setup_fr = Tutorial(
        setup_en.tutorial_name,
        setup_en.description,
        "Français",
        "setup_fr.md",
        "setup/fr",
        ["Thedragon005"]
    )

    tutorials = [setup_en, setup_fr]


class ApeEscapeWorld(World):
    """
    Ape Escape is a platform game published and developed by Sony for the PlayStation, released in 1999.
    The story revolves around the main protagonist, Spike, who has to prevent history from being changed
    by an army of monkeys led by Specter, the main antagonist.
    """
    game = "Ape Escape"
    author: str = "Thedragon005"
    web: ClassVar[WebWorld] = ApeEscapeWeb()
    topology_present = True

    options_dataclass = ApeEscapeOptions
    options: ApeEscapeOptions

    item_name_to_id = item_table

    for key, value in item_name_to_id.items():
        item_name_to_id[key] = value + base_location_id

    location_name_to_id = location_table

    for key, value in location_name_to_id.items():
        location_name_to_id[key] = value + base_location_id

    item_name_groups = GROUPED_ITEMS
    location_name_groups = GROUPED_LOCATIONS


    def __init__(self, multiworld: MultiWorld, player: int):
        self.goal: Optional[int] = 0
        self.requiredtokens: Optional[int] = 0
        self.totaltokens: Optional[int] = 0
        self.tokenlocations: Optional[int] = 0
        self.logic: Optional[int] = 0
        self.infinitejump: Optional[int] = 0
        self.superflyer: Optional[int] = 0
        self.entrance: Optional[int] = 0
        self.unlocksperkey: Optional[int] = 0
        self.extrakeys: Optional[int] = 0
        self.coin: Optional[int] = 0
        self.mailbox: Optional[int] = 0
        self.lamp: Optional[int] = 0
        self.gadget: Optional[int] = 0
        self.shufflenet: Optional[int] = 0
        self.shufflewaternet: Optional[int] = 0
        self.lowoxygensounds: Optional[int] = 0
        self.trapfillpercentage: Optional[int] = 0
        self.itemdisplay: Optional[int] = 0
        self.itempool: List[ApeEscapeItem] = []
        self.levellist: List[ApeEscapeLevel] = []
        self.entranceorder: List[ApeEscapeLevel] = []

        super(ApeEscapeWorld, self).__init__(multiworld, player)


    def generate_early(self) -> None:
        self.goal = self.options.goal.value
        self.requiredtokens = self.options.requiredtokens.value
        self.totaltokens = self.options.totaltokens.value
        self.tokenlocations = self.options.tokenlocations.value
        self.logic = self.options.logic.value
        self.infinitejump = self.options.infinitejump.value
        self.superflyer = self.options.superflyer.value
        self.entrance = self.options.entrance.value
        self.unlocksperkey = self.options.unlocksperkey.value
        self.extrakeys = self.options.extrakeys.value
        self.coin = self.options.coin.value
        self.mailbox = self.options.mailbox.value
        self.lamp = self.options.lamp.value
        self.gadget = self.options.gadget.value
        self.shufflenet = self.options.shufflenet.value
        self.shufflewaternet = self.options.shufflewaternet.value
        self.lowoxygensounds = self.options.lowoxygensounds.value
        self.trapfillpercentage = self.options.trapfillpercentage.value
        self.itemdisplay = self.options.itemdisplay.value
        self.itempool = []


    def create_regions(self):
        create_regions(self)


    def set_rules(self):
        set_rules(self)


    def create_item(self, name: str) -> ApeEscapeItem:
        item_id = item_table[name]
        classification = ItemClassification.progression

        item = ApeEscapeItem(name, classification, item_id, self.player)
        return item


    def create_item_skipbalancing(self, name: str) -> ApeEscapeItem:
        item_id = item_table[name]
        classification = ItemClassification.progression_skip_balancing

        item = ApeEscapeItem(name, classification, item_id, self.player)
        return item


    def create_item_useful(self, name: str) -> ApeEscapeItem:
        item_id = item_table[name]
        classification = ItemClassification.useful

        item = ApeEscapeItem(name, classification, item_id, self.player)
        return item


    def create_item_filler(self, name: str) -> ApeEscapeItem:
        item_id = item_table[name]
        classification = ItemClassification.filler

        item = ApeEscapeItem(name, classification, item_id, self.player)
        return item


    def create_item_trap(self, name: str) -> ApeEscapeItem:
        item_id = item_table[name]
        classification = ItemClassification.trap

        item = ApeEscapeItem(name, classification, item_id, self.player)
        return item


    def create_items(self):
        reservedlocations = 0

        club = self.create_item(AEItem.Club.value)
        net = self.create_item(AEItem.Net.value)
        radar = self.create_item(AEItem.Radar.value)
        shooter = self.create_item(AEItem.Sling.value)
        hoop = self.create_item(AEItem.Hoop.value)
        flyer = self.create_item(AEItem.Flyer.value)
        car = self.create_item(AEItem.Car.value)
        punch = self.create_item(AEItem.Punch.value)
        victory = self.create_item(AEItem.Victory.value)

        waternet = self.create_item(AEItem.WaterNet.value)
        # progwaternet = self.create_item(AEItem.ProgWaterNet.value)
        watercatch = self.create_item(AEItem.WaterCatch.value)

        CB_Lamp = self.create_item(AEItem.CB_Lamp.value)
        DI_Lamp = self.create_item(AEItem.DI_Lamp.value)
        CrC_Lamp = self.create_item(AEItem.CrC_Lamp.value)
        CP_Lamp = self.create_item(AEItem.CP_Lamp.value)
        SF_Lamp = self.create_item(AEItem.SF_Lamp.value)
        TVT_Lobby_Lamp = self.create_item(AEItem.TVT_Lobby_Lamp.value)
        TVT_Tank_Lamp = self.create_item(AEItem.TVT_Tank_Lamp.value)
        MM_Lamp = self.create_item(AEItem.MM_Lamp.value)
        MM_DoubleDoorKey = self.create_item(AEItem.MM_DoubleDoorKey.value)

        self.itempool += [MM_DoubleDoorKey]

        # Create the desired amount of Specter Tokens if the settings require them, and make them local if requested.
        if self.options.goal == "tokenhunt" or self.options.goal == "mmtoken" or self.options.goal == "ppmtoken":
            self.itempool += [self.create_item_skipbalancing(AEItem.Token.value) for _ in range(0, max(self.options.requiredtokens, self.options.totaltokens))]
            if self.options.tokenlocations == "ownworld":
                self.options.local_items.value.add("Specter Token")

        # Create enough keys to access every level, if keys are on, plus the desired amount of extra keys.
        if self.options.unlocksperkey != "none":
            numkeys = get_required_keys(self.options.unlocksperkey.value, self.options.goal.value, self.options.coin.value)
            self.itempool += [self.create_item(AEItem.Key.value) for _ in range(0, numkeys[21] + self.options.extrakeys.value)]

        # Monkey Lamp shuffle - only add to the pool if the option is on (treat as vanilla otherwise)
        if self.options.lamp == "true":
            self.itempool += [CB_Lamp]
            self.itempool += [DI_Lamp]
            self.itempool += [CrC_Lamp]
            self.itempool += [CP_Lamp]
            self.itempool += [SF_Lamp]
            self.itempool += [TVT_Lobby_Lamp]
            self.itempool += [TVT_Tank_Lamp]
            self.itempool += [MM_Lamp]

        # Water Net shuffle handling
        if self.options.shufflewaternet == 0x00 or self.options.gadget == 0x07:  # Off or Starting Gadget
            self.multiworld.push_precollected(waternet)
        elif self.options.shufflewaternet == 0x01:  # Progressive
            self.itempool += [watercatch]
            self.itempool += [self.create_item(AEItem.ProgWaterNet.value)]
            self.itempool += [self.create_item(AEItem.ProgWaterNet.value)]
        else:  # On
            self.itempool += [waternet]

        # Net shuffle handling
        if self.options.shufflenet == "false":
            self.multiworld.push_precollected(net)
        elif self.options.shufflenet == "true":
            # If net shuffle is on, make sure there are locations that don't require net.
            if self.options.coin == "true" or self.options.mailbox == "true":
                self.itempool += [net]
            else:
                # All locations require net with these options, so throw a warning about incompatible options and just give the net anyway.
                # if instead we want to error out and prevent generation, uncomment this line:
                # raise OptionError(f"{self.player_name} has no sphere 1 locations!")
                warning(
                    f"Warning: selected options for {self.player_name} have no sphere 1 locations. Giving Time Net.")
                self.multiworld.push_precollected(net)

        if self.options.gadget == "club":
            self.multiworld.push_precollected(club)
            self.itempool += [radar, shooter, hoop, flyer, car, punch]
        elif self.options.gadget == "radar":
            self.multiworld.push_precollected(radar)
            self.itempool += [club, shooter, hoop, flyer, car, punch]
        elif self.options.gadget == "sling":
            self.multiworld.push_precollected(shooter)
            self.itempool += [club, radar, hoop, flyer, car, punch]
        elif self.options.gadget == "hoop":
            self.multiworld.push_precollected(hoop)
            self.itempool += [club, radar, shooter, flyer, car, punch]
        elif self.options.gadget == "flyer":
            self.multiworld.push_precollected(flyer)
            self.itempool += [club, radar, shooter, hoop, car, punch]
        elif self.options.gadget == "car":
            self.multiworld.push_precollected(car)
            self.itempool += [club, radar, shooter, hoop, flyer, punch]
        elif self.options.gadget == "punch":
            self.multiworld.push_precollected(punch)
            self.itempool += [club, radar, shooter, hoop, flyer, car]
        elif self.options.gadget == "none" or self.options.gadget == "waternet":
            self.itempool += [club, radar, shooter, hoop, flyer, car, punch]

        # Create "Victory" item for goals where the goal is at a location.
        if self.options.goal == "mm" or self.options.goal == "mmtoken":
            self.get_location(AELocation.Specter.value).place_locked_item(victory)
        elif self.options.goal == "ppm" or self.options.goal == "ppmtoken":
            self.get_location(AELocation.Specter2.value).place_locked_item(victory)

        # This is where creating items for increasing special pellet maximums would go.

        # Trap item fill: randomly pick items according to a set of weights.
        # Trap weights: Banana Peel, Gadget Shuffle
        if self.options.trapfillpercentage != 0:
            trap_weights = [75, 25]
            trap_percentage = self.options.trapfillpercentage / 100
            trap_count = round((len(self.multiworld.get_unfilled_locations(self.player)) - len(self.itempool) - reservedlocations) * trap_percentage, None)

            for x in range(1, len(trap_weights)):
                trap_weights[x] = trap_weights[x] + trap_weights[x - 1]

            for _ in range(trap_count):
                randomTrap = self.random.randint(1, trap_weights[len(trap_weights) - 1])
                if 0 < randomTrap <= trap_weights[0]:
                    self.itempool += [self.create_item_trap(AEItem.BananaPeelTrap.value)]
                else:
                    self.itempool += [self.create_item_trap(AEItem.BananaPeelTrap.value)]
                    # Deactivated for now
                    # self.itempool += [self.create_item_trap(AEItem.GadgetShuffleTrap.value)]

            # print("Created " + str(trap_count) + " traps.")

        # Junk item fill: randomly pick items according to a set of weights.
        # Filler item weights are for 1 Jacket, 1/5 Cookies, 1/5/25 Energy Chips, 1/3 Explosive/Guided Pellets and Nothing, respectively.
        # TODO: expose these weights as a YAML option.
        weights = [7, 16, 3, 31, 14, 4, 9, 3, 9, 3, 0]

        for x in range(1, len(weights)):
            weights[x] = weights[x] + weights[x - 1]
        filler_count = len(self.multiworld.get_unfilled_locations(self.player)) - len(self.itempool) - reservedlocations
        for _ in range(filler_count):
            randomFiller = self.random.randint(1, weights[len(weights) - 1])
            if 0 < randomFiller <= weights[0]:
                self.itempool += [self.create_item_useful(AEItem.Shirt.value)]
            elif weights[0] < randomFiller <= weights[1]:
                self.itempool += [self.create_item_filler(AEItem.Cookie.value)]
            elif weights[1] < randomFiller <= weights[2]:
                self.itempool += [self.create_item_filler(AEItem.FiveCookies.value)]
            elif weights[2] < randomFiller <= weights[3]:
                self.itempool += [self.create_item_filler(AEItem.Triangle.value)]
            elif weights[3] < randomFiller <= weights[4]:
                self.itempool += [self.create_item_filler(AEItem.BigTriangle.value)]
            elif weights[4] < randomFiller <= weights[5]:
                self.itempool += [self.create_item_filler(AEItem.BiggerTriangle.value)]
            elif weights[5] < randomFiller <= weights[6]:
                self.itempool += [self.create_item_useful(AEItem.Flash.value)]
            elif weights[6] < randomFiller <= weights[7]:
                self.itempool += [self.create_item_useful(AEItem.ThreeFlash.value)]
            elif weights[7] < randomFiller <= weights[8]:
                self.itempool += [self.create_item_useful(AEItem.Rocket.value)]
            elif weights[8] < randomFiller <= weights[9]:
                self.itempool += [self.create_item_useful(AEItem.ThreeRocket.value)]
            else:
                self.itempool += [self.create_item_filler(AEItem.Nothing.value)]
        # print("Created " + str(filler_count) + " filler items.")

        self.multiworld.itempool += self.itempool


    def fill_slot_data(self):
        bytestowrite = []
        entranceids = []
        newpositions = []
        firstroomids = [0x01, 0x02, 0x03, 0x06, 0x0B, 0x0F, 0x13, 0x14, 0x16, 0x18, 0x1D, 0x1E, 0x21, 0x24, 0x25, 0x28,
                        0x2D, 0x35, 0x38, 0x3F, 0x45, 0x57]
        orderedfirstroomids = []
        for x in range(0, 22):
            newpositions.append(self.levellist[x].newpos)
            entranceids.append(self.entranceorder[x].entrance)
            orderedfirstroomids.append(firstroomids[self.entranceorder[x].vanillapos])
            bytestowrite += self.entranceorder[x].bytes
            bytestowrite.append(0)  # We need a separator byte after each level name.

        return {
            "goal": self.options.goal.value,
            "requiredtokens": self.options.requiredtokens.value,
            "totaltokens": self.options.totaltokens.value,
            "tokenlocations": self.options.tokenlocations.value,
            "logic": self.options.logic.value,
            "infinitejump": self.options.infinitejump.value,
            "superflyer": self.options.superflyer.value,
            "entrance": self.options.entrance.value,
            "unlocksperkey": self.options.unlocksperkey.value,
            "extrakeys": self.options.extrakeys.value,
            "coin": self.options.coin.value,
            "mailbox": self.options.mailbox.value,
            "lamp": self.options.lamp.value,
            "gadget": self.options.gadget.value,
            "shufflenet": self.options.shufflenet.value,
            "shufflewaternet": self.options.shufflewaternet.value,
            "lowoxygensounds": self.options.lowoxygensounds.value,
            "trapfillpercentage": self.options.trapfillpercentage.value,
            "itemdisplay": self.options.itemdisplay.value,
            "kickoutprevention": self.options.kickoutprevention.value,
            "autoequip": self.options.autoequip.value,
            "levelnames": bytestowrite,  # List of level names in entrance order. FF leads to the first.
            "entranceids": entranceids,  # Not used by the client. List of level ids in entrance order.
            "newpositions": newpositions,  # List of positions a level is moved to. The position of FF is first.
            "firstrooms": orderedfirstroomids,  # List of first rooms in entrance order.
            "reqkeys": get_required_keys(self.options.unlocksperkey.value, self.options.goal.value, self.options.coin.value),
            "death_link": self.options.death_link.value
        }


    def write_spoiler(self, spoiler_handle: TextIO):
        if self.options.entrance.value != 0x00:
            spoiler_handle.write(
                f"\n\nApe Escape entrance connections for {self.multiworld.get_player_name(self.player)}:")
            for x in range(0, 22):
                spoiler_handle.write(f"\n  {self.levellist[x].name} ==> {self.entranceorder[x].name}")
            spoiler_handle.write(f"\n")


    def generate_output(self, output_directory: str):
        data = {
            "slot_data": self.fill_slot_data()
        }
        # Remove .apae output because it does nothing, we do everything in RAM
        # filename = f"{self.multiworld.get_out_file_name_base(self.player)}.apae"
        # with open(os.path.join(output_directory, filename), 'w') as f:
        #     json.dump(data, f)
