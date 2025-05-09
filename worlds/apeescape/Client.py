import sys
import logging
import time
from random import random
from tokenize import endpats

from win32comext.shell.shell import BHID_DataObject

import Utils
from typing import TYPE_CHECKING, Optional, Dict, Set, ClassVar, Any, Tuple

from MultiServer import team_slot
from Options import Toggle
from NetUtils import ClientStatus
from .Strings import AEItem
from .Items import gadgetsValues
from ..ladx.TrackerConsts import transition_state

# TODO: REMOVE ASAP - Borrowed from MM2
# This imports the bizhawk apworld if it's not already imported. This code block should be removed for a PR.
if "worlds._bizhawk" not in sys.modules:
    import importlib
    import os
    import zipimport

    bh_apworld_path = os.path.join(os.path.dirname(sys.modules["worlds"].__file__), "_bizhawk.apworld")
    if os.path.isfile(bh_apworld_path):
        importer = zipimport.zipimporter(bh_apworld_path)
        spec = importer.find_spec(os.path.basename(bh_apworld_path).rsplit(".", 1)[0])
        mod = importlib.util.module_from_spec(spec)
        mod.__package__ = f"worlds.{mod.__package__}"
        mod.__name__ = f"worlds.{mod.__name__}"
        sys.modules[mod.__name__] = mod
        importer.exec_module(mod)
    elif not os.path.isdir(os.path.splitext(bh_apworld_path)[0]):
        logging.error("Did not find _bizhawk.apworld required to play Ape Escape.")

import worlds._bizhawk as bizhawk
from worlds._bizhawk.client import BizHawkClient
from worlds.apeescape.RAMAddress import RAM
from worlds.apeescape.Locations import hundoMonkeysCount
from worlds.apeescape.Options import GoalOption, RequiredTokensOption, TotalTokensOption, TokenLocationsOption, LogicOption, InfiniteJumpOption, SuperFlyerOption, EntranceOption, KeyOption, ExtraKeysOption, CoinOption, MailboxOption, LampOption, GadgetOption, ShuffleNetOption, ShuffleWaterNetOption, LowOxygenSounds, TrapFillPercentage, ItemDisplayOption, KickoutPreventionOption, DeathLink


if TYPE_CHECKING:
    from worlds._bizhawk.context import BizHawkClientContext, BizHawkClientCommandProcessor
else:
    BizHawkClientContext = object

EXPECTED_ROM_NAME = "ape escape / AP 2"

logger = logging.getLogger("Client")

def cmd_ae_commands(self: "BizHawkClientCommandProcessor") -> None:
    """Show what commands are available for Ape Escape Archipelago"""
    from worlds._bizhawk.context import BizHawkClientContext
    if self.ctx.game != "Ape Escape":
        logger.warning("This command can only be used when playing Ape Escape.")
        return
    # if not self.ctx.server or not self.ctx.slot:
        # logger.warning("You must be connected to a server to use this command.")
        # return

    logger.info(f"----------------------------------------------\n"
                f"Commands for Ape Escape\n"
                f"----------------------------------------------\n"
                f"  /ae_commands\n"
                f"      Description : Show this list\n"
                f"  /bh_itemdisplay [On/Off]\n"
                f"      Description : Display items directly in the Bizhawk client\n"
                f"      [Optional] Status (On/Off) : Toggle or Enable/Disable the option\n"
                f"  /prevent_kickout [On/Off]\n"
                f"      Description : If on, prevents Spike from being ejected \n"
                f"                    after catching all monkeys in a level\n"
                f"      [Optional] Status (On/Off) : Toggle or Enable/Disable the option\n"
                f"  /deathlink [On/Off]\n"
                f"      Description : Enable/Disable the deathlink option\n"
                f"      [Optional] Status (On/Off) : Toggle or Enable/Disable the option\n"
                f"  /auto_equip [On/Off]\n"
                f"      Description : When on, will equip gadgets if there is a free face button\n"
                f"      [Optional] Status (On/Off) : Toggle or Enable/Disable the option\n")


def cmd_bh_itemdisplay(self: "BizHawkClientCommandProcessor", status = "") -> None:
    """Toggle the item display in Bizhawk"""
    from worlds._bizhawk.context import BizHawkClientContext
    if self.ctx.game != "Ape Escape":
        logger.warning("This command can only be used when playing Ape Escape.")
        return
    if not self.ctx.server or not self.ctx.slot:
        logger.warning("You must be connected to a server to use this command.")
        return

    ctx = self.ctx
    assert isinstance(ctx, BizHawkClientContext)
    client = ctx.client_handler
    assert isinstance(client, ApeEscapeClient)
    if status == "":
        if client.bhdisplay == 0:
            msg = "ON"
        else:
            msg = "OFF"
        logger.info(f"Bizhawk Item Display: {msg}\n"
                    f"    To change the status, use the command like so: /bh_itemdisplay [on/off]")
        return
    elif status.lower() == "on":
        client.bhdisplay = 1
    else:
        client.bhdisplay = 0
    client.changeBHDisplay = True
    if client.bhdisplay == 1:
        item_display = "ON"
        #client.send_bizhawk_message(ctx, "Bizhawk Item Display Enabled", "Passthrough", "")
    else:
        item_display = "OFF"
        #client.send_bizhawk_message(ctx, "Bizhawk Item Display Disabled", "Passthrough", "")
    client.BHDisplayOption = client.bhdisplay
    logger.info(f"Bizhawk Item Display is now {item_display}\n")


def cmd_prevent_kickout(self: "BizHawkClientCommandProcessor", status = "") -> None:
    """Toggle Kickout Prevention on and off"""
    from worlds._bizhawk.context import BizHawkClientContext
    if self.ctx.game != "Ape Escape":
        logger.warning("This command can only be used when playing Ape Escape.")
        return
    if not self.ctx.server or not self.ctx.slot:
        logger.warning("You must be connected to a server to use this command.")
        return

    ctx = self.ctx
    assert isinstance(ctx, BizHawkClientContext)
    client = ctx.client_handler
    assert isinstance(client, ApeEscapeClient)
    if status == "":
        if client.bhdisplay == 0:
            msg = "ON"
        else:
            msg = "OFF"
        logger.info(f"Kickout Prevention: {msg}\n"
                    f"    To change the status, use the command like so: /prevent_kickout [on/off]")
        return
    elif status.lower() == "on":
        client.preventKickOut = 1
    elif status.lower() == "off":
        client.preventKickOut = 0
    else:
        logger.info(f"Invalid argument for function ""prevent_kickout""\n")
        return
    # Replace slot_data
    #client.change_kickout_prevention(ctx)
    client.changeKickout = True
    if client.preventKickOut == 1:
        kickout = "ON"
        #client.send_bizhawk_message(ctx, "Kickout Prevention Enabled", "Custom", "")
    else:
        kickout = "OFF"
        #client.send_bizhawk_message(ctx, "Kickout Prevention Disabled", "Custom", "")
    client.KickoutPrevention = client.preventKickOut
    logger.info(f"Kickout Prevention is now {kickout}\n")


def cmd_deathlink(self: "BizHawkClientCommandProcessor", status = "") -> None:
    """Toggle Deathlink on and off"""
    from worlds._bizhawk.context import BizHawkClientContext
    if self.ctx.game != "Ape Escape":
        logger.warning("This command can only be used when playing Ape Escape.")
        return
    if not self.ctx.server or not self.ctx.slot:
        logger.warning("You must be connected to a server to use this command.")
        return

    ctx = self.ctx
    assert isinstance(ctx, BizHawkClientContext)
    client = ctx.client_handler
    assert isinstance(client, ApeEscapeClient)
    if status == "":
        if client.deathlink == 0:
            msg = "ON"
        else:
            msg = "OFF"
        logger.info(f"Deathlink: {msg}\n"
                    f"    To change the status, use the command like so: /deathlink [on/off]")
        return
    elif status.lower() == "on":
        client.deathlink = 1
    elif status.lower() == "off":
        client.deathlink = 0
    else:
        logger.info(f"Invalid argument for function ""deathlink""\n")
        return
    # Replace slot_data

    #client.change_kickout_prevention(ctx)
    client.changeDeathlink = True
    if client.deathlink == 1:
        msg = "ON"
        #client.send_bizhawk_message(ctx, "Deathlink Enabled", "Custom", "")
    else:
        msg = "OFF"
        #client.send_bizhawk_message(ctx, "Deathlink Disabled", "Custom", "")
    client.DeathLinkOption = client.deathlink
    logger.info(f"Deathlink is now {msg}\n")


def cmd_auto_equip(self: "BizHawkClientCommandProcessor", status = "") -> None:
    """Toggle Auto-Equip on and off"""
    from worlds._bizhawk.context import BizHawkClientContext
    if self.ctx.game != "Ape Escape":
        logger.warning("This command can only be used when playing Ape Escape.")
        return
    if not self.ctx.server or not self.ctx.slot:
        logger.warning("You must be connected to a server to use this command.")
        return

    ctx = self.ctx
    assert isinstance(ctx, BizHawkClientContext)
    client = ctx.client_handler
    assert isinstance(client, ApeEscapeClient)
    if status == "":
        if client.autoequip == 0:
            msg = "ON"
        else:
            msg = "OFF"
        logger.info(f"Auto-Equip: {msg}\n"
                    f"    To change the status, use the command like so: /autoequip [on/off]")
        return
    elif status.lower() == "on":
        client.autoequip = 1
    elif status.lower() == "off":
        client.autoequip = 0
    else:
        logger.info(f"Invalid argument for function ""autoequip""\n")
        return
    # Replace slot_data

    #client.change_kickout_prevention(ctx)
    client.changeAutoEquip = True
    if client.autoequip == 1:
        msg = "ON"
        #client.send_bizhawk_message(ctx, "Automatic Gadget Equipping Enabled", "Custom", "")
    else:
        msg = "OFF"
        #client.send_bizhawk_message(ctx, "Automatic Gadget Equipping Disabled", "Custom", "")
    client.AutoEquipOption = client.autoequip
    logger.info(f"Auto Equip is now {msg}\n")


class ApeEscapeClient(BizHawkClient):
    game = "Ape Escape"
    system = "PSX"

    # TODO Remove when doing official PR
    client_version = "0.8.3"

    local_checked_locations: Set[int]
    local_set_events: Dict[str, bool]
    local_found_key_items: Dict[str, bool]
    goal_flag: int

    offset = 128000000
    levelglobal = 0
    roomglobal = 0
    worldkeycount = 0
    tokencount = 0
    boss1flag = 0
    boss2flag = 0
    boss3flag = 0
    boss4flag = 0
    changeKickout = False
    changeDeathlink = False
    changeAutoEquip = False
    changeBHDisplay = False
    KickoutPrevention = 2
    preventKickOut = 2
    DeathLinkOption = 2
    deathlink = 2
    AutoEquipOption = 2
    autoequip = 2
    BHDisplayOption = 2
    bhdisplay = 2
    replacePunch = True
    currentCoinAddress = RAM.startingCoinAddress
    resetClient = False
    inWater = 0
    waternetState = 0
    watercatchState = 0
    bizhawk_itemdisplay = False
    bizhawk_display_set = False


    def __init__(self) -> None:
        super().__init__()

        self.local_checked_locations = set()
        self.local_set_events = {}
        self.local_found_key_items = {}


    def initialize_client(self):
        self.currentCoinAddress = RAM.startingCoinAddress
        self.changeKickout = False
        self.changeDeathlink = False
        self.changeAutoEquip = False
        self.changeBHDisplay = False
        self.DeathLinkOption = 2
        self.deathlink = 2
        self.KickoutPrevention = 2
        self.preventKickOut = 2
        self.AutoEquipOption = 2
        self.autoequip = 2
        self.BHDisplayOption = 2
        self.bhdisplay = 2
        self.replacePunch = True
        self.killPlayer = True
        self.inWater = 0
        self.waternetState = 0
        self.watercatchState = 0
        self.death_counter = None
        self.previous_death_link = 0
        self.pending_death_link: bool = False
        # default to true, as we don't want to send a deathlink until playing
        self.sending_death_link: bool = True
        self.ignore_next_death_link = False
        self.DIButton = 0
        self.CrCWaterButton = 0
        # self.CrCBasementButton = 0
        self.MM_Painting_Button = 0
        self.MM_MonkeyHead_Button = 0
        self.DR_Block_Pushed = 0
        self.TVT_Lobby_Button = 0
        self.bool_MMDoubleDoor = False
        self.bool_LampGlobal = False
        self.gotBanana = False
        self.lowOxygenCounter = 1
        self.trap_queue = []
        self.bizhawk_itemdisplay = False
        self.bizhawk_display_set = False


    async def validate_rom(self, ctx: BizHawkClientContext) -> bool:
        ape_identifier_ram_address: int = 0xA37F0
        ape_identifier_ram_address_PAL: int = 0xA37F0
        # BASCUS-94423SYS in ASCII = Ape Escape I think??
        bytes_expected: bytes = bytes.fromhex("4241534355532D3934343233535953")
        bytes_expected_PAL:bytes = bytes.fromhex("4245534345532D3031353634535953")
        try:
            bytes_actual: bytes = (await bizhawk.read(ctx.bizhawk_ctx, [(
                ape_identifier_ram_address, len(bytes_expected), "MainRAM"
            )]))[0]
            if bytes_actual != bytes_expected:
                if "ae_commands" in ctx.command_processor.commands:
                    ctx.command_processor.commands.pop("ae_commands")
                if "bh_itemdisplay" in ctx.command_processor.commands:
                    ctx.command_processor.commands.pop("bh_itemdisplay")
                if "prevent_kickout" in ctx.command_processor.commands:
                    ctx.command_processor.commands.pop("prevent_kickout")
                if "deathlink" in ctx.command_processor.commands:
                    ctx.command_processor.commands.pop("deathlink")
                if "auto_equip" in ctx.command_processor.commands:
                    ctx.command_processor.commands.pop("auto_equip")
                return False
        except Exception:
            if "ae_commands" in ctx.command_processor.commands:
                ctx.command_processor.commands.pop("ae_commands")
            if "bh_itemdisplay" in ctx.command_processor.commands:
                ctx.command_processor.commands.pop("bh_itemdisplay")
            if "prevent_kickout" in ctx.command_processor.commands:
                ctx.command_processor.commands.pop("prevent_kickout")
            if "deathlink" in ctx.command_processor.commands:
                ctx.command_processor.commands.pop("deathlink")
            if "auto_equip" in ctx.command_processor.commands:
                ctx.command_processor.commands.pop("auto_equip")
            return False

        if not self.game == "Ape Escape":
            if "ae_commands" in ctx.command_processor.commands:
                ctx.command_processor.commands.pop("ae_commands")
            if "bh_itemdisplay" in ctx.command_processor.commands:
                ctx.command_processor.commands.pop("bh_itemdisplay")
            if "prevent_kickout" in ctx.command_processor.commands:
                ctx.command_processor.commands.pop("prevent_kickout")
            if "deathlink" in ctx.command_processor.commands:
                ctx.command_processor.commands.pop("deathlink")
            if "auto_equip" in ctx.command_processor.commands:
                ctx.command_processor.commands.pop("auto_equip")
            return False
        # TODO Remove when doing official PR
        logger.info("================================================")
        logger.info("Archipelago Ape Escape version "  + self.client_version)
        logger.info("================================================")
        logger.info("Custom commands are available for this game")
        logger.info("Type /ae_commands for the full list")
        logger.info("================================================")
        ctx.game = self.game
        ctx.items_handling = 0b111
        ctx.want_slot_data = True
        ctx.watcher_timeout = 0.125
        if "ae_commands" not in ctx.command_processor.commands:
            ctx.command_processor.commands["ae_commands"] = cmd_ae_commands
        if "bizhawk_itemdisplay" not in ctx.command_processor.commands:
            ctx.command_processor.commands["bh_itemdisplay"] = cmd_bh_itemdisplay
        if "prevent_kickout" not in ctx.command_processor.commands:
            ctx.command_processor.commands["prevent_kickout"] = cmd_prevent_kickout
        if "deathlink" not in ctx.command_processor.commands:
            ctx.command_processor.commands["deathlink"] = cmd_deathlink
        if "auto_equip" not in ctx.command_processor.commands:
            ctx.command_processor.commands["auto_equip"] = cmd_auto_equip
        self.initialize_client()

        return True


    def on_package(self, ctx: "BizHawkClientContext", cmd: str, args: Dict[str, Any]) -> None:
        # if cmd == "Connected":
            # self.kickout_prevention_handling(ctx, "init")
            # self.deathlink_option_handling(ctx, "init")
            # self.autoequip_option_handling(ctx, "init")
            # self.bh_display_option_handling(ctx, "init")

        if cmd == "Bounced":
            if "tags" in args:
                assert ctx.slot is not None
                if "DeathLink" in args["tags"] and args["data"]["source"] != ctx.slot_info[ctx.slot].name:
                    self.on_deathlink(ctx)
        if cmd == "Retrieved":
            if "keys" not in args:
                print(f"invalid Retrieved packet to ApeEscapeClient: {args}")
                return
            keys = dict(args["keys"])
            if f"AE_kickoutprevention_{ctx.team}_{ctx.slot}" in args["keys"]:
                self.KickoutPrevention = keys.get(f"AE_kickoutprevention_{ctx.team}_{ctx.slot}", None)
            if f"AE_deathlink_{ctx.team}_{ctx.slot}" in args["keys"]:
                self.DeathLinkOption = keys.get(f"AE_deathlink_{ctx.team}_{ctx.slot}", None)
            if f"AE_autoequip_{ctx.team}_{ctx.slot}" in args["keys"]:
                self.AutoEquipOption = keys.get(f"AE_autoequip_{ctx.team}_{ctx.slot}", None)
            if f"AE_bhdisplay_{ctx.team}_{ctx.slot}" in args["keys"]:
                self.BHDisplayOption = keys.get(f"AE_bhdisplay_{ctx.team}_{ctx.slot}", None)
            if f"AE_DIButton_{ctx.team}_{ctx.slot}" in args["keys"]:
                self.DIButton = keys.get(f"AE_DIButton_{ctx.team}_{ctx.slot}", None)
            if f"AE_CrCWaterButton_{ctx.team}_{ctx.slot}" in args["keys"]:
                self.CrCWaterButton = keys.get(f"AE_CrCWaterButton_{ctx.team}_{ctx.slot}", None)
            # if f"AE_CrCBasementButton_{ctx.team}_{ctx.slot}" in args["keys"]:
                # self.CrCBasementButton = keys.get(f"AE_CrCBasementButton_{ctx.team}_{ctx.slot}", None)
            if f"AE_MM_Painting_Button_{ctx.team}_{ctx.slot}" in args["keys"]:
                self.MM_Painting_Button = keys.get(f"AE_MM_Painting_Button_{ctx.team}_{ctx.slot}", None)
            if f"AE_MM_MonkeyHead_Button_{ctx.team}_{ctx.slot}" in args["keys"]:
                self.MM_MonkeyHead_Button = keys.get(f"AE_MM_MonkeyHead_Button_{ctx.team}_{ctx.slot}", None)
            if f"AE_TVT_Lobby_Button_{ctx.team}_{ctx.slot}" in args["keys"]:
                self.TVT_Lobby_Button = keys.get(f"AE_TVT_Lobby_Button_{ctx.team}_{ctx.slot}", None)
            if f"AE_DR_Block_{ctx.team}_{ctx.slot}" in args["keys"]:
                self.DR_Block_Pushed = keys.get(f"AE_DR_Block_{ctx.team}_{ctx.slot}", None),


    async def check_gadgets(self, ctx: "BizHawkClientContext",gadgetStateFromServer) -> list[str]:
        gadgets = []
        if (gadgetStateFromServer & 1 != 0):
            gadgets.append(AEItem.Club.value)
        if (gadgetStateFromServer & 2 != 0):
            gadgets.append(AEItem.Net.value)
        if (gadgetStateFromServer & 4 != 0):
            gadgets.append(AEItem.Radar.value)
        if (gadgetStateFromServer & 8 != 0):
            gadgets.append(AEItem.Sling.value)
        if (gadgetStateFromServer & 16 != 0):
            gadgets.append(AEItem.Hoop.value)
        if (gadgetStateFromServer & 32 != 0):
            gadgets.append(AEItem.Punch.value)
        if (gadgetStateFromServer & 64 != 0):
            gadgets.append(AEItem.Flyer.value)
        if (gadgetStateFromServer & 128 != 0):
            gadgets.append(AEItem.Car.value)
        return gadgets


    async def set_auth(self, ctx: BizHawkClientContext) -> None:
        x = 3


    async def kickout_prevention_handling(self, ctx: BizHawkClientContext,context):
        if context == "init":
            if ctx.team is None:
                # print("skip")
                return
            await ctx.send_msgs([{
                "cmd": "Get",
                "keys": [f"AE_kickoutprevention_{ctx.team}_{ctx.slot}"]
            }])

            if self.KickoutPrevention == 2:
                print("Still Waiting")
                return
            # print(self.KickoutPrevention)
            # print(f"{ctx.team}_{ctx.slot}_{context}")
            if self.KickoutPrevention is None:
                print("Used slotdata")
                print(ctx.slot_data["kickoutprevention"])
                self.preventKickOut = int(ctx.slot_data["kickoutprevention"])
                # self.changeKickout = True
                # self.KickoutPrevention = self.preventKickOut
            else:
                # Got valid Datastorage, take this instead of slot_data
                # print("Got valid datastorage")
                # print(f"DATASTORAGE_PK{self.preventKickOut}_KP{self.KickoutPrevention}_{context}")
                self.preventKickOut = self.KickoutPrevention
            if self.preventKickOut == 1:
                msg = "ON"
            else:
                msg = "OFF"
            logger.info(f"\n--Options Status--")
            logger.info(f"Kickout Prevention: {msg}")
        elif context == "change":
            await ctx.send_msgs(
                [
                    {
                        "cmd": "Set",
                        "key": f"AE_kickoutprevention_{ctx.team}_{ctx.slot}",
                        "default": 0,
                        "want_reply": False,
                        "operations": [{"operation": "replace", "value": self.preventKickOut}],
                    }
                ]
            )
            if self.preventKickOut == 1:
                await self.send_bizhawk_message(ctx, "Kickout Prevention Enabled", "Custom", "")
            else:
                await self.send_bizhawk_message(ctx, "Kickout Prevention Disabled", "Custom", "")
            # self.preventKickOut = self.KickoutPrevention
            print(f"set AE_kickoutprevention_{ctx.team}_{ctx.slot} to {self.preventKickOut}")


    async def deathlink_option_handling(self, ctx: BizHawkClientContext,context):
        if context == "init":
            if ctx.team is None:
                #print("skip")
                return
            await ctx.send_msgs([{
                "cmd": "Get",
                "keys": [f"AE_deathlink_{ctx.team}_{ctx.slot}"]
            }])

            if self.DeathLinkOption == 2:
               # print("Still Waiting")
                return
            if self.DeathLinkOption is None:
                # print("Used slotdata")
                # print(ctx.slot_data["kickoutprevention"])
                self.deathlink = int(ctx.slot_data["death_link"])
                # self.KickoutPrevention = self.preventKickOut
                # self.changeKickout = True
            else:
                # Got valid Datastorage, take this instead of slot_data
                # print("Got valid datastorage")
                # print(f"DATASTORAGE_PK{self.preventKickOut}_KP{self.KickoutPrevention}_{context}")
                self.deathlink = self.DeathLinkOption
            if self.deathlink == 1:
                msg = "ON"
            else:
                msg = "OFF"
            logger.info(f"DeathLink: {msg}")
        elif context == "change":
            await ctx.send_msgs(
                [
                    {
                        "cmd": "Set",
                        "key": f"AE_deathlink_{ctx.team}_{ctx.slot}",
                        "default": 0,
                        "want_reply": False,
                        "operations": [{"operation": "replace", "value": self.deathlink}],
                    }
                ]
            )
            if self.deathlink == 1:
                await self.send_bizhawk_message(ctx, "Deathlink Enabled", "Custom", "")
            else:
                await self.send_bizhawk_message(ctx, "Deathlink Prevention Disabled", "Custom", "")
            # self.deathlink = self.DeathLinkOption
            print(f"set AE_deathlink_{ctx.team}_{ctx.slot} to {self.deathlink}")


    async def autoequip_option_handling(self, ctx: BizHawkClientContext,context):
        if context == "init":
            if ctx.team is None:
                # print("skip")
                return
            await ctx.send_msgs([{
                "cmd": "Get",
                "keys": [f"AE_autoequip_{ctx.team}_{ctx.slot}"]
            }])

            if self.AutoEquipOption == 2:
                # print("Still Waiting")
                return
            # print(self.AutoEquipOption)
            if self.AutoEquipOption is None:
                # print("Used slotdata")
                # print(ctx.slot_data["autoequip"])
                self.autoequip = int(ctx.slot_data["autoequip"])
                self.AutoEquipOption = self.autoequip
            else:
                # Got valid Datastorage, take this instead of slot_data
                # print("Got valid datastorage")
                # print(f"DATASTORAGE_{self.autoequip}_KP{self.AutoEquipOption}_{context}")
                self.autoequip = self.AutoEquipOption
            if self.autoequip == 1:
                msg = "ON"
            else:
                msg = "OFF"
            logger.info(f"Auto-Equip: {msg}")
        elif context == "change":
            await ctx.send_msgs(
                [
                    {
                        "cmd": "Set",
                        "key": f"AE_autoequip_{ctx.team}_{ctx.slot}",
                        "default": 0,
                        "want_reply": False,
                        "operations": [{"operation": "replace", "value": self.autoequip}],
                    }
                ]
            )
            if self.autoequip == 1:
                await self.send_bizhawk_message(ctx, "Auto-Equip Enabled", "Custom", "")
            else:
                await self.send_bizhawk_message(ctx, "Auto-Equip Disabled", "Custom", "")
            # self.autoequip = self.AutoEquipOption
            print(f"set AE_autoequip_{ctx.team}_{ctx.slot} to {self.autoequip}")


    async def bh_display_option_handling(self, ctx: BizHawkClientContext,context):
        if context == "init":
            if ctx.team is None:
                # print("skip")
                return
            await ctx.send_msgs([{
                "cmd": "Get",
                "keys": [f"AE_bhdisplay_{ctx.team}_{ctx.slot}"]
            }])

            if self.BHDisplayOption == 2:
                # print("Still Waiting")
                return
            if self.BHDisplayOption is None:
                # print("Used slotdata")
                # print(ctx.slot_data["kickoutprevention"])
                self.bhdisplay = int(ctx.slot_data["itemdisplay"])
                self.BHDisplayOption = self.bhdisplay
                # self.changeBHDisplay = True
            else:
                # Got valid Datastorage, take this instead of slot_data
                # print("Got valid datastorage")
                # print(f"DATASTORAGE_PK{self.preventKickOut}_KP{self.KickoutPrevention}_{context}")
                self.bhdisplay = self.BHDisplayOption
            if self.bhdisplay == 1:
                msg = "ON"
            else:
                msg = "OFF"
            logger.info(f"Bizhawk Item Display: {msg}")
        elif context == "change":
            await ctx.send_msgs(
                [
                    {
                        "cmd": "Set",
                        "key": f"AE_bhdisplay_{ctx.team}_{ctx.slot}",
                        "default": 0,
                        "want_reply": False,
                        "operations": [{"operation": "replace", "value": self.bhdisplay}],
                    }
                ]
            )
            if self.bhdisplay == 1:
                await self.send_bizhawk_message(ctx, "Bizhawk Item Display Enabled", "Passthrough", "")
            else:
                await self.send_bizhawk_message(ctx, "Bizhawk Item Display Disabled", "Passthrough", "")

            # self.bhdisplay = self.BHDisplayOption
            print(f"set AE_bhdisplay_{ctx.team}_{ctx.slot} to {self.bhdisplay}")


    async def send_bizhawk_message(self, ctx: BizHawkClientContext, message, msgtype, data) -> None:
        # Set the default state of the command based on the YAML option if it hasn't been set yet.
        # if self.bizhawk_display_set == False:
        #     self.bizhawk_itemdisplay = (ctx.slot_data["itemdisplay"] == ItemDisplayOption.option_on)
        #     self.bizhawk_display_set = True

        if self.bhdisplay == 1:
            if msgtype == "Item":
                sender = ctx.player_names[data.player]
                # print(sender)
                # print(str( item - self.offset]))
                itemname = data.item - self.offset
                itemname = ctx.item_names.lookup_in_game(data.item)

                # Same player as the seed, different message
                if sender == ctx.player_names[ctx.slot]:
                    strMessage = "You found your own '" + str(itemname) + "'"
                else:
                    strMessage = "You received '" + str(itemname) + "' from " + str(sender)
                await bizhawk.display_message(ctx.bizhawk_ctx, strMessage)
            elif msgtype == "Custom":
                strMessage = message
                await bizhawk.display_message(ctx.bizhawk_ctx, strMessage)
            elif msgtype == "Passthrough":
                strMessage = message
                await bizhawk.display_message(ctx.bizhawk_ctx, strMessage)
        elif msgtype == "Passthrough":
            strMessage = message
            await bizhawk.display_message(ctx.bizhawk_ctx, strMessage)


    async def game_watcher(self, ctx: BizHawkClientContext) -> None:
        # Detects if the AP connection is made.
        # If not, "return" immediately to not send anything while not connected
        if ctx.server is None or ctx.server.socket.closed or ctx.slot_data is None or ctx.auth is None:
            self.initClient = False
            return
        # Detection for triggering "initialize_client()" when Disconnecting/Reconnecting to AP (only once per connection)
        if self.initClient == False:
            self.initClient = True
            self.initialize_client()
            # print("========================")
            # print("INIT")
            # print("========================")
            # await self.kickout_prevention_handling(ctx,"init")
            # await self.deathlink_option_handling(ctx, "init")
            # await self.autoequip_option_handling(ctx, "init")
            # await self.bh_display_option_handling(ctx, "init")

            strMessage = "Connected to Bizhawk Client - Ape Escape Archipelago v " + str(self.client_version)
            await self.send_bizhawk_message(ctx, strMessage, "Passthrough", "")
        try:

            if self.KickoutPrevention == 2 or self.preventKickOut == 2:
                await self.kickout_prevention_handling(ctx, "init")
            if self.changeKickout == True:
                self.changeKickout = False
                await self.kickout_prevention_handling(ctx,"change")

            if self.DeathLinkOption == 2 or self.deathlink == 2:
                await self.deathlink_option_handling(ctx, "init")
            if self.changeDeathlink == True:
                self.changeDeathlink = False
                await self.deathlink_option_handling(ctx,"change")

            if self.AutoEquipOption == 2 or self.autoequip == 2:
                await self.autoequip_option_handling(ctx, "init")
            if self.changeAutoEquip == True:
                self.changeAutoEquip = False
                await self.autoequip_option_handling(ctx,"change")

            if self.BHDisplayOption == 2 or self.bhdisplay == 2:
                await self.bh_display_option_handling(ctx, "init")
            if self.changeBHDisplay == True:
                self.changeBHDisplay = False
                await self.bh_display_option_handling(ctx,"change")

            # await self.change_kickout_prevention(ctx)


            # Game state, locations and items read
            readTuples = [
                # GameStates
                (RAM.lastReceivedArchipelagoID, 4, "MainRAM"),
                (RAM.gameStateAddress, 1, "MainRAM"),
                (RAM.currentRoomIdAddress, 1, "MainRAM"),  # Current Room
                (RAM.Nearby_RoomIDAddress, 1, "MainRAM"),  # Nearby Room
                (RAM.currentLevelAddress, 1, "MainRAM"),  # Current Level
                (RAM.gameRunningAddress, 1, "MainRAM"),
                (RAM.jakeVictoryAddress, 1, "MainRAM"),  # Jake Races Victory state
                (RAM.transitionPhase, 1, "MainRAM"),  # Jake Races Victory state
                (RAM.localLevelState, 1, "MainRAM"),  # Jake Races Victory state
                # Locations (Coins, Monkeys, Mailboxes)
                (self.currentCoinAddress - 2, 1, "MainRAM"),  # Previous Coin State Room
                (self.currentCoinAddress, 1, "MainRAM"),  # Current New Coin State Room
                (RAM.totalCoinsAddress, 1, "MainRAM"),  # Coin Count
                (RAM.hundoApesAddress, 1, "MainRAM"),  # Hundo monkey count, to write to required count
                (RAM.requiredApesAddress, 1, "MainRAM"),
                (RAM.currentApesAddress, 1, "MainRAM"),
                (RAM.gotMailAddress, 1, "MainRAM"),
                (RAM.mailboxIDAddress, 1, "MainRAM"),
                # Items
                (RAM.energyChipsAddress, 1, "MainRAM"),
                (RAM.cookieAddress, 1, "MainRAM"),
                (RAM.livesAddress, 1, "MainRAM"),
                (RAM.flashAddress, 1, "MainRAM"),
                (RAM.rocketAddress, 1, "MainRAM"),
                (RAM.keyCountFromServer, 1, "MainRAM"),
                (RAM.tokenCountFromServer, 1, "MainRAM"),
                # Misc
                (RAM.spikeStateAddress, 1, "MainRAM"),
                (RAM.spikeState2Address, 1, "MainRAM"),
                (RAM.kickoutofLevelAddress, 4, "MainRAM"),
                (RAM.kickoutofLevelAddress2, 4, "MainRAM"),
                (RAM.CrC_BossPhaseAddress, 1, "MainRAM"),
                (RAM.CrC_DoorVisual, 1, "MainRAM"),
                (RAM.CrC_BossLife, 1, "MainRAM"),
                (RAM.CrC_kickoutofLevelAddress, 4, "MainRAM"),
                (RAM.TVT_kickoutofLevelAddress, 4, "MainRAM"),
                (RAM.TVT_BossPhase, 1, "MainRAM"),
                (RAM.TVT_BossLife, 1, "MainRAM"),
                (RAM.S1_P2_State, 1, "MainRAM"),
                (RAM.S1_P2_Life, 1, "MainRAM"),
                (RAM.S2_isCaptured, 1, "MainRAM"),
                (RAM.S1_Cutscene_Redirection, 4, "MainRAM"),
                (RAM.S2_Cutscene_Redirection, 4, "MainRAM"),
                (RAM.S1_P1_FightTrigger, 1, "MainRAM"),
            ]

            reads = await bizhawk.read(ctx.bizhawk_ctx, readTuples)

            # GameStates
            recv_index = int.from_bytes(reads[0], byteorder = "little")
            gameState = int.from_bytes(reads[1], byteorder = "little")
            currentRoom = int.from_bytes(reads[2], byteorder = "little")
            NearbyRoom = int.from_bytes(reads[3], byteorder = "little")
            currentLevel = int.from_bytes(reads[4], byteorder = "little")
            gameRunning = int.from_bytes(reads[5], byteorder = "little")
            jakeVictory = int.from_bytes(reads[6], byteorder = "little")
            transitionPhase = int.from_bytes(reads[7], byteorder = "little")
            localLevelState = int.from_bytes(reads[8], byteorder = "little")
            # Locations
            previousCoinStateRoom = int.from_bytes(reads[9], byteorder = "little")
            currentCoinStateRoom = int.from_bytes(reads[10], byteorder = "little")
            coinCount = int.from_bytes(reads[11], byteorder = "little")
            localhundoCount = int.from_bytes(reads[12], byteorder = "little")
            requiredApes = int.from_bytes(reads[13], byteorder = "little")
            currentApes = int.from_bytes(reads[14], byteorder = "little")
            gotMail = int.from_bytes(reads[15], byteorder = "little")
            mailboxID = int.from_bytes(reads[16], byteorder = "little")
            # Items
            energyChips = int.from_bytes(reads[17], byteorder = "little")
            cookies = int.from_bytes(reads[18], byteorder = "little")
            totalLives = int.from_bytes(reads[19], byteorder = "little")
            flashAmmo = int.from_bytes(reads[20], byteorder = "little")
            rocketAmmo = int.from_bytes(reads[21], byteorder = "little")
            keyCountFromServer = int.from_bytes(reads[22], byteorder = "little")
            tokenCountFromServer = int.from_bytes(reads[23], byteorder = "little")
            # Misc
            spikeState = int.from_bytes(reads[24], byteorder = "little")
            spikeState2 = int.from_bytes(reads[25], byteorder = "little")
            kickoutofLevel = int.from_bytes(reads[26], byteorder = "little")
            kickoutofLevel2 = int.from_bytes(reads[27], byteorder="little")
            CrC_BossPhase = int.from_bytes(reads[28], byteorder = "little")
            CrC_DoorVisual = int.from_bytes(reads[29], byteorder = "little")
            CrC_BossLife = int.from_bytes(reads[30], byteorder = "little")
            CrC_kickoutofLevel = int.from_bytes(reads[31], byteorder = "little")
            TVT_kickoutofLevel = int.from_bytes(reads[32], byteorder = "little")
            TVT_BossPhase = int.from_bytes(reads[33], byteorder = "little")
            TVT_BossLife = int.from_bytes(reads[34], byteorder = "little")
            S1_P2_State = int.from_bytes(reads[35], byteorder = "little")
            S1_P2_Life = int.from_bytes(reads[36], byteorder = "little")
            S2_isCaptured = int.from_bytes(reads[37], byteorder = "little")
            S1_Cutscene_Redirection = int.from_bytes(reads[38], byteorder = "little")
            S2_Cutscene_Redirection = int.from_bytes(reads[39], byteorder = "little")
            S1_P1_FightTrigger = int.from_bytes(reads[40], byteorder = "little")

            # Related to Gadgets
            gadgetTuples = [
                (RAM.unlockedGadgetsAddress, 1, "MainRAM"),  # Gadget unlocked states
                (RAM.gadgetStateFromServer, 2, "MainRAM"),
                (RAM.heldGadgetAddress, 1, "MainRAM"),  # Currently held gadget
                (RAM.triangleGadgetAddress, 1, "MainRAM"),  # Gadget equipped to each face button
                (RAM.squareGadgetAddress, 1, "MainRAM"),
                (RAM.circleGadgetAddress, 1, "MainRAM"),
                (RAM.crossGadgetAddress, 1, "MainRAM"),
                (RAM.gadgetUseStateAddress, 1, "MainRAM"),  # Which gadget is used in what way. **Not used at the moment
                (RAM.punchVisualAddress, 32, "MainRAM"),  # Which gadget is used in what way. **Not used at the moment
            ]

            gadgetReads = await bizhawk.read(ctx.bizhawk_ctx, gadgetTuples)

            gadgets = int.from_bytes(gadgetReads[0], byteorder = "little")
            gadgetStateFromServer = int.from_bytes(gadgetReads[1], byteorder = "little")
            heldGadget = int.from_bytes(gadgetReads[2], byteorder = "little")
            triangleGadget = int.from_bytes(gadgetReads[3], byteorder = "little")
            squareGadget = int.from_bytes(gadgetReads[4], byteorder = "little")
            circleGadget = int.from_bytes(gadgetReads[5], byteorder = "little")
            crossGadget = int.from_bytes(gadgetReads[6], byteorder = "little")
            gadgetUseState = int.from_bytes(gadgetReads[7], byteorder = "little")
            punchVisualAddress = int.from_bytes(gadgetReads[8], byteorder = "little")

            # Menu and level select reads
            menuTuples = [
                (RAM.selectedWorldAddress, 1, "MainRAM"),  # In level select, the current world
                (RAM.selectedLevelAddress, 1, "MainRAM"),  # In level select, the current level
                (RAM.enteredWorldAddress, 1, "MainRAM"),  # After selecting a level, the entered world
                (RAM.enteredLevelAddress, 1, "MainRAM"),  # After selecting a level, the entered level
                (RAM.menuStateAddress, 1, "MainRAM"),
                (RAM.menuState2Address, 1, "MainRAM"),
                (RAM.newGameAddress, 1, "MainRAM"),
                (RAM.startingCoinAddress, 100, "MainRAM"),
                (RAM.temp_startingCoinAddress, 100, "MainRAM"),
                (RAM.SA_CompletedAddress, 1, "MainRAM"),
                (RAM.Temp_SA_CompletedAddress, 1, "MainRAM"),
                (RAM.GA_CompletedAddress, 1, "MainRAM"),
                (RAM.Temp_GA_CompletedAddress, 1, "MainRAM"),
                (RAM.worldIsScrollingRight, 2, "MainRAM")

            ]

            menuReads = await bizhawk.read(ctx.bizhawk_ctx, menuTuples)

            # Level Select/Menu data
            LS_currentWorld = int.from_bytes(menuReads[0], byteorder = "little")
            LS_currentLevel = int.from_bytes(menuReads[1], byteorder = "little")
            status_currentWorld = int.from_bytes(menuReads[2], byteorder = "little")
            status_currentLevel = int.from_bytes(menuReads[3], byteorder = "little")
            menuState = int.from_bytes(menuReads[4], byteorder = "little")
            menuState2 = int.from_bytes(menuReads[5], byteorder = "little")
            newGameAddress = int.from_bytes(menuReads[6], byteorder = "little")
            # Level Select Coin hiding
            CoinTable = int.from_bytes(menuReads[7], byteorder = "little")
            TempCoinTable = int.from_bytes(menuReads[8], byteorder = "little")
            SA_Completed = int.from_bytes(menuReads[9], byteorder = "little")
            Temp_SA_Completed = int.from_bytes(menuReads[10], byteorder = "little")
            GA_Completed = int.from_bytes(menuReads[11], byteorder = "little")
            Temp_GA_Completed = int.from_bytes(menuReads[12], byteorder = "little")
            worldIsScrollingRight = int.from_bytes(menuReads[13], byteorder = "little")

            # Water net shuffle Reads
            swimTuples = [
                (RAM.canDiveAddress, 4, "MainRAM"),
                (RAM.canWaterCatchAddress, 1, "MainRAM"),
                (RAM.tempWaterNetAddress, 1, "MainRAM"),
                (RAM.tempWaterCatchAddress, 1, "MainRAM"),
                (RAM.isUnderwater, 1, "MainRAM"),  # Underwater variable
                (RAM.swim_oxygenLevelAddress, 2, "MainRAM"),
            ]

            swimReads = await bizhawk.read(ctx.bizhawk_ctx, swimTuples)

            canDive = int.from_bytes(swimReads[0], byteorder = "little")
            canWaterCatch = int.from_bytes(swimReads[1], byteorder = "little")
            WaterNetStateFromServer = int.from_bytes(swimReads[2], byteorder = "little")
            WaterCatchStateFromServer = int.from_bytes(swimReads[3], byteorder = "little")
            isUnderwater = int.from_bytes(swimReads[4], byteorder = "little")
            swim_oxygenLevel = int.from_bytes(swimReads[5], byteorder = "little")

            lampTuples = [
                (RAM.tempCB_LampAddress, 1, "MainRAM"),
                (RAM.tempDI_LampAddress, 1, "MainRAM"),
                (RAM.tempCrC_LampAddress, 1, "MainRAM"),
                (RAM.tempCP_LampAddress, 1, "MainRAM"),
                (RAM.tempSF_LampAddress, 1, "MainRAM"),
                (RAM.tempTVT_Lobby_LampAddress, 1, "MainRAM"),
                (RAM.tempTVT_Tank_LampAddress, 1, "MainRAM"),
                (RAM.tempMM_LampAddress, 1, "MainRAM"),
            ]

            lampReads = await bizhawk.read(ctx.bizhawk_ctx, lampTuples)

            CBLampStateFromServer = int.from_bytes(lampReads[0], byteorder = "little")
            DILampStateFromServer = int.from_bytes(lampReads[1], byteorder = "little")
            CrCLampStateFromServer = int.from_bytes(lampReads[2], byteorder = "little")
            CPLampStateFromServer = int.from_bytes(lampReads[3], byteorder = "little")
            SFLampStateFromServer = int.from_bytes(lampReads[4], byteorder = "little")
            TVTLobbyLampStateFromServer = int.from_bytes(lampReads[5], byteorder = "little")
            TVTTankLampStateFromServer = int.from_bytes(lampReads[6], byteorder = "little")
            MMLampStateFromServer = int.from_bytes(lampReads[7], byteorder = "little")

            locksTuples = [
                # Doors
                (RAM.temp_MMLobbyDoorAddress, 1, "MainRAM"),
                (RAM.MM_Lobby_DoubleDoor_OpenAddress, 1, "MainRAM"),
                (RAM.MM_Jake_DefeatedAddress, 1, "MainRAM"),
                (RAM.MM_Professor_RescuedAddress, 1, "MainRAM"),
                (RAM.MM_Clown_State, 1, "MainRAM"),
                (RAM.MM_Natalie_RescuedAddress, 1, "MainRAM"),
                (RAM.temp_MM_Jake_DefeatedAddress, 1, "MainRAM"),
                (RAM.temp_MM_Professor_RescuedAddress, 1, "MainRAM"),
                (RAM.temp_MM_Natalie_RescuedAddress, 1, "MainRAM"),
                (RAM.MM_Natalie_Rescued_Local, 1, "MainRAM"),
                (RAM.MM_Lobby_DoorDetection, 4, "MainRAM"),

                # Buttons
                (RAM.DI_Button_Pressed, 1, "MainRAM"),
                (RAM.DI_Button_DoorVisual, 1, "MainRAM"),
                (RAM.CrC_Water_ButtonPressed, 1, "MainRAM"),
                (RAM.CrC_Water_DoorVisual, 1, "MainRAM"),
                (RAM.CrC_Basement_ButtonPressed, 1, "MainRAM"),
                (RAM.CrC_Basement_DoorVisual1, 1, "MainRAM"),
                (RAM.TVT_Lobby_Button, 1, "MainRAM"),
                (RAM.TVT_Lobby_Water_HitBox, 1, "MainRAM"),
                (RAM.MM_MonkeyHead_Button, 1, "MainRAM"),
                (RAM.MM_MonkeyHead_Door, 1, "MainRAM"),
                (RAM.MM_Painting_Button, 1, "MainRAM"),
                (RAM.MM_Painting_Visual, 1, "MainRAM"),
                (RAM.DR_Block_Pushed, 1, "MainRAM"),

            ]

            locksReads = await bizhawk.read(ctx.bizhawk_ctx, locksTuples)
            # Doors
            MM_Lobby_DoubleDoor = int.from_bytes(locksReads[0], byteorder = "little")
            MM_Lobby_DoubleDoor_Open = int.from_bytes(locksReads[1], byteorder = "little")
            MM_Jake_DefeatedAddress = int.from_bytes(locksReads[2], byteorder = "little")
            MM_Professor_RescuedAddress = int.from_bytes(locksReads[3], byteorder = "little")
            MM_Clown_State = int.from_bytes(locksReads[4], byteorder = "little")
            MM_Natalie_RescuedAddress = int.from_bytes(locksReads[5], byteorder = "little")
            MM_Jake_Defeated = int.from_bytes(locksReads[6], byteorder = "little")
            MM_Professor_Rescued = int.from_bytes(locksReads[7], byteorder = "little")
            MM_Natalie_Rescued = int.from_bytes(locksReads[8], byteorder = "little")
            MM_Natalie_Rescued_Local = int.from_bytes(locksReads[9], byteorder = "little")
            MM_Lobby_DoorDetection = int.from_bytes(locksReads[10], byteorder = "little")

            # Buttons
            DI_Button_Pressed = int.from_bytes(locksReads[11], byteorder = "little")
            DI_Button_DoorVisual = int.from_bytes(locksReads[12], byteorder = "little")
            CrC_Water_ButtonPressed = int.from_bytes(locksReads[13], byteorder = "little")
            CrC_Water_Door_Visual = int.from_bytes(locksReads[14], byteorder = "little")
            CrC_Basement_ButtonPressed = int.from_bytes(locksReads[15], byteorder = "little")
            CrC_Basement_DoorVisual1 = int.from_bytes(locksReads[16], byteorder = "little")
            TVT_Lobby_ButtonPressed = int.from_bytes(locksReads[17], byteorder = "little")
            TVT_Lobby_Water_Hitbox = int.from_bytes(locksReads[18], byteorder = "little")
            MM_MonkeyHead_ButtonPressed = int.from_bytes(locksReads[19], byteorder = "little")
            MM_MonkeyHead_Door = int.from_bytes(locksReads[20], byteorder = "little")
            MM_Painting_ButtonPressed = int.from_bytes(locksReads[21], byteorder = "little")
            MM_Painting_Visual = int.from_bytes(locksReads[22], byteorder = "little")
            DR_Block_Pushed = int.from_bytes(locksReads[23], byteorder="little")
            levelCountTuples = [
                (RAM.levelMonkeyCount[11], 1, "MainRAM"),
                (RAM.levelMonkeyCount[12], 1, "MainRAM"),
                (RAM.levelMonkeyCount[13], 1, "MainRAM"),
                (RAM.levelMonkeyCount[21], 1, "MainRAM"),
                (RAM.levelMonkeyCount[22], 1, "MainRAM"),
                (RAM.levelMonkeyCount[23], 1, "MainRAM"),
                (RAM.levelMonkeyCount[31], 1, "MainRAM"),
                (RAM.levelMonkeyCount[41], 1, "MainRAM"),
                (RAM.levelMonkeyCount[42], 1, "MainRAM"),
                (RAM.levelMonkeyCount[43], 1, "MainRAM"),
                (RAM.levelMonkeyCount[51], 1, "MainRAM"),
                (RAM.levelMonkeyCount[52], 1, "MainRAM"),
                (RAM.levelMonkeyCount[53], 1, "MainRAM"),
                (RAM.levelMonkeyCount[61], 1, "MainRAM"),
                (RAM.levelMonkeyCount[71], 1, "MainRAM"),
                (RAM.levelMonkeyCount[72], 1, "MainRAM"),
                (RAM.levelMonkeyCount[73], 1, "MainRAM"),
                (RAM.levelMonkeyCount[81], 1, "MainRAM"),
                (RAM.levelMonkeyCount[82], 1, "MainRAM"),
                (RAM.levelMonkeyCount[83], 1, "MainRAM"),
                (RAM.levelMonkeyCount[91], 1, "MainRAM")
            ]
            monkeylevelcounts = await bizhawk.read(ctx.bizhawk_ctx, levelCountTuples)

            # Write tables
            itemsWrites = []
            TrapWrites = []
            Menuwrites = []

            # Handle death link
            DL_Reads = [cookies,gameRunning,gameState,menuState2,spikeState2]
            await self.handle_death_link(ctx,DL_Reads)

            # When in Menu, change the behavior of "NewGame" to warp you to time station instead
            if gameState == RAM.gameState["Menu"] and newGameAddress == 0xAC:
                Menuwrites += [(RAM.newGameAddress, 0x98.to_bytes(1, "little"), "MainRAM")]
                Menuwrites += [(RAM.cookieAddress, 0x05.to_bytes(1, "little"), "MainRAM")]
                await bizhawk.write(ctx.bizhawk_ctx, Menuwrites)
            # Set Initial received_ID when in first level ever OR in first hub ever
            if (recv_index == 0xFFFFFFFF) or (recv_index == 0x00FF00FF):
                recv_index = 0
                # Set gadgetStateFromServer to default if you connect in first level/first time hub
                if gadgetStateFromServer == 0xFFFF or gadgetStateFromServer == 0x00FF:
                    gadgetStateFromServer = 0

            if keyCountFromServer == 0xFF:
                # Get items from server
                keyCountFromServer = 0

            if tokenCountFromServer == 0xFF:
                # Get items from server
                tokenCountFromServer = 0

            if MM_Lobby_DoubleDoor == 0xFF:
                MM_Lobby_DoubleDoor = 0

            if MM_Jake_Defeated > 0x01:
                MM_Jake_Defeated = 0

            if MM_Professor_Rescued > 0x01:
                MM_Professor_Rescued = 0

            if MM_Natalie_Rescued > 0x01:
                MM_Natalie_Rescued = 0

            # Get WaterNet state from memory
            waternetState = 0
            if WaterNetStateFromServer != 0xFF:
                waternetState = WaterNetStateFromServer

            # Get Dive state from memory
            watercatchState = 0
            if WaterCatchStateFromServer != 0x00:
                watercatchState = WaterCatchStateFromServer

            # Get Lamp states
            CBLampState = 0
            DILampState = 0
            CrCLampState = 0
            CPLampState = 0
            SFLampState = 0
            TVTLobbyLampState = 0
            TVTTankLampState = 0
            MMLampState = 0

            if CBLampStateFromServer != 0x00 and CBLampStateFromServer != 0xFF: CBLampState = CBLampStateFromServer
            if DILampStateFromServer != 0x00 and DILampStateFromServer != 0xFF: DILampState = DILampStateFromServer
            if CrCLampStateFromServer != 0x00 and CrCLampStateFromServer != 0xFF: CrCLampState = CrCLampStateFromServer
            if CPLampStateFromServer != 0x00 and CPLampStateFromServer != 0xFF: CPLampState = CPLampStateFromServer
            if SFLampStateFromServer != 0x00 and SFLampStateFromServer != 0xFF: SFLampState = SFLampStateFromServer
            if TVTLobbyLampStateFromServer != 0x00 and TVTLobbyLampStateFromServer != 0xFF: TVTLobbyLampState = TVTLobbyLampStateFromServer
            if TVTTankLampStateFromServer != 0x00 and TVTTankLampStateFromServer != 0xFF: TVTTankLampState = TVTTankLampStateFromServer
            if MMLampStateFromServer != 0x00 and MMLampStateFromServer != 0xFF: MMLampState = MMLampStateFromServer


            START_recv_index = recv_index

            # Prevent sending items when connecting early (Sony, Menu or Intro Cutscene)
            firstBootStates = {RAM.gameState["Sony"], RAM.gameState["Menu"], RAM.gameState["Cutscene2"], RAM.gameState["Demo"], RAM.gameState["Save/Load"]}
            boolIsFirstBoot = gameState in firstBootStates
            #print(boolIsFirstBoot)
            if recv_index < (len(ctx.items_received)) and not boolIsFirstBoot:
                increment = 0
                for item in ctx.items_received:
                    # Increment to already received address first before sending
                    if increment < START_recv_index:
                        increment += 1
                    else:
                        recv_index += 1
                        if RAM.items["Club"] <= (item.item - self.offset) <= RAM.items["Car"]:
                            if gadgetStateFromServer | (item.item - self.offset) != gadgetStateFromServer:
                                gadgetStateFromServer = gadgetStateFromServer | (item.item - self.offset)
                        elif (item.item - self.offset) == RAM.items["Key"]:
                            keyCountFromServer += 1
                        elif (item.item - self.offset) == RAM.items["Token"]:
                            tokenCountFromServer += 1
                            if ctx.slot_data["goal"] == GoalOption.option_tokenhunt and tokenCountFromServer == min(ctx.slot_data["requiredtokens"], ctx.slot_data["totaltokens"]):
                                await ctx.send_msgs([{
                                    "cmd": "StatusUpdate",
                                    "status": ClientStatus.CLIENT_GOAL
                                }])
                                await self.send_bizhawk_message(ctx, "You have completed your goal o[8(|)", "Passthrough", "")
                        elif (item.item - self.offset) == RAM.items["Victory"]:
                            await ctx.send_msgs([{
                                "cmd": "StatusUpdate",
                                "status": ClientStatus.CLIENT_GOAL
                            }])
                            await self.send_bizhawk_message(ctx, "You have completed your goal o[8(|)", "Passthrough", "")
                        elif (item.item - self.offset) == RAM.items["WaterNet"]:
                            waternetState = 2
                            watercatchState = 1
                        elif (item.item - self.offset) == RAM.items["ProgWaterNet"]:
                            if waternetState != 2:
                                waternetState += 1
                        elif (item.item - self.offset) == RAM.items["MM_DoubleDoorKey"]:
                            MM_Lobby_DoubleDoor = 1
                        elif (item.item - self.offset) == RAM.items["WaterCatch"]:
                            watercatchState = 1
                        elif (item.item - self.offset) == RAM.items["CB_Lamp"]:
                            CBLampState = 1
                        elif (item.item - self.offset) == RAM.items["DI_Lamp"]:
                            DILampState = 1
                        elif (item.item - self.offset) == RAM.items["CrC_Lamp"]:
                            CrCLampState = 1
                        elif (item.item - self.offset) == RAM.items["CP_Lamp"]:
                            CPLampState = 1
                        elif (item.item - self.offset) == RAM.items["SF_Lamp"]:
                            SFLampState = 1
                        elif (item.item - self.offset) == RAM.items["TVT_Lobby_Lamp"]:
                            TVTLobbyLampState = 1
                        elif (item.item - self.offset) == RAM.items["TVT_Tank_Lamp"]:
                            TVTTankLampState = 1
                        elif (item.item - self.offset) == RAM.items["MM_Lamp"]:
                            MMLampState = 1
                        elif RAM.items["Shirt"] <= (item.item - self.offset) <= RAM.items["ThreeRocket"]:
                            if (item.item - self.offset) == RAM.items["Triangle"] or (item.item - self.offset) == RAM.items["BigTriangle"] or (item.item - self.offset) == RAM.items["BiggerTriangle"]:
                                if (item.item - self.offset) == RAM.items["Triangle"]:
                                    energyChips += 1
                                elif (item.item - self.offset) == RAM.items["BigTriangle"]:
                                    energyChips += 5
                                elif (item.item - self.offset) == RAM.items["BiggerTriangle"]:
                                    energyChips += 25
                                # If total gets greater than 100, subtract 100 and give a life instead
                                if energyChips >= 100:
                                    energyChips = energyChips - 100
                                    # Don't give a life if it would exceed 99 lives
                                    if totalLives < 100:
                                        totalLives += 1
                            elif (item.item - self.offset) == RAM.items["Cookie"]:
                                if cookies < 5:
                                    cookies += 1
                            elif (item.item - self.offset) == RAM.items["FiveCookies"]:
                                cookies = 5
                            elif (item.item - self.offset) == RAM.items["Shirt"]:
                                if totalLives < 100:
                                    totalLives += 1
                            # add special pellets, ensuring they don't go over the current cap
                            elif (item.item - self.offset) == RAM.items["Flash"]:
                                if flashAmmo < 9:
                                    flashAmmo += 1
                            elif (item.item - self.offset) == RAM.items["Rocket"]:
                                if rocketAmmo < 9:
                                    rocketAmmo += 1
                            elif (item.item - self.offset) == RAM.items["ThreeFlash"]:
                                flashAmmo += 3
                                if flashAmmo > 9:
                                    flashAmmo = 9
                            elif (item.item - self.offset) == RAM.items["ThreeRocket"]:
                                rocketAmmo += 3
                                if rocketAmmo > 9:
                                    rocketAmmo = 9
                        # elif RAM.items["BananaPeelTrap"] <= (item.item - self.offset) <= RAM.items["GadgetShuffleTrap"]:
                        elif RAM.items["BananaPeelTrap"] == (item.item - self.offset):
                            self.trap_queue.append((item.item - self.offset))

                        # Send message of received item - Victory has a special message above
                        if item.item - self.offset != RAM.items["Victory"]:
                            await self.send_bizhawk_message(ctx, "", "Item", item)

                # Writes to memory if there is a new item, after the loop
                itemsWrites += [(RAM.lastReceivedArchipelagoID, recv_index.to_bytes(4, "little"), "MainRAM")]
                itemsWrites += [(RAM.tempLastReceivedArchipelagoID, recv_index.to_bytes(4, "little"), "MainRAM")]
                itemsWrites += [(RAM.energyChipsAddress, energyChips.to_bytes(1, "little"), "MainRAM")]
                itemsWrites += [(RAM.cookieAddress, cookies.to_bytes(1, "little"), "MainRAM")]
                itemsWrites += [(RAM.livesAddress, totalLives.to_bytes(1, "little"), "MainRAM")]
                itemsWrites += [(RAM.flashAddress, flashAmmo.to_bytes(1, "little"), "MainRAM")]
                itemsWrites += [(RAM.rocketAddress, rocketAmmo.to_bytes(1, "little"), "MainRAM")]
                itemsWrites += [(RAM.keyCountFromServer, keyCountFromServer.to_bytes(1, "little"), "MainRAM")]
                itemsWrites += [(RAM.tempKeyCountFromServer, keyCountFromServer.to_bytes(1, "little"), "MainRAM")]
                itemsWrites += [(RAM.tokenCountFromServer, tokenCountFromServer.to_bytes(1, "little"), "MainRAM")]
                itemsWrites += [(RAM.tempTokenCountFromServer, tokenCountFromServer.to_bytes(1, "little"), "MainRAM")]
                itemsWrites += [(RAM.gadgetStateFromServer, gadgetStateFromServer.to_bytes(2, "little"), "MainRAM")]
                itemsWrites += [(RAM.tempGadgetStateFromServer, gadgetStateFromServer.to_bytes(2, "little"), "MainRAM")]
                itemsWrites += [(RAM.tempWaterNetAddress, waternetState.to_bytes(1, "little"), "MainRAM")]
                itemsWrites += [(RAM.tempWaterCatchAddress, watercatchState.to_bytes(1, "little"), "MainRAM")]
                itemsWrites += [(RAM.tempCB_LampAddress, CBLampState.to_bytes(1, "little"), "MainRAM")]
                itemsWrites += [(RAM.tempDI_LampAddress, DILampState.to_bytes(1, "little"), "MainRAM")]
                itemsWrites += [(RAM.tempCrC_LampAddress, CrCLampState.to_bytes(1, "little"), "MainRAM")]
                itemsWrites += [(RAM.tempCP_LampAddress, CPLampState.to_bytes(1, "little"), "MainRAM")]
                itemsWrites += [(RAM.tempSF_LampAddress, SFLampState.to_bytes(1, "little"), "MainRAM")]
                itemsWrites += [(RAM.tempTVT_Lobby_LampAddress, TVTLobbyLampState.to_bytes(1, "little"), "MainRAM")]
                itemsWrites += [(RAM.tempTVT_Tank_LampAddress, TVTTankLampState.to_bytes(1, "little"), "MainRAM")]
                itemsWrites += [(RAM.tempMM_LampAddress, MMLampState.to_bytes(1, "little"), "MainRAM")]
                itemsWrites += [(RAM.temp_MMLobbyDoorAddress, MM_Lobby_DoubleDoor.to_bytes(1, "little"), "MainRAM")]

            self.worldkeycount = keyCountFromServer
            self.tokencount = tokenCountFromServer

            # Local update conditions
            # Condition to not update on first pass of client (self.roomglobal is 0 on first pass)
            if self.roomglobal == 0:
                localcondition = False
            else:
                localcondition = (currentLevel == self.levelglobal)

            # Stock BossRooms in a variable (For excluding these rooms in local monkeys sending)
            bossRooms = RAM.bossListLocal.keys()
            mailboxesRooms = RAM.mailboxListLocal.keys()

            # Check if in level select or in time hub, then read global monkeys
            if gameState == RAM.gameState["LevelSelect"] or currentLevel == RAM.levels["Time"]:
                keyList = list(RAM.monkeyListGlobal.keys())
                valList = list(RAM.monkeyListGlobal.values())

                addresses = []

                for val in valList:
                    tuple1 = (val, 1, "MainRAM")
                    addresses.append(tuple1)

                globalMonkeys = await bizhawk.read(ctx.bizhawk_ctx, addresses)
                monkeysToSend = set()

                for i in range(len(globalMonkeys)):
                    if int.from_bytes(globalMonkeys[i], byteorder='little') == RAM.caughtStatus["PrevCaught"]:
                        monkeysToSend.add(keyList[i] + self.offset)

                if monkeysToSend is not None and monkeysToSend != set():
                    await ctx.send_msgs([{
                        "cmd": "LocationChecks",
                        "locations": list(x for x in monkeysToSend)
                    }])

            # elif being in a level
            # check if NOT in a boss room since there is no monkeys to send there
            elif gameState == RAM.gameState["InLevel"] and (localcondition) and not(currentRoom in bossRooms):
                monkeyaddrs = RAM.monkeyListLocal[currentRoom]
                key_list = list(monkeyaddrs.keys())
                val_list = list(monkeyaddrs.values())
                addresses = []

                for val in val_list:
                    tuple1 = (val, 1, "MainRAM")
                    addresses.append(tuple1)

                localmonkeys = await bizhawk.read(ctx.bizhawk_ctx, addresses)
                monkeys_to_send = set()

                for i in range(len(localmonkeys)):
                    if int.from_bytes(localmonkeys[i], byteorder='little') == RAM.caughtStatus["Caught"]:
                        monkeys_to_send.add(key_list[i] + self.offset)

                if monkeys_to_send is not None:
                    await ctx.send_msgs([{
                        "cmd": "LocationChecks",
                        "locations": list(x for x in monkeys_to_send)
                    }])

            # Check for Coins
            if gameState != RAM.gameState["LevelSelect"]:
                # If the previous address is empty it means you are too far, go back once
                # Happens in case of save-states or loading a previous save file that did not collect the same amount of coins
                coins_to_send = set()
                if (previousCoinStateRoom == 0xFF or previousCoinStateRoom == 0x00) and (
                        self.currentCoinAddress > RAM.startingCoinAddress):
                    self.currentCoinAddress -= 2
                # Check for new coins from current coin address
                if currentCoinStateRoom != 0xFF and currentCoinStateRoom != 0x00:
                    coins_to_send.add(int(currentCoinStateRoom + self.offset + 300))
                    await ctx.send_msgs([{
                        "cmd": "LocationChecks",
                        "locations": list(x for x in coins_to_send)
                    }])
                    self.currentCoinAddress += 2

            # Check for level bosses
            if gameState == RAM.gameState["InLevel"] and (localcondition) and (currentRoom in bossRooms):
                bossaddrs = RAM.bossListLocal[currentRoom]
                key_list = list(bossaddrs.keys())
                val_list = list(bossaddrs.values())
                addresses = []

                for val in val_list:
                    tuple1 = (val, 1, "MainRAM")
                    addresses.append(tuple1)

                bossesList = await bizhawk.read(ctx.bizhawk_ctx, addresses)
                bosses_to_send = set()

                for i in range(len(bossesList)):
                    # For TVT boss, check TVT_BossPhase, if it's 3 the fight is ongoing
                    if (currentRoom == 68):
                        if (TVT_BossPhase == 3 and int.from_bytes(bossesList[i], byteorder='little') == 0x00):
                            bosses_to_send.add(key_list[i] + self.offset)
                    elif (currentRoom == 70):
                        if (gameRunning == 1 and int.from_bytes(bossesList[i], byteorder='little') == 0x00):
                            bosses_to_send.add(key_list[i] + self.offset)
                            MM_Jake_Defeated = 1
                    elif (currentRoom == 71):
                        if int.from_bytes(bossesList[i], byteorder='little') == 0x00:
                            bosses_to_send.add(key_list[i] + self.offset)
                            MM_Professor_Rescued = 1
                    else:
                        if int.from_bytes(bossesList[i], byteorder='little') == 0x00:
                            bosses_to_send.add(key_list[i] + self.offset)

                if bosses_to_send is not None and bosses_to_send != set():
                    await ctx.send_msgs([{
                        "cmd": "LocationChecks",
                        "locations": list(x for x in bosses_to_send)
                    }])

            # Check for Mailboxes
            if (localcondition) and (currentRoom in mailboxesRooms):
                mailboxesaddrs = RAM.mailboxListLocal[currentRoom]
                boolGotMail = (gotMail == 0x02)
                key_list = list(mailboxesaddrs.keys())
                val_list = list(mailboxesaddrs.values())

                mail_to_send = set()
                # Rearange the array if there is 2 indexes for the same mailbox

                for i in range(len(val_list)):
                    strVal = str(val_list[i])
                    if strVal.__contains__("{"):
                        strVal = strVal.replace("{", "").replace("}", "")
                        strVal = strVal.split(",")
                        for j in range(len(strVal)):
                            key_list.append(key_list[i])
                            val_list.append(int(strVal[j]))
                        val_list.pop(i)
                        key_list.pop(i)
                for i in range(len(val_list)):
                    if val_list[i] == mailboxID and boolGotMail:
                        mail_to_send.add(key_list[i] + self.offset)

                if mail_to_send is not None and mail_to_send != set():
                    await ctx.send_msgs([{
                        "cmd": "LocationChecks",
                        "locations": list(x for x in mail_to_send)
                    }])

            # Check for victory conditions
            specter1Condition = (currentRoom == 86 and S1_P2_State == 1 and S1_P2_Life == 0)
            specter2Condition = (currentRoom == 87 and S2_isCaptured == 1)
            if RAM.gameState["InLevel"] == gameState and specter1Condition:
                await ctx.send_msgs([{
                    "cmd": "LocationChecks",
                    "locations": list(x for x in [self.offset + 205])
                }])

            if RAM.gameState["InLevel"] == gameState and specter2Condition:
                await ctx.send_msgs([{
                    "cmd": "LocationChecks",
                    "locations": list(x for x in [self.offset + 206])
                }])

            # Write Array

            # Training Room, set to 0xFF to mark as complete
            # Training Room Unlock state checkup : Set to 0x00000000 to prevent all buttons from working
            # Gadgets unlocked
            # Required apes (to match hundo)
            writes = [
                (RAM.trainingRoomProgressAddress, 0xFF.to_bytes(1, "little"), "MainRAM"),
                (RAM.unlockedGadgetsAddress, gadgetStateFromServer.to_bytes(2, "little"), "MainRAM"),
                (RAM.requiredApesAddress, localhundoCount.to_bytes(1, "little"), "MainRAM"),
            ]

            # Training Room Unlock state:
            # Due to a Bug with Gadget Training, will lock the gadget training ONLY when going into the room
            if (transitionPhase == 0x06 and NearbyRoom == 90) or currentRoom == 90:
                writes += [(RAM.GadgetTrainingsUnlockAddress, 0x00000000.to_bytes(4, "little"), "MainRAM")]
            else:
                writes += [(RAM.GadgetTrainingsUnlockAddress, 0x8C63FDCC.to_bytes(4, "little"), "MainRAM")]

            # Kickout Prevention
            # Now prevents getting kicked out of a boss level by catching a monkey while the boss is defeated
            # Prevent kickout if option is on (Only in levels)

            if self.preventKickOut == 1:
                #print(currentRoom)

                #If in level, make the "localLevelState" as "
                if gameState in (RAM.gameState["InLevel"],RAM.gameState["InLevelTT"]):
                    if currentRoom == 48:
                        if CrC_BossPhase == 4 and CrC_BossLife == 0x00:
                            writes += [(RAM.CrC_BossPhaseAddress, 0x05.to_bytes(1, "little"), "MainRAM")]
                            #writes += [(RAM.CrC_DoorVisual, 0xF8.to_bytes(1, "little"), "MainRAM")]
                            #writes += [(RAM.CrC_DoorHitBox, 0xF8.to_bytes(1, "little"), "MainRAM")]
                    if currentRoom == 68:
                        if TVT_BossPhase == 4 and TVT_BossLife == 0x00:
                            writes += [(RAM.TVT_BossPhase, 0x05.to_bytes(1, "little"), "MainRAM")]

                    # Prevents Kickout if it is not already prevented
                    if kickoutofLevel != 0:
                        writes += [(RAM.kickoutofLevelAddress, 0x00000000.to_bytes(4, "little"), "MainRAM")]
                        writes += [(RAM.kickoutofLevelAddress2, 0x00000000.to_bytes(4, "little"), "MainRAM")]
                    if localLevelState != 0x03:
                        writes += [(RAM.localLevelState, 0x03.to_bytes(1, "little"), "MainRAM")]
                else:
                    # Stops preventing Kickout outside of the Levels,since it could cause crashes
                    if kickoutofLevel == 0:
                        writes += [(RAM.kickoutofLevelAddress, 0x84830188.to_bytes(4, "little"), "MainRAM")]
                        writes += [(RAM.kickoutofLevelAddress2, 0x24020001.to_bytes(4, "little"), "MainRAM")]
            elif self.preventKickOut == 0:
                # Ensure you always get kicked out when catching the last monkey,to be consistent
                if kickoutofLevel == 0:
                    writes += [(RAM.kickoutofLevelAddress, 0x84830188.to_bytes(4, "little"), "MainRAM")]
                    writes += [(RAM.kickoutofLevelAddress2, 0x24020001.to_bytes(4, "little"), "MainRAM")]
                if localLevelState != 0x00:
                    writes += [(RAM.localLevelState, 0x00.to_bytes(1, "little"), "MainRAM")]

            # Check for Jake Victory
            if currentRoom == 19 and gameState == RAM.gameState["JakeCleared"] and jakeVictory == 0x2:
                coins = set()
                coins.add(295 + self.offset)
                coins.add(296 + self.offset)
                coins.add(297 + self.offset)
                coins.add(298 + self.offset)
                coins.add(299 + self.offset)
                await ctx.send_msgs([{
                    "cmd": "LocationChecks",
                    "locations": list(x for x in coins)
                }])
            elif currentRoom == 36 and gameState == RAM.gameState["JakeCleared"] and jakeVictory == 0x2:
                coins = set()
                coins.add(290 + self.offset)
                coins.add(291 + self.offset)
                coins.add(292 + self.offset)
                coins.add(293 + self.offset)
                coins.add(294 + self.offset)
                await ctx.send_msgs([{
                    "cmd": "LocationChecks",
                    "locations": list(x for x in coins)
                }])

            # ======== Trap Handling =========
            # For Traps.
            currentGadgets = await self.check_gadgets(ctx, gadgetStateFromServer)
            Trap_Reads = [gameState, gotMail, spikeState2, menuState, menuState2, currentGadgets,currentRoom]
            await self.traps_handling(ctx, Trap_Reads)
            # ================================

            # ======= Credits skipping =======
            # Credits skipping function for S1 and S2
            Credits_Reads = [currentRoom, gameState, S1_Cutscene_Redirection, S2_Cutscene_Redirection]
            await self.Credits_handling(ctx, Credits_Reads)
            # ================================

            # ======= MM Optimizations =======
            # Execute the code segment for MM Double Door and related optimizations
            MM_Reads = [currentRoom, currentLevel, gameState, NearbyRoom, transitionPhase, MM_Jake_Defeated, MM_Lobby_DoubleDoor, MM_Lobby_DoorDetection, MM_Lobby_DoubleDoor_Open, MM_Jake_DefeatedAddress, MM_Natalie_RescuedAddress, MM_Natalie_Rescued, MM_Natalie_Rescued_Local, MM_Professor_Rescued, S1_P1_FightTrigger]
            await self.MM_Optimizations(ctx, MM_Reads)
            # ================================

            # ====== Permanent Buttons =======
            # Execute the Buttons handling code segment
            Button_Reads = [currentRoom, gameState, DI_Button_Pressed, CrC_Water_ButtonPressed, CrC_Basement_ButtonPressed, TVT_Lobby_ButtonPressed, MM_MonkeyHead_ButtonPressed, MM_Painting_ButtonPressed, DI_Button_DoorVisual, CrC_Water_Door_Visual, CrC_Basement_DoorVisual1, TVT_Lobby_Water_Hitbox, MM_MonkeyHead_Door, MM_Painting_Visual, DR_Block_Pushed, transitionPhase]
            await self.permanent_buttons_handling(ctx, Button_Reads)
            # ================================

            localLampsUpdate = {20: CBLampState, 53: CPLampState, 79: MMLampState}
            globalLampsUpdate = {26: DILampState, 46: CrCLampState, 57: SFLampState, 65: TVTLobbyLampState,66: TVTTankLampState}

            # ========= Lamp Unlocks =========
            # Tables for Lamp updates
            # Execute the Lamp unlocking code segment
            Lamps_Reads = [gameState, currentRoom, NearbyRoom, localLampsUpdate, globalLampsUpdate, transitionPhase]
            await self.lamps_unlocks_handling(ctx, Lamps_Reads)
            # ================================

            # ========== Water Net ===========
            # Swim/Dive Prevention code
            WN_Reads = [gameState, waternetState, gameRunning, spikeState2, swim_oxygenLevel, cookies, isUnderwater, watercatchState]
            await self.water_net_handling(ctx, WN_Reads)
            # ================================

            # ====== Gadgets handling ========
            # For checking which gadgets should be equipped
            # Also apply Magic Punch visual correction
            Gadgets_Reads = [currentLevel, currentRoom, heldGadget, gadgetStateFromServer, crossGadget, squareGadget, circleGadget, triangleGadget, menuState, menuState2, punchVisualAddress, gameState, currentGadgets]
            await self.gadgets_handler(ctx, Gadgets_Reads, Temp_SA_Completed, Temp_GA_Completed)
            # ================================

            # == Level Select Optimization ===
            # Execute the Level Select optimization code segment
            LSO_Reads = [gameState, CoinTable, TempCoinTable, SA_Completed, Temp_SA_Completed, GA_Completed, Temp_GA_Completed, LS_currentLevel, LS_currentWorld, worldIsScrollingRight]
            await self.level_select_optimization(ctx, LSO_Reads)
            # ================================

            if gameState == RAM.gameState["LevelSelect"]:
                writes += [(RAM.localApeStartAddress, 0x0.to_bytes(8, "little"), "MainRAM")]
                # Update level (and potentially era) names.
                bytestowrite = ctx.slot_data["levelnames"]
                # This is a bit of a "magic number" right now. Trying to get the length didn't work.
                # Trying to write all the bytes at once also didn't work.
                for x in range(0, 308):
                    writes += [(RAM.startOfLevelNames + x, bytestowrite[x].to_bytes(1, "little"), "MainRAM")]

            # Reroute the player to the correct level. Technically only needed for entrance shuffle, vanilla entrances are just a special case of entrance shuffle so this works perfectly fine for that case, too.
            if gameState == RAM.gameState["LevelIntro"] or gameState == RAM.gameState["LevelIntroTT"]:
                # print("In level intro state.")
                # Pull the order of first rooms from slot data. This is a List sorted by the order of entrances in the level select - so the first value is the room being entered from Fossil Field.
                firstroomids = ctx.slot_data["firstrooms"]
                # Match these room ids to the internal identifiers - 11, 12, 13, 21, ... 83, 91, 92
                levelidtofirstroom = dict(zip(RAM.levelAddresses.keys(), firstroomids))
                # Use Selected World (0-9) and Selected Level (0-2) to determine the selected level.
                chosenLevel = 10 * status_currentWorld + status_currentLevel + 11
                # Peak Point Matrix doesn't follow the pattern, so manually override if it's that.
                if chosenLevel > 100:
                    chosenLevel = 92
                targetRoom = levelidtofirstroom.get(chosenLevel)
                # Actually send Spike to the desired level!
                writes += [(RAM.currentRoomIdAddress, targetRoom.to_bytes(1, "little"), "MainRAM")]

            # Unlock levels
            writes += self.unlockLevels(ctx, monkeylevelcounts, gameState, hundoMonkeysCount, ctx.slot_data["reqkeys"], ctx.slot_data["newpositions"], Temp_SA_Completed, Temp_GA_Completed)

            # ===== Text Replacements ======
            # Replace text Time Station mailbox here.
            # ==============================
            if currentRoom == 88 and gotMail == 0x02 and mailboxID == 0x71:
                mailboxtext = ""
                mailboxbytes = []

                mailboxbytes += text_to_bytes("World settings")
                mailboxbytes += [13] # New line

                # Add goal to mailbox text
                if ctx.slot_data["goal"] == GoalOption.option_mm or ctx.slot_data["goal"] == GoalOption.option_mmtoken:
                    mailboxtext = "Goal: Specter 1"
                elif ctx.slot_data["goal"] == GoalOption.option_ppm or ctx.slot_data["goal"] == GoalOption.option_ppmtoken:
                    mailboxtext = "Goal: Specter 2"
                else:
                    mailboxtext = "Goal: Token Hunt"
                mailboxbytes += text_to_bytes(mailboxtext)
                mailboxbytes += [13]

                # Add token information to mailbox text
                if ctx.slot_data["goal"] == GoalOption.option_mmtoken or ctx.slot_data["goal"] == GoalOption.option_ppmtoken or ctx.slot_data["goal"] == GoalOption.option_tokenhunt:
                    mailboxbytes += text_to_bytes("You need")
                    mailboxbytes += [13]
                    reqtokens = min(ctx.slot_data["requiredtokens"], ctx.slot_data["totaltokens"])
                    tottokens = max(ctx.slot_data["requiredtokens"], ctx.slot_data["totaltokens"])
                    mailboxbytes += text_to_bytes(str(reqtokens) + "/" + str(tottokens) + " tokens.")
                    mailboxbytes += [13]
                    mailboxbytes += [13]
                    mailboxbytes += text_to_bytes("You now have")
                    mailboxbytes += [13]
                    # Grammar handling
                    if self.tokencount != 1:
                        mailboxbytes += text_to_bytes(str(self.tokencount) + " tokens.")
                    else:
                        mailboxbytes += text_to_bytes(str(self.tokencount) + " token.")
                else:
                    mailboxbytes += [13]
                    mailboxbytes += text_to_bytes("There are no token")
                    mailboxbytes += [13]
                    mailboxbytes += text_to_bytes("requirements for")
                    mailboxbytes += [13]
                    mailboxbytes += text_to_bytes("this world.")

                # Pad the text with zeroes to account for the fixed length first page
                while len(mailboxbytes) < 79:
                    mailboxbytes += [0]

                # Next page
                mailboxbytes += [13]
                mailboxbytes += [13]
                mailboxbytes += [15]

                # Add difficulty and trick information to mailbox text
                if ctx.slot_data["logic"] == LogicOption.option_normal:
                    mailboxtext = "Difficulty: Normal"
                elif ctx.slot_data["logic"] == LogicOption.option_hard:
                    mailboxtext = "Difficulty: Hard"
                else:
                    mailboxtext = "Difficulty: Expert"
                mailboxbytes += text_to_bytes(mailboxtext)
                mailboxbytes += [13]

                if ctx.slot_data["infinitejump"] == InfiniteJumpOption.option_false:
                    mailboxtext = "Infinite Jump: Off"
                else:
                    mailboxtext = "Infinite Jump: On"
                mailboxbytes += text_to_bytes(mailboxtext)
                mailboxbytes += [13]

                if ctx.slot_data["superflyer"] == SuperFlyerOption.option_false:
                    mailboxtext = "Super Flyer: Off"
                else:
                    mailboxtext = "Super Flyer: On"
                mailboxbytes += text_to_bytes(mailboxtext)
                mailboxbytes += [13]

                # Add lamp shuffle information to mailbox text
                if ctx.slot_data["lamp"] == LampOption.option_false:
                    mailboxtext = "Lamp Shuffle: Off"
                else:
                    mailboxtext = "Lamp Shuffle: On"
                mailboxbytes += text_to_bytes(mailboxtext)
                mailboxbytes += [13]

                # Add Water Net information to mailbox text
                mailboxbytes += text_to_bytes("Water Net Status:")
                mailboxbytes += [13]
                mailboxbytes += text_to_bytes("Swim ")
                if waternetState == 0: # Can't swim
                    mailboxbytes += [10] # X button icon
                    mailboxbytes += [4]
                else:
                    mailboxbytes += [10] # O button icon
                    mailboxbytes += [1]
                mailboxbytes += text_to_bytes(" Dive ")
                if waternetState == 2: # Can dive
                    mailboxbytes += [10]
                    mailboxbytes += [1]
                else:
                    mailboxbytes += [10]
                    mailboxbytes += [4]
                mailboxbytes += [13]
                mailboxbytes += text_to_bytes("Catch ")
                if watercatchState == 0: # Can't water catch
                    mailboxbytes += [10]
                    mailboxbytes += [4]
                else:
                    mailboxbytes += [10]
                    mailboxbytes += [1]

                # Next page
                mailboxbytes += [13]
                mailboxbytes += [13]
                mailboxbytes += [15]

                # Add coin and mailbox shuffle information to mailbox text
                if ctx.slot_data["coin"] == CoinOption.option_false:
                    mailboxtext = "Coins: Off"
                else:
                    mailboxtext = "Coins: On"
                mailboxbytes += text_to_bytes(mailboxtext)
                mailboxbytes += [13]

                if ctx.slot_data["mailbox"] == MailboxOption.option_false:
                    mailboxtext = "Mailboxes: Off"
                else:
                    mailboxtext = "Mailboxes: On"
                mailboxbytes += text_to_bytes(mailboxtext)
                mailboxbytes += [13]

                # Add world key information to mailbox text
                if ctx.slot_data["unlocksperkey"] == KeyOption.option_none:
                    mailboxbytes += [13]
                    mailboxbytes += text_to_bytes("There are no")
                    mailboxbytes += [13]
                    mailboxbytes += text_to_bytes("World Keys in")
                    mailboxbytes += [13]
                    mailboxbytes += text_to_bytes("this world.")
                    mailboxbytes += [13]
                else:
                    mailboxbytes += text_to_bytes("Keys unlock")
                    mailboxbytes += [13]
                    if ctx.slot_data["unlocksperkey"] == KeyOption.option_world:
                        mailboxtext = "one world each."
                    elif ctx.slot_data["unlocksperkey"] == KeyOption.option_level:
                        mailboxtext = "one level each."
                    else:
                        mailboxtext = "two levels each."
                    mailboxbytes += text_to_bytes(mailboxtext)
                    mailboxbytes += [13]
                    # Grammar handling
                    if ctx.slot_data["extrakeys"] != 1:
                        mailboxbytes += text_to_bytes("There are " + str(ctx.slot_data["extrakeys"]))
                        mailboxbytes += [13]
                        mailboxbytes += text_to_bytes("extra World Keys.")
                    else:
                        mailboxbytes += text_to_bytes("There is " + str(ctx.slot_data["extrakeys"]))
                        mailboxbytes += [13]
                        mailboxbytes += text_to_bytes("extra World Key.")
                    mailboxbytes += [13]
                    if self.worldkeycount != 1:
                        mailboxbytes += text_to_bytes("You have " + str(self.worldkeycount) + " keys.")
                    else:
                        mailboxbytes += text_to_bytes("You have " + str(self.worldkeycount) + " key.")

                # Next page
                mailboxbytes += [13]
                mailboxbytes += [13]
                mailboxbytes += [15]

                # Add entrance shuffle information to mailbox text
                if ctx.slot_data["entrance"] == EntranceOption.option_off:
                    mailboxtext = "Entrance: Off"
                elif ctx.slot_data["entrance"] == EntranceOption.option_on:
                    mailboxtext = "Entrance: On"
                else:
                    mailboxtext = "Entrance: Lock MM"
                mailboxbytes += text_to_bytes(mailboxtext)
                mailboxbytes += [13]
                # TODO: Door shuffle status goes here
                mailboxbytes += [13]
                
                # Add door and lamp statuses to mailbox text
                mailboxbytes += text_to_bytes("MM Double Door: ")
                if MM_Lobby_DoubleDoor == 0: # Don't have item
                    mailboxbytes += [10] # X button icon
                    mailboxbytes += [4]
                else:
                    mailboxbytes += [10] # O button icon
                    mailboxbytes += [1]
                mailboxbytes += [13]
                if ctx.slot_data["lamp"] == LampOption.option_true:
                    mailboxbytes += text_to_bytes("          Lamps")
                    mailboxbytes += [13]
                    mailboxbytes += text_to_bytes("CB: ")
                    if CBLampState == 0: # Don't have item
                        mailboxbytes += [10] # X button icon
                        mailboxbytes += [4]
                    else:
                        mailboxbytes += [10] # O button icon
                        mailboxbytes += [1]
                    mailboxbytes += text_to_bytes(" DI: ")
                    if DILampState == 0: # Don't have item
                        mailboxbytes += [10] # X button icon
                        mailboxbytes += [4]
                    else:
                        mailboxbytes += [10] # O button icon
                        mailboxbytes += [1]
                    mailboxbytes += text_to_bytes(" CC: ")
                    if CrCLampState == 0: # Don't have item
                        mailboxbytes += [10] # X button icon
                        mailboxbytes += [4]
                    else:
                        mailboxbytes += [10] # O button icon
                        mailboxbytes += [1]
                    mailboxbytes += [13]
                    mailboxbytes += text_to_bytes("CP: ")
                    if CPLampState == 0: # Don't have item
                        mailboxbytes += [10] # X button icon
                        mailboxbytes += [4]
                    else:
                        mailboxbytes += [10] # O button icon
                        mailboxbytes += [1]
                    mailboxbytes += text_to_bytes(" SF: ")
                    if SFLampState == 0: # Don't have item
                        mailboxbytes += [10] # X button icon
                        mailboxbytes += [4]
                    else:
                        mailboxbytes += [10] # O button icon
                        mailboxbytes += [1]
                    mailboxbytes += text_to_bytes(" TV: ")
                    if TVTLobbyLampState == 0: # Don't have item
                        mailboxbytes += [10] # X button icon
                        mailboxbytes += [4]
                    else:
                        mailboxbytes += [10] # O button icon
                        mailboxbytes += [1]
                    mailboxbytes += [13]
                    mailboxbytes += text_to_bytes("TV: ")
                    if TVTTankLampState == 0: # Don't have item
                        mailboxbytes += [10] # X button icon
                        mailboxbytes += [4]
                    else:
                        mailboxbytes += [10] # O button icon
                        mailboxbytes += [1]
                    mailboxbytes += text_to_bytes(" MM: ")
                    if MMLampState == 0: # Don't have item
                        mailboxbytes += [10] # X button icon
                        mailboxbytes += [4]
                    else:
                        mailboxbytes += [10] # O button icon
                        mailboxbytes += [1]
            
                # End mailbox text
                mailboxbytes += [13]
                # Pad the text with zeroes to overwrite all pre-existing text
                while len(mailboxbytes) < 600:
                    mailboxbytes += [0]

                for x in range(0, 600):
                    writes += [(RAM.timeStationMailboxStart + x, mailboxbytes[x].to_bytes(1, "little"), "MainRAM")]

            await bizhawk.write(ctx.bizhawk_ctx, writes)
            await bizhawk.write(ctx.bizhawk_ctx, itemsWrites)

            self.levelglobal = currentLevel
            # For future room Auto-Tab in tracker
            if self.roomglobal != currentRoom:
                self.roomglobal = currentRoom
                await ctx.send_msgs(
                    [
                        {
                            "cmd": "Set",
                            "key": f"AE_room_{ctx.team}_{ctx.slot}",
                            "default": 0,
                            "want_reply": False,
                            "operations": [{"operation": "replace", "value": currentRoom}],
                        }
                    ]
                )

        except bizhawk.RequestFailedError:
            # Exit handler and return to main loop to reconnect
            pass


    async def gadgets_handler(self, ctx: "BizHawkClientContext", Gadgets_Reads, SAcomplete, GAcomplete):
        currentLevel = Gadgets_Reads[0]
        currentRoom = Gadgets_Reads[1]
        heldGadget = Gadgets_Reads[2]
        gadgetStateFromServer = Gadgets_Reads[3]
        crossGadget = Gadgets_Reads[4]
        squareGadget = Gadgets_Reads[5]
        circleGadget = Gadgets_Reads[6]
        triangleGadget = Gadgets_Reads[7]
        menuState = Gadgets_Reads[8]
        menuState2 = Gadgets_Reads[9]
        punchVisualAddress = Gadgets_Reads[10]
        gameState = Gadgets_Reads[11]
        currentGadgets = Gadgets_Reads[12]
        # print(currentGadgets)
        gadgets_Writes = []
        punch_Guards = []
        punch_Writes = []

        if gameState == RAM.gameState['InLevel']:

            # Add radar to races if the level has been cleared and the player has radar, to allow radaring Jake
            if (currentLevel == 0x07):
                if (gadgetStateFromServer & 4 != 0) and (SAcomplete == 25):
                    gadgets_Writes += [(RAM.triangleGadgetAddress, 0x02.to_bytes(1, "little"), "MainRAM")]
            elif (currentLevel == 0x0E):
                if (gadgetStateFromServer & 4 != 0) and (GAcomplete == 25):
                    gadgets_Writes += [(RAM.triangleGadgetAddress, 0x02.to_bytes(1, "little"), "MainRAM")]
                # If the current level is Gladiator Attack, the Sky Flyer is currently equipped, and the player does not have the Sky Flyer: unequip it
                if (heldGadget == 6) and (gadgetStateFromServer & 64 == 0):
                    gadgets_Writes += [(RAM.crossGadgetAddress, 0xFF.to_bytes(1, "little"), "MainRAM")]
                    gadgets_Writes += [(RAM.heldGadgetAddress, 0xFF.to_bytes(1, "little"), "MainRAM")]
        # Unequip the Time Net if it was shuffled. Note that just checking the Net option is not sufficient to known if the net was actually shuffled - we need to ensure there are locations in this world that don't require net to be sure.
        if ctx.slot_data["shufflenet"] == ShuffleNetOption.option_true and (
                ctx.slot_data["coin"] == CoinOption.option_true or ctx.slot_data[
            "mailbox"] == MailboxOption.option_true):
            if (crossGadget == 1) and (gadgetStateFromServer & 2 == 0):
                gadgets_Writes += [(RAM.crossGadgetAddress, 0xFF.to_bytes(1, "little"), "MainRAM")]

        # Equip the selected starting gadget onto the triangle button. Stun Club is the default and doesn't need changing. Additionally, in the "none" case, switch the selection to the Time Net if it wasn't shuffled.
        if ((heldGadget == 0) and (gadgetStateFromServer % 2 == 0)):
            if ctx.slot_data["gadget"] == GadgetOption.option_radar:
                gadgets_Writes += [(RAM.triangleGadgetAddress, 0x02.to_bytes(1, "little"), "MainRAM")]
                gadgets_Writes += [(RAM.heldGadgetAddress, 0x02.to_bytes(1, "little"), "MainRAM")]
                triangleGadget = 0x02
            elif ctx.slot_data["gadget"] == GadgetOption.option_sling:
                gadgets_Writes += [(RAM.triangleGadgetAddress, 0x03.to_bytes(1, "little"), "MainRAM")]
                gadgets_Writes += [(RAM.heldGadgetAddress, 0x03.to_bytes(1, "little"), "MainRAM")]
                triangleGadget = 0x03
            elif ctx.slot_data["gadget"] == GadgetOption.option_hoop:
                gadgets_Writes += [(RAM.triangleGadgetAddress, 0x04.to_bytes(1, "little"), "MainRAM")]
                gadgets_Writes += [(RAM.heldGadgetAddress, 0x04.to_bytes(1, "little"), "MainRAM")]
                triangleGadget = 0x04
            elif ctx.slot_data["gadget"] == GadgetOption.option_flyer:
                gadgets_Writes += [(RAM.triangleGadgetAddress, 0x06.to_bytes(1, "little"), "MainRAM")]
                gadgets_Writes += [(RAM.heldGadgetAddress, 0x06.to_bytes(1, "little"), "MainRAM")]
                triangleGadget = 0x06
            elif ctx.slot_data["gadget"] == GadgetOption.option_car:
                gadgets_Writes += [(RAM.triangleGadgetAddress, 0x07.to_bytes(1, "little"), "MainRAM")]
                gadgets_Writes += [(RAM.heldGadgetAddress, 0x07.to_bytes(1, "little"), "MainRAM")]
                triangleGadget = 0x07
            elif ctx.slot_data["gadget"] == GadgetOption.option_punch:
                gadgets_Writes += [(RAM.triangleGadgetAddress, 0x05.to_bytes(1, "little"), "MainRAM")]
                gadgets_Writes += [(RAM.heldGadgetAddress, 0x05.to_bytes(1, "little"), "MainRAM")]
                triangleGadget = 0x05
            elif ctx.slot_data["gadget"] == GadgetOption.option_none or ctx.slot_data["gadget"] == GadgetOption.option_waternet:
                gadgets_Writes += [(RAM.triangleGadgetAddress, 0xFF.to_bytes(1, "little"), "MainRAM")]
                if ctx.slot_data["shufflenet"] == ShuffleNetOption.option_true:
                    gadgets_Writes += [(RAM.heldGadgetAddress, 0xFF.to_bytes(1, "little"), "MainRAM")]
                elif ctx.slot_data["shufflenet"] == ShuffleNetOption.option_false:
                    gadgets_Writes += [(RAM.heldGadgetAddress, 0x01.to_bytes(1, "little"), "MainRAM")]
        await bizhawk.write(ctx.bizhawk_ctx, gadgets_Writes)

        # If Auto-Equip is on, still checks to exclude races from it
        if self.autoequip == 1 and (currentRoom != 19 and currentRoom != 36):
            if currentGadgets :
                boolCrossGadget = crossGadget  == 0xFF
                boolSquareGadget = squareGadget == 0xFF
                boolCircleGadget = circleGadget == 0xFF
                boolTriangleGadget = triangleGadget == 0xFF
                boolFreeSpace = boolCrossGadget or boolSquareGadget or boolCircleGadget or boolTriangleGadget
                boolNoGadgets = boolCrossGadget and boolSquareGadget and boolCircleGadget and boolTriangleGadget
                if boolFreeSpace:
                    for x in range(len(currentGadgets)):
                        gadget = gadgetsValues[currentGadgets[x]]
                        boolGadgetOnCross = crossGadget == gadget
                        boolGadgetOnSquare = squareGadget == gadget
                        boolGadgetOnCircle = circleGadget == gadget
                        boolGadgetOnTriangle = triangleGadget == gadget
                        boolGadgetAlreadyOn = boolGadgetOnCross or boolGadgetOnSquare or boolGadgetOnCircle or boolGadgetOnTriangle
                        if not boolGadgetAlreadyOn:
                            if boolCrossGadget:
                                crossGadget = gadget
                                gadgets_Writes += [(RAM.crossGadgetAddress, gadget.to_bytes(1, "little"), "MainRAM")]
                                if boolNoGadgets:
                                    gadgets_Writes += [(RAM.heldGadgetAddress, gadget.to_bytes(1, "little"), "MainRAM")]
                                    boolNoGadgets = False
                            elif boolSquareGadget:
                                squareGadget = gadget
                                gadgets_Writes += [(RAM.squareGadgetAddress, gadget.to_bytes(1, "little"), "MainRAM")]
                            elif boolCircleGadget:
                                circleGadget = gadget
                                gadgets_Writes += [(RAM.circleGadgetAddress, gadget.to_bytes(1, "little"), "MainRAM")]
                            elif boolTriangleGadget:
                                triangleGadget = gadget
                                gadgets_Writes += [(RAM.triangleGadgetAddress, gadget.to_bytes(1, "little"), "MainRAM")]

        # Punch Visual glitch in menu fix
        # Replace all values from 0x0E78C0 to 0x0E78DF to this:
        # 0010000000000000E00B00000000000000100000000000000000000000000000
        bytes_ToWrite: bytes = bytes.fromhex(
            "0010000000000000E00B00000000000000100000000000000000000000000000")

        if menuState == 0x00 and menuState2 == 0x01 and gameState != RAM.gameState['LevelSelect']:
            if ((gadgetStateFromServer & 32) == 32) and punchVisualAddress.to_bytes(32,"little") != bytes_ToWrite: # and self.replacePunch == True:
                # print(punchVisualAddress)
                # print(int.from_bytes(bytes_ToWrite))
                punch_Writes += [(RAM.punchVisualAddress, bytes_ToWrite, "MainRAM")]
                punch_Guards += [(RAM.menuStateAddress, 0x00.to_bytes(1,"little"), "MainRAM")]
                punch_Guards += [(RAM.menuState2Address, 0x01.to_bytes(1,"little"), "MainRAM")]
                # print("Replaced Punch visuals")
                # gadgets_Writes += [(RAM.unlockedGadgetsAddress, 0x24.to_bytes(1, "little"), "MainRAM")]
                await bizhawk.guarded_write(ctx.bizhawk_ctx, punch_Writes, punch_Guards)
        await bizhawk.write(ctx.bizhawk_ctx, gadgets_Writes)


    async def Credits_handling(self, ctx: "BizHawkClientContext", Credits_Reads) -> None:
        currentRoom = Credits_Reads[0]
        gameState = Credits_Reads[1]
        S1_Cutscene_Redirection = hex(Credits_Reads[2])
        S2_Cutscene_Redirection = hex(Credits_Reads[3])
        Credits_Writes = []

        # Does not execute the function if you not in a level (Or custscene of S1)
        if (gameState not in (RAM.gameState['InLevel'], RAM.gameState['InLevelTT'],RAM.gameState['Cutscene2'])):
            return None

        if gameState == RAM.gameState['Cutscene2']:
            if S1_Cutscene_Redirection != 0x2403000D:
                Credits_Writes += [(RAM.S1_Cutscene_Redirection, 0x2403000D.to_bytes(4, "little"), "MainRAM")]

        if currentRoom == 87:
            if S2_Cutscene_Redirection != 0x2403000D:
                Credits_Writes += [(RAM.S2_Cutscene_Redirection, 0x2403000D.to_bytes(4, "little"), "MainRAM")]
        await bizhawk.write(ctx.bizhawk_ctx, Credits_Writes)


    async def MM_Optimizations(self, ctx: "BizHawkClientContext", MM_Reads) -> None:
        currentRoom = MM_Reads[0]
        currentLevel = MM_Reads[1]
        gameState = MM_Reads[2]
        NearbyRoom = MM_Reads[3]
        transitionPhase = MM_Reads[4]
        MM_Jake_Defeated = MM_Reads[5]
        MM_Lobby_DoubleDoor = MM_Reads[6]
        MM_Lobby_DoorDetection = MM_Reads[7]
        MM_Lobby_DoubleDoor_Open = MM_Reads[8]
        MM_Jake_DefeatedAddress = MM_Reads[9]
        MM_Natalie_RescuedAddress = MM_Reads[10]
        MM_Natalie_Rescued = MM_Reads[11]
        MM_Natalie_Rescued_Local = MM_Reads[12]
        MM_Professor_Rescued = MM_Reads[13]
        S1_P1_FightTrigger = MM_Reads[14]

        MM_Writes = []
        SpecterLevels = (RAM.levels['Specter'], RAM.levels['S_Jake'], RAM.levels['S_Circus'], RAM.levels['S_Coaster'], RAM.levels['S_Western Land'], RAM.levels['S_Castle'])
        writes = []
        guards = []

        # Only do the MM_Optimizations IN Monkey Madness, else revert back to default behavior and do nothing else
        if currentLevel not in SpecterLevels or gameState == RAM.gameState['LevelSelect']:
            writes += [(RAM.MM_Lobby_DoorDetection, 0x8C820000.to_bytes(4, "little"), "MainRAM")]
            guards += [(RAM.MM_Lobby_DoorDetection, 0x8C800000.to_bytes(4, "little"), "MainRAM")]
            await bizhawk.guarded_write(ctx.bizhawk_ctx, writes, guards)
            return None
        # print("MM_Optimizations")

        if MM_Jake_Defeated == 1:
            MM_Writes += [(RAM.MM_Jake_DefeatedAddress, 0x05.to_bytes(1, "little"), "MainRAM")]
            MM_Writes += [(RAM.temp_MM_Jake_DefeatedAddress, 0x01.to_bytes(1, "little"), "MainRAM")]
        else:
            MM_Writes += [(RAM.MM_Jake_DefeatedAddress, 0x00.to_bytes(1, "little"), "MainRAM")]
            MM_Writes += [(RAM.temp_MM_Jake_DefeatedAddress, 0x00.to_bytes(1, "little"), "MainRAM")]

        if MM_Professor_Rescued == 1:
            MM_Writes += [(RAM.MM_Professor_RescuedAddress, 0x05.to_bytes(1, "little"), "MainRAM")]
            MM_Writes += [(RAM.temp_MM_Professor_RescuedAddress, 0x01.to_bytes(1, "little"), "MainRAM")]
        else:
            MM_Writes += [(RAM.MM_Professor_RescuedAddress, 0x00.to_bytes(1, "little"), "MainRAM")]
            MM_Writes += [(RAM.temp_MM_Professor_RescuedAddress, 0x00.to_bytes(1, "little"), "MainRAM")]

        if MM_Natalie_Rescued == 1:
            MM_Writes += [(RAM.MM_Natalie_RescuedAddress, 0x05.to_bytes(1, "little"), "MainRAM")]
            MM_Writes += [(RAM.temp_MM_Natalie_RescuedAddress, 0x01.to_bytes(1, "little"), "MainRAM")]
        else:
            MM_Writes += [(RAM.MM_Natalie_RescuedAddress, 0x00.to_bytes(1, "little"), "MainRAM")]
            MM_Writes += [(RAM.temp_MM_Natalie_RescuedAddress, 0x00.to_bytes(1, "little"), "MainRAM")]

        # Natalie's Rescue Coffin room detection (When in the room)
        if currentRoom == 76:
            if MM_Natalie_Rescued_Local == 0x01:
                MM_Writes += [(RAM.temp_MM_Natalie_RescuedAddress, 0x01.to_bytes(1, "little"), "MainRAM")]

        # Natalie's Cutscene reset (When transitioning to Haunted Mansion)
        if NearbyRoom == 75 and MM_Natalie_Rescued != 0x01 and transitionPhase == 0x06:
            MM_Writes += [(RAM.MM_Natalie_CutsceneState, 0x00.to_bytes(1, "little"), "MainRAM")]

        # When going into the MM_Lobby, disable the Door Detection
        if (NearbyRoom == 69 and transitionPhase == 0x06) or (currentRoom == 69 and transitionPhase != 0x06):
            # print("Next room == Lobby")
            if MM_Lobby_DoorDetection != 0x8C800000:
                MM_Writes += [(RAM.MM_Lobby_DoorDetection, 0x8C800000.to_bytes(4, "little"), "MainRAM")]
        elif (NearbyRoom != 69 and transitionPhase == 0x06):
            if MM_Lobby_DoorDetection != 0x8C820000:
                MM_Writes += [(RAM.MM_Lobby_DoorDetection, 0x8C820000.to_bytes(4, "little"), "MainRAM")]

        # Same detection address needed to check if Jake is supposed to spawn or not.
        # Put it back to "ON" when transitioning to the Go Karz room or Clown Room
        # if (NearbyRoom == 71) and transitionPhase == 0x06:
            # MM_Writes += [(RAM.MM_Jake_DefeatedAddress, 0x00.to_bytes(1, "little"), "MainRAM")]
            # print("Changed room Detection for Jake")

        # MM_Lobby door handling
        if currentRoom == 69 and transitionPhase != 0x06:
            # Open the Electric Door and remove the Hitbox blocking you to go to Go Karz room (Jake fight)
            MM_Writes += [(RAM.MM_Lobby_JakeDoorFenceAddress, 0x01.to_bytes(1, "little"), "MainRAM")]
            MM_Writes += [(RAM.MM_Lobby_JakeDoor_HitboxAddress, 0x80.to_bytes(1, "little"), "MainRAM")]
            MM_Writes += [(RAM.MM_Lobby_DoubleDoor_OpenAddress, 0x05.to_bytes(1, "little"), "MainRAM")]

            door_addresses = RAM.doors_addresses

            if currentRoom in door_addresses.keys():
                doorlist_keys = list(door_addresses[currentRoom].keys())
                doorlist_values = list(door_addresses[currentRoom].values())

                # print(doorlist_values)
                for x in range(len(doorlist_keys)):
                    Door_writes = []
                    Door_guards = [(RAM.currentRoomIdAddress, currentRoom.to_bytes(1, "little"), "MainRAM")]
                    # lamp_values2 = list(lamp_values[x].__str__().replace("[", "").replace("]", "").split(","))
                    door_values = list(doorlist_values[x])
                    # print(doorlist_values[x])
                    door_bytes = door_values[0]
                    door_openvalue = door_values[1].to_bytes(door_bytes, "little")
                    door_closedvalue = door_values[2].to_bytes(door_bytes, "little")
                    door_address = (doorlist_keys[x])
                    # print(door_address)
                    if MM_Lobby_DoubleDoor == 0:
                        # Close the door if opened
                        Door_writes += [(door_address, door_closedvalue, "MainRAM")]
                        Door_guards += [(door_address, door_openvalue, "MainRAM")]
                    else:
                        # Open the door if it's closed
                        Door_writes += [(door_address, door_openvalue, "MainRAM")]
                        Door_guards += [(door_address, door_closedvalue, "MainRAM")]

                    await bizhawk.guarded_write(ctx.bizhawk_ctx, Door_writes, Door_guards)

        # Prevent Specter 1 fight for Specter 1 token goal when not having enough tokens.
        token = self.tokencount
        if (NearbyRoom == 83 and transitionPhase == 0x06) or (currentRoom == 83 and transitionPhase != 0x06):
            # print("Current/Next Room is Specter 1 room")
            if ctx.slot_data["goal"] == GoalOption.option_mmtoken:
                # print("with the correct goal")
                if token < min(ctx.slot_data["requiredtokens"], ctx.slot_data["totaltokens"]):
                    # print("and insufficient tokens")
                    # MM_Writes += [(RAM.S1_P1_Life, 0x06.to_bytes(1, "little"), "MainRAM")]
                    # Prevent the fight
                    MM_Writes += [(RAM.S1_P1_FightTrigger, 0x0D.to_bytes(1, "little"), "MainRAM")]
                else:
                    # Allow the fight
                    if S1_P1_FightTrigger == 0x0D:
                        MM_Writes += [(RAM.S1_P1_FightTrigger, 0x00.to_bytes(1, "little"), "MainRAM")]

        await bizhawk.write(ctx.bizhawk_ctx, MM_Writes)


    async def permanent_buttons_handling(self, ctx: "BizHawkClientContext", Button_Reads) -> None:
        currentRoom = Button_Reads[0]
        gameState = Button_Reads[1]
        DI_Button_Pressed = Button_Reads[2]
        CrC_Water_ButtonPressed = Button_Reads[3]
        CrC_Basement_ButtonPressed = Button_Reads[4]
        TVT_Lobby_ButtonPressed = Button_Reads[5]
        MM_MonkeyHead_ButtonPressed = Button_Reads[6]
        MM_Painting_ButtonPressed = Button_Reads[7]
        DI_Button_DoorVisual = Button_Reads[8]
        CrC_Water_DoorVisual = Button_Reads[9]
        CrC_Basement_DoorVisual1 = Button_Reads[10]
        TVT_Lobby_Water_Hitbox = Button_Reads[11]
        MM_MonkeyHead_Door = Button_Reads[12]
        MM_Painting_Visual = Button_Reads[13]
        DR_Block_Pushed = Button_Reads[14]
        transitionPhase = Button_Reads[15]

        Button_Writes = []

        # Does not execute the function if you not in a level
        if (gameState not in (RAM.gameState['InLevel'],RAM.gameState['InLevelTT'])):
            return None

        # print("permanent_buttons_handling")
        # If CrC_ButtonRoom button is pressed,send the value "{Player}_CrCWaterButton" to the server's Datastorage
        # This behavior unlocks the door permanently after you press the button once.
        if currentRoom == 11 and transitionPhase != 6:
            if DR_Block_Pushed == 0x01:
                await ctx.send_msgs([{
                    "cmd": "Set",
                    # "key": str(ctx.player_names[ctx.slot]) + "_DIButton",
                    "key": f"AE_DR_Block_{ctx.team}_{ctx.slot}",
                    "default": 0,
                    "want_reply": False,
                    "operations": [{"operation": "replace", "value": 1}]
                }])

        if currentRoom == 28 and transitionPhase != 6:
            if DI_Button_Pressed == 0x01:
                if self.DIButton != 1:
                    await ctx.send_msgs([{
                        "cmd": "Set",
                        # "key": str(ctx.player_names[ctx.slot]) + "_DIButton",
                        "key": f"AE_DIButton_{ctx.team}_{ctx.slot}",
                        "default": 0,
                        "want_reply": False,
                        "operations": [{"operation": "replace", "value": 1}]
                    }])

        if currentRoom == 49 and transitionPhase != 6:
            if CrC_Water_ButtonPressed == 0x01:
                if self.CrCWaterButton != 1:
                    await ctx.send_msgs([{
                        "cmd": "Set",
                        # "key": str(ctx.player_names[ctx.slot]) + "_CrCWaterButton",
                        "key": f"AE_CrCWaterButton_{ctx.team}_{ctx.slot}",
                        "default": 0,
                        "want_reply": False,
                        "operations": [{"operation": "replace", "value": 1}]
                    }])

        # if currentRoom == 47:
        #     if CrC_Basement_ButtonPressed == 0x01:
        #         if self.CrCBasementButton != 1:
        #             await ctx.send_msgs([{
        #                 "cmd": "Set",
        #                 "key": str(ctx.player_names[ctx.slot]) + "_CrCBasementButton",
        #                 "default": 0,
        #                 "want_reply": False,
        #                 "operations": [{"operation": "replace", "value": 1}]
        #             }])

        if currentRoom == 65 and transitionPhase != 6:
            if TVT_Lobby_ButtonPressed == 0x01:
                if self.TVT_Lobby_Button != 1:
                    await ctx.send_msgs([{
                        "cmd": "Set",
                        # "key": str(ctx.player_names[ctx.slot]) + "_TVT_Lobby_Button",
                        "key": f"AE_TVT_Lobby_Button_{ctx.team}_{ctx.slot}",
                        "default": 0,
                        "want_reply": False,
                        "operations": [{"operation": "replace", "value": 1}]
                    }])

        # Detection of Interior Climb button press (MonkeyHead Room)
        if currentRoom == 84 and transitionPhase != 6:
            if MM_MonkeyHead_ButtonPressed == 0x01:
                if self.MM_MonkeyHead_Button != 1:
                    await ctx.send_msgs([{
                        "cmd": "Set",
                        "key": f"AE_MM_MonkeyHead_Button_{ctx.team}_{ctx.slot}",
                        #"key": str(ctx.player_names[ctx.slot]) + "_MM_MonkeyHead_Button",
                        "default": 0,
                        "want_reply": False,
                        "operations": [{"operation": "replace", "value": 1}]
                    }])

        # Detection of Painting button press (Outside Climb)
        if currentRoom == 82 and transitionPhase != 6:
            if MM_Painting_ButtonPressed == 0x01:
                if self.MM_Painting_Button != 1:
                    await ctx.send_msgs([{
                        "cmd": "Set",
                        "key": f"AE_MM_Painting_Button_{ctx.team}_{ctx.slot}",
                        #"key": str(ctx.player_names[ctx.slot]) + "_MM_Painting_Button",
                        "default": 0,
                        "want_reply": False,
                        "operations": [{"operation": "replace", "value": 1}]
                    }])

        # Dexter's Island Slide Room button unlock
        if currentRoom == 28 and transitionPhase != 6:
            if DI_Button_DoorVisual != 0x00:
                if self.DIButton != 1:
                    await ctx.send_msgs([{
                        "cmd": "Get",
                        "keys": [f"AE_DIButton_{ctx.team}_{ctx.slot}"]
                    }])
                if self.DIButton == 1:
                    Button_Writes += [(RAM.DI_Button_Pressed, 0x01.to_bytes(1, "little"), "MainRAM")]
                    Button_Writes += [(RAM.DI_Button_DoorVisual, 0x00.to_bytes(1, "little"), "MainRAM")]
                    Button_Writes += [(RAM.DI_Button_DoorHitBox, 0xDC.to_bytes(1, "little"), "MainRAM")]
                    Button_Writes += [(RAM.DI_Button_Visual1, 0x80162250.to_bytes(4, "little"), "MainRAM")]
                    Button_Writes += [(RAM.DI_Button_Visual2, 0x80162268.to_bytes(4, "little"), "MainRAM")]
                    Button_Writes += [(RAM.DI_Button_Visual3, 0x80162390.to_bytes(4, "little"), "MainRAM")]
                    Button_Writes += [(RAM.DI_Button_Visual4, 0x80162288.to_bytes(4, "little"), "MainRAM")]

        # Crumbling Castle Water Room door unlock check
        if currentRoom == 45 and transitionPhase != 6:
            if CrC_Water_DoorVisual != 0x00:
                if self.CrCWaterButton != 1:
                    await ctx.send_msgs([{
                        "cmd": "Get",
                        "keys": [f"AE_CrCWaterButton_{ctx.team}_{ctx.slot}"]
                    }])
                if self.CrCWaterButton == 1:
                    Button_Writes += [(RAM.CrC_Water_DoorVisual, 0x00.to_bytes(1, "little"), "MainRAM")]
                    Button_Writes += [(RAM.TR4_TransitionEnabled, 0x00.to_bytes(1, "little"), "MainRAM")]

        # Crumbling Castle Basement Room door unlock check
        # if currentRoom == 47:
        #     if CrC_Basement_DoorVisual1 != 0x00:
        #         if self.CrCBasementButton != 1:
        #             await ctx.send_msgs([{
        #                 "cmd": "Get",
        #                 "keys": [str(ctx.player_names[ctx.slot]) + "_CrCBasementButton"]
        #             }])
        #         if self.CrCBasementButton == 1:
        #             Button_Writes += [(RAM.CrC_Basement_DoorHitBox1, 0xF200F808.to_bytes(4, "little"), "MainRAM")]
        #             Button_Writes += [(RAM.CrC_Basement_DoorHitBox2, 0x0008FB00.to_bytes(4, "little"), "MainRAM")]
        #             Button_Writes += [(RAM.CrC_Basement_DoorHitBox3, 0x01000400.to_bytes(4, "little"), "MainRAM")]
        #             Button_Writes += [(RAM.CrC_Basement_DoorVisual1, 0x00.to_bytes(1, "little"), "MainRAM")]
        #             Button_Writes += [(RAM.CrC_Basement_DoorVisual2, 0xF0.to_bytes(1, "little"), "MainRAM")]
        #             Button_Writes += [(RAM.CrC_Basement_ButtonVisual1, 0x80178ADC.to_bytes(4, "little"), "MainRAM")]
        #             Button_Writes += [(RAM.CrC_Basement_ButtonVisual2, 0x80178AF4.to_bytes(4, "little"), "MainRAM")]
        #             Button_Writes += [(RAM.CrC_Basement_ButtonVisual3, 0x80178C14.to_bytes(4, "little"), "MainRAM")]
        #             Button_Writes += [(RAM.CrC_Basement_ButtonVisual4, 0x80178B0C.to_bytes(4, "little"), "MainRAM")]

        # TV Tower water draining check
        if currentRoom == 65 and transitionPhase != 6:
            if TVT_Lobby_Water_Hitbox != 0x00:
                if self.TVT_Lobby_Button != 1:
                    await ctx.send_msgs([{
                        "cmd": "Get",
                        "keys": [f"AE_TVT_Lobby_Button_{ctx.team}_{ctx.slot}"]
                    }])
                if self.TVT_Lobby_Button == 1:
                    Button_Writes += [(RAM.TVT_Lobby_Water_HitBox, 0x00.to_bytes(1, "little"), "MainRAM")]
                    Button_Writes += [(RAM.TVT_Lobby_Water_DoorHitbox1, 0x80.to_bytes(1, "little"), "MainRAM")]
                    Button_Writes += [(RAM.TVT_Lobby_Water_DoorHitbox2, 0x80.to_bytes(1, "little"), "MainRAM")]
                    Button_Writes += [(RAM.TVT_Lobby_Water_DoorVisualP1, 0x00.to_bytes(1, "little"), "MainRAM")]
                    Button_Writes += [(RAM.TVT_Lobby_Water_DoorVisualP2, 0x00.to_bytes(1, "little"), "MainRAM")]
                    Button_Writes += [(RAM.TVT_Lobby_Water_BackColor1, 0xAC78.to_bytes(2, "little"), "MainRAM")]
                    Button_Writes += [(RAM.TVT_Lobby_Water_BackColor2, 0xAC90.to_bytes(2, "little"), "MainRAM")]
                    Button_Writes += [(RAM.TVT_Lobby_Water_BackColor3, 0xAE14.to_bytes(2, "little"), "MainRAM")]
                    Button_Writes += [(RAM.TVT_Lobby_Water_BackColor4, 0xAC9C.to_bytes(2, "little"), "MainRAM")]
                    Button_Writes += [(RAM.TVT_Lobby_Water_BackColor5, 0xB1B8.to_bytes(2, "little"), "MainRAM")]
                    Button_Writes += [(RAM.TVT_Lobby_Water_ColorS1P1, 0xB1D0.to_bytes(2, "little"), "MainRAM")]
                    Button_Writes += [(RAM.TVT_Lobby_Water_ColorS1P2, 0xB2EC.to_bytes(2, "little"), "MainRAM")]
                    Button_Writes += [(RAM.TVT_Lobby_Water_TunnelColorS1P1, 0xB1E4.to_bytes(2, "little"), "MainRAM")]
                    Button_Writes += [(RAM.TVT_Lobby_Water_TunnelColorS1P2, 0xB9A0.to_bytes(2, "little"), "MainRAM")]
                    Button_Writes += [(RAM.TVT_Lobby_Water_TunnelColorS2P1, 0xB9B8.to_bytes(2, "little"), "MainRAM")]
                    Button_Writes += [(RAM.TVT_Lobby_Water_TunnelColorS2P2, 0xBB44.to_bytes(2, "little"), "MainRAM")]
                    Button_Writes += [(RAM.TVT_Lobby_Water_TunnelColorS2P3, 0xB9C4.to_bytes(2, "little"), "MainRAM")]
                    Button_Writes += [(RAM.TVT_Lobby_WaterVisual1, 0xF70C.to_bytes(2, "little"), "MainRAM")]
                    Button_Writes += [(RAM.TVT_Lobby_WaterVisual2, 0x00.to_bytes(1, "little"), "MainRAM")]
                    Button_Writes += [(RAM.TVT_Lobby_WaterVisual3, 0xF70C.to_bytes(2, "little"), "MainRAM")]
                    Button_Writes += [(RAM.TVT_Lobby_WaterVisual4, 0x00.to_bytes(1, "little"), "MainRAM")]

        # Monkey Madness Castle Lobby checks
        if currentRoom == 80 and transitionPhase != 6:
            # Monkey Madness Monkey Head door unlock check
            if MM_MonkeyHead_Door != 0x01:
                if self.MM_MonkeyHead_Button != 1:
                    await ctx.send_msgs([{
                        "cmd": "Get",
                        "keys": [f"AE_MM_MonkeyHead_Button_{ctx.team}_{ctx.slot}"]
                    }])
                if self.MM_MonkeyHead_Button == 1:
                    Button_Writes += [(RAM.MM_MonkeyHead_Door, 0x01.to_bytes(1, "little"), "MainRAM")]

            # Monkey Madness Painting door unlock check
            if MM_Painting_Visual != 0x06:
                if self.MM_Painting_Button != 1:
                    await ctx.send_msgs([{
                        "cmd": "Get",
                        "keys": [f"AE_MM_Painting_Button_{ctx.team}_{ctx.slot}"]
                    }])
                if self.MM_Painting_Button == 1:
                    Button_Writes += [(RAM.MM_Painting_Visual, 0x06.to_bytes(1, "little"), "MainRAM")]
                    Button_Writes += [(RAM.MM_Painting_HitBox, 0x06.to_bytes(1, "little"), "MainRAM")]
                    Button_Writes += [(RAM.MM_Painting_VisualStair1, 0x03.to_bytes(1, "little"), "MainRAM")]
                    Button_Writes += [(RAM.MM_Painting_VisualStair2, 0x03.to_bytes(1, "little"), "MainRAM")]
                    Button_Writes += [(RAM.MM_Painting_VisualStair3, 0x03.to_bytes(1, "little"), "MainRAM")]
                    Button_Writes += [(RAM.MM_Painting_HitBoxStair1, 0x06.to_bytes(1, "little"), "MainRAM")]
                    Button_Writes += [(RAM.MM_Painting_HitBoxStair2, 0x06.to_bytes(1, "little"), "MainRAM")]
                    Button_Writes += [(RAM.MM_Painting_HitBoxStair3, 0x06.to_bytes(1, "little"), "MainRAM")]
                    Button_Writes += [(RAM.MM_Painting_VisualFence, 0x00.to_bytes(1, "little"), "MainRAM")]
                    Button_Writes += [(RAM.MM_Painting_HitBoxFence, 0x80.to_bytes(1, "little"), "MainRAM")]

        await bizhawk.write(ctx.bizhawk_ctx, Button_Writes)


    async def lamps_unlocks_handling(self, ctx: "BizHawkClientContext", Lamps_Reads) -> None:
        # Variables
        gameState = Lamps_Reads[0]
        currentRoom = Lamps_Reads[1]
        NearbyRoom = Lamps_Reads[2]
        localLampsUpdate = Lamps_Reads[3]
        globalLampsUpdate = Lamps_Reads[4]
        transitionPhase = Lamps_Reads[5]

        # Deactivate Monkeys detection for lamps and switch to manual door opening if lamp shuffle is activated
        # Condition for some rooms that require the same addresses to function properly
        specialrooms = [41, 44, 67, 75, 76]

        Lamps_writes = []

        # Does not execute the function if you not in a level
        if (gameState not in (RAM.gameState['InLevel'], RAM.gameState['InLevelTT'])):
            return None

        # print("lamps_unlocks_handling")

        lampDoors_toggles = RAM.lampDoors_toggles
        # Trigger Monkey Lamps depending on Lamp states
        boolOpenDoor = False

        # Update lamp doors depending on value
        # print(lampDoors_toggles.keys())
        GotLamp = False
        RoomHaveLamp = False
        if currentRoom in localLampsUpdate:
            GotLamp = localLampsUpdate[currentRoom] == 0x01
            RoomHaveLamp = True
        elif currentRoom in globalLampsUpdate:
            GotLamp = globalLampsUpdate[currentRoom] == 0x01
            RoomHaveLamp = True

        NearbyRoomHaveLamp = False
        if NearbyRoom in localLampsUpdate:
            NearbyRoomHaveLamp = True
        elif NearbyRoom in globalLampsUpdate:
            NearbyRoomHaveLamp = True

        if ctx.slot_data["lamp"] == 0x00:
            # If the room had a lamp, activate all values while going in the transition
            if (NearbyRoomHaveLamp == True and transitionPhase == 0x06 and (NearbyRoom not in specialrooms)) or (
                    RoomHaveLamp == True and transitionPhase != 0x06):
                # print("LampRoom")
                Lamps_writes += [(RAM.localLamp_MonkeyDetect, RAM.lampDoors_update['localLamp_MonkeyDetect_ON'].to_bytes(4, "little"), "MainRAM")]
                Lamps_writes += [(RAM.globalLamp_MonkeyDetect1, RAM.lampDoors_update['globalLamp_MonkeyDetect1_ON'].to_bytes(4, "little"), "MainRAM")]
                Lamps_writes += [(RAM.globalLamp_MonkeyDetect2, RAM.lampDoors_update['globalLamp_MonkeyDetect2_ON'].to_bytes(4, "little"), "MainRAM")]
            elif (NearbyRoom in specialrooms and transitionPhase == 0x06) or (currentRoom in specialrooms):
                # print("SpecialRoom")
                Lamps_writes += [(RAM.localLamp_MonkeyDetect, RAM.lampDoors_update['localLamp_MonkeyDetect_ON'].to_bytes(4, "little"), "MainRAM")]
                Lamps_writes += [(RAM.globalLamp_MonkeyDetect1, RAM.lampDoors_update['globalLamp_MonkeyDetect1_OFF'].to_bytes(4, "little"), "MainRAM")]
                Lamps_writes += [(RAM.globalLamp_MonkeyDetect2, RAM.lampDoors_update['globalLamp_MonkeyDetect2_OFF'].to_bytes(4, "little"), "MainRAM")]
            elif (NearbyRoomHaveLamp == False and transitionPhase == 0x06) or ((currentRoom not in specialrooms) and (RoomHaveLamp == False)):
                # print("NoLampsRoom")
                Lamps_writes += [(RAM.localLamp_MonkeyDetect, RAM.lampDoors_update['localLamp_MonkeyDetect_OFF'].to_bytes(4, "little"), "MainRAM")]
                Lamps_writes += [(RAM.globalLamp_MonkeyDetect1, RAM.lampDoors_update['globalLamp_MonkeyDetect1_OFF'].to_bytes(4, "little"), "MainRAM")]
                Lamps_writes += [(RAM.globalLamp_MonkeyDetect2, RAM.lampDoors_update['globalLamp_MonkeyDetect2_OFF'].to_bytes(4, "little"), "MainRAM")]
        else:
            if (NearbyRoom in specialrooms and transitionPhase == 0x06) or currentRoom in specialrooms:
                # print("SpecialRoom")
                Lamps_writes += [(RAM.localLamp_MonkeyDetect, RAM.lampDoors_update['localLamp_MonkeyDetect_ON'].to_bytes(4, "little"), "MainRAM")]
                Lamps_writes += [(RAM.globalLamp_MonkeyDetect1, RAM.lampDoors_update['globalLamp_MonkeyDetect1_OFF'].to_bytes(4, "little"), "MainRAM")]
                Lamps_writes += [(RAM.globalLamp_MonkeyDetect2, RAM.lampDoors_update['globalLamp_MonkeyDetect2_OFF'].to_bytes(4, "little"), "MainRAM")]
            elif (currentRoom not in specialrooms) or transitionPhase == 0x06:
                # print("NotSpecialRoom")
                Lamps_writes += [(RAM.localLamp_MonkeyDetect, RAM.lampDoors_update['localLamp_MonkeyDetect_OFF'].to_bytes(4, "little"), "MainRAM")]
                Lamps_writes += [(RAM.globalLamp_MonkeyDetect1, RAM.lampDoors_update['globalLamp_MonkeyDetect1_OFF'].to_bytes(4, "little"), "MainRAM")]
                Lamps_writes += [(RAM.globalLamp_MonkeyDetect2, RAM.lampDoors_update['globalLamp_MonkeyDetect2_OFF'].to_bytes(4, "little"), "MainRAM")]

        # You can now have the Lamp Item and bypass the door
        if currentRoom in lampDoors_toggles.keys() and GotLamp:
            lamplist_keys = list(lampDoors_toggles[currentRoom].keys())
            lamplist_values = list(lampDoors_toggles[currentRoom].values())
            # print(lamplist_values)
            for x in range(len(lamplist_keys)):
                Lamps_writes2 = []
                Lamps_Guards = [(RAM.currentRoomIdAddress, currentRoom.to_bytes(1, "little"), "MainRAM")]
                # lamp_values2 = list(lamp_values[x].__str__().replace("[", "").replace("]", "").split(","))
                lamp_values = list(lamplist_values[x])
                lamp_bytes = lamp_values[0]
                lamp_openvalue = lamp_values[1].to_bytes(lamp_bytes, "little")
                lamp_closedvalue = lamp_values[2].to_bytes(lamp_bytes, "little")
                lamp_address = (lamplist_keys[x])
                Lamps_writes2 += [(lamp_address, lamp_openvalue, "MainRAM")]
                Lamps_Guards += [(lamp_address, lamp_closedvalue, "MainRAM")]
                await bizhawk.guarded_write(ctx.bizhawk_ctx, Lamps_writes2, Lamps_Guards)
        await bizhawk.write(ctx.bizhawk_ctx, Lamps_writes)


    async def traps_handling(self, ctx: "BizHawkClientContext", Trap_Reads) -> None:
        # TODO: GadgetShuffle Trap is very unstable right now, it had been deactivated

        # Notes for traps for now:
        # Banana Peel = Slip by setting SpikeState2 to 0x2F
        gameState = Trap_Reads[0]
        gotMail = Trap_Reads[1]
        spikeState2 = Trap_Reads[2]
        menuState = Trap_Reads[3]
        menuState2 = Trap_Reads[4]
        currentGadgets = Trap_Reads[5]
        currentRoom = Trap_Reads[6]

        Trap_Writes = []
        Trap_Guards = []

        # Gamestate
        valid_gameStates = (RAM.gameState['InLevel'], RAM.gameState['InLevelTT'], RAM.gameState['TimeStation'], RAM.gameState['Jake'])
        in_menu = (menuState == 0 and menuState2 == 1)
        reading_mail = (gotMail == 0x01) or (gotMail == 0x02)
        is_sliding = (spikeState2 == 0x2F)
        is_idle = (spikeState2 in {0x80,0x81,0x82,0x83,0x84})
        in_race = (currentRoom == 19 or currentRoom == 36)

        if self.trap_queue == []:
            #Exit if no traps
            return None
        else:
            # Does not send the traps in these states
            if (gameState not in valid_gameStates or in_menu or reading_mail or is_sliding or in_race or is_idle):
                # print("Waiiiitttiinnng for...valid state")
                if is_idle:
                    # Trigger a Wake Up for spike. Banana Peel is deadly while Idle
                    Trap_Writes += [(RAM.spikeIdleTimer, 0x0000.to_bytes(2, "little"), "MainRAM")]
                    await bizhawk.write(ctx.bizhawk_ctx, Trap_Writes)
                return None
                # Exit without sending trap, keeping it active for the next pass

            if self.trap_queue[0] == RAM.items['BananaPeelTrap']:
                self.trap_queue.pop(0)
                Trap_Writes += [(RAM.spikeState2Address, 0x2F.to_bytes(1, "little"), "MainRAM")]
            elif self.trap_queue[0] == RAM.items['GadgetShuffleTrap']:
                self.trap_queue.pop(0)

                # print(self.trap_queue)
                chosen_gadgets = []
                chosen_values = [0, 0, 0, 0]
                faces = [0, 1, 2, 3]
                # Exit if no gadgets has been unlocked yet
                if currentGadgets == []:
                    return None

                # 1 pass for each face
                for x in range(4):
                    randomFace = int(round(random() * (len(faces) -1), None))
                    face = faces[randomFace]
                    # If there is no more gadgets, it means we put an "Empty" spot
                    if currentGadgets == []:
                        # print("Face #" + str(randomFace + 1) + " : None | 255")
                        chosen_values[face] = 0xFF
                        faces.pop(randomFace)
                    else:
                        randomGadget = int(round(random() * (len(currentGadgets) - 1), None))
                        gadget_value = gadgetsValues[currentGadgets[randomGadget]]
                        chosen_values[face] = gadget_value
                        # print("Face #" + str(faces[randomFace]) + " : " + str(currentGadgets[randomGadget]) + " | " + str(gadgetsValues[currentGadgets[randomGadget]]))
                        chosen_gadgets.append(str(currentGadgets[randomGadget]))
                        currentGadgets.pop(randomGadget)
                        faces.pop(randomFace)
                # print(chosen_gadgets)

                Trap_Writes += [(RAM.crossGadgetAddress, chosen_values[0].to_bytes(1, "little"), "MainRAM")]
                Trap_Writes += [(RAM.squareGadgetAddress, chosen_values[1].to_bytes(1, "little"), "MainRAM")]
                Trap_Writes += [(RAM.circleGadgetAddress, chosen_values[2].to_bytes(1, "little"), "MainRAM")]
                Trap_Writes += [(RAM.triangleGadgetAddress, chosen_values[3].to_bytes(1, "little"), "MainRAM")]

                # Select a gadget slot
                randomSelect = int(round(random() * (len(chosen_values) - 1),None))
                # print("random:" + str(randomSelect))
                # print(chosen_values)
                # Attempt to correct the radar being weird on shuffle sometimes
                if chosen_values[randomSelect] == 0x02:
                    Trap_Writes1 = []
                    Trap_Writes1 += [(RAM.radarFixAddress, 0x30.to_bytes(1, "little"), "MainRAM")]
                    await bizhawk.write(ctx.bizhawk_ctx, Trap_Writes1)
                elif chosen_values[randomSelect] == 0x04:
                    Trap_Writes1 = []
                    Trap_Writes1 += [(RAM.heldGadgetAddress, 0xFF.to_bytes(1, "little"), "MainRAM")]
                    Trap_Writes1 += [(RAM.hoopFixAddress, 0x0000000000000000.to_bytes(14, "little"), "MainRAM")]
                    await bizhawk.write(ctx.bizhawk_ctx, Trap_Writes1)
                if spikeState2 in (128, 129, 131):
                    Trap_Writes += [(RAM.spikeState2Address, 0x00.to_bytes(1, "little"), "MainRAM")]
                Trap_Writes += [(RAM.heldGadgetAddress, chosen_values[randomSelect].to_bytes(1, "little"), "MainRAM")]
                # if chosen_values[randomSelect] != 0xFF:
                    # print(chosen_values[randomSelect])
                    # print("Selected gadget : " + chosen_gadgets[randomSelect])
                # else:
                    # print("Selected gadget : NONE")

            await bizhawk.write(ctx.bizhawk_ctx, Trap_Writes)


    async def level_select_optimization(self, ctx: "BizHawkClientContext", LSO_Reads) -> None:
        # For coin display to be ignored while in Level Select
        gameState = LSO_Reads[0]
        CoinTable = LSO_Reads[1]
        TempCoinTable = LSO_Reads[2]
        SA_Completed = LSO_Reads[3]
        Temp_SA_Completed = LSO_Reads[4]
        GA_Completed = LSO_Reads[5]
        Temp_GA_Completed = LSO_Reads[6]
        LS_currentLevel = LSO_Reads[7]
        LS_currentWorld = LSO_Reads[8]
        worldIsScrollingRight = LSO_Reads[9]

        LS_Writes = []

        if RAM.gameState["LevelSelect"] == gameState:
            if CoinTable != RAM.blank_coinTable and ((TempCoinTable == RAM.blank_coinTable)) or ((TempCoinTable == RAM.blank_coinTable2)):
                LS_Writes += [(RAM.startingCoinAddress, RAM.blank_coinTable.to_bytes(100, "little"), "MainRAM")]
                LS_Writes += [(RAM.temp_startingCoinAddress, CoinTable.to_bytes(100, "little"), "MainRAM")]
            if SA_Completed != 0x00 and Temp_SA_Completed == 0xFF:
                LS_Writes += [(RAM.SA_CompletedAddress, 0x00.to_bytes(1, "little"), "MainRAM")]
                LS_Writes += [(RAM.GA_CompletedAddress, 0x00.to_bytes(1, "little"), "MainRAM")]
                LS_Writes += [(RAM.Temp_SA_CompletedAddress, SA_Completed.to_bytes(1, "little"), "MainRAM")]
                LS_Writes += [(RAM.Temp_GA_CompletedAddress, GA_Completed.to_bytes(1, "little"), "MainRAM")]

        else:
            if CoinTable == RAM.blank_coinTable and ((TempCoinTable != RAM.blank_coinTable and TempCoinTable != RAM.blank_coinTable2)):
                LS_Writes += [(RAM.startingCoinAddress, TempCoinTable.to_bytes(100, "little"), "MainRAM")]
                LS_Writes += [(RAM.temp_startingCoinAddress, RAM.blank_coinTable.to_bytes(100, "little"), "MainRAM")]

            if SA_Completed == 0x00 and Temp_SA_Completed != 0xFF:
                LS_Writes += [(RAM.SA_CompletedAddress, Temp_SA_Completed.to_bytes(1, "little"), "MainRAM")]
                LS_Writes += [(RAM.GA_CompletedAddress, Temp_GA_Completed.to_bytes(1, "little"), "MainRAM")]
                LS_Writes += [(RAM.Temp_SA_CompletedAddress, 0xFF.to_bytes(1, "little"), "MainRAM")]
                LS_Writes += [(RAM.Temp_GA_CompletedAddress, 0x00.to_bytes(1, "little"), "MainRAM")]

        # Prevent scrolling past the unlocked ERA/level
        if gameState == RAM.gameState["LevelSelect"]:
            reqkeys = ctx.slot_data["reqkeys"]

            # Get all keys required for the next world, based on first level of ERAS
            WorldUnlocks = [reqkeys[3], reqkeys[6], reqkeys[7], reqkeys[10], reqkeys[13], reqkeys[14], reqkeys[17],
                            reqkeys[20], reqkeys[21]]
            # Format current selected level to compare against reqkeys table
            currentLevel = (3 * LS_currentWorld) + LS_currentLevel
            if LS_currentWorld >= 3:
                currentLevel -= 2
            if LS_currentWorld >= 6:
                currentLevel -= 2

            # Check if the selected world is the last (To stay within bound of the list)
            if 0 <= LS_currentWorld < 9:
                # Modified old fix to detect current level requirement and scroll back to the last unlocked world/level
                if self.worldkeycount < reqkeys[currentLevel]:
                    # Kinda strange condition but just to be sure ;)
                    if LS_currentLevel == 0 and LS_currentWorld != 0:
                        LS_Writes += [(RAM.selectedWorldAddress, (LS_currentWorld - 1).to_bytes(1, "little"), "MainRAM")]
                    else:
                        LS_Writes += [(RAM.selectedLevelAddress, (LS_currentLevel - 1).to_bytes(1, "little"), "MainRAM")]

                # If you have less World Keys that the required keys for the next ERA, disable R1, Right Stick and Right DPAD detection

                if (LS_currentWorld < 8) and (worldIsScrollingRight == 0xFFFF):
                    if (self.worldkeycount < WorldUnlocks[LS_currentWorld + 1]):
                        LS_Writes += [(RAM.worldScrollToRightDPAD, 0x0000.to_bytes(2, "little"), "MainRAM")]
                        LS_Writes += [(RAM.worldScrollToRightR1, 0x0000.to_bytes(2, "little"), "MainRAM")]
                elif (self.worldkeycount < WorldUnlocks[LS_currentWorld]):
                    LS_Writes += [(RAM.worldScrollToRightDPAD, 0x0000.to_bytes(2, "little"), "MainRAM")]
                    LS_Writes += [(RAM.worldScrollToRightR1, 0x0000.to_bytes(2, "little"), "MainRAM")]
                else:
                    LS_Writes += [(RAM.worldScrollToRightDPAD, 0x0009.to_bytes(2, "little"), "MainRAM")]
                    LS_Writes += [(RAM.worldScrollToRightR1, 0x0009.to_bytes(2, "little"), "MainRAM")]

        await bizhawk.write(ctx.bizhawk_ctx, LS_Writes)


    async def water_net_handling(self, ctx: "BizHawkClientContext", WN_Reads) -> None:
        # Water Net client handling
        # If Progressive WaterNet is 0 no Swim and no Dive, if it's 1 No Dive (Swim only)
        # 8-9 Jumping/falling, 35-36 D-Jump, 83-84 Flyer => don't reset the counter

        inAir = [0x08, 0x09, 0x35, 0x36, 0x83, 0x84]
        swimming = [0x46, 0x47]
        grounded = [0x00, 0x01, 0x02, 0x05,0x07]  # 0x80, 0x81 Removed them since you can fling you net and give you extra air
        limited_OxygenLevel = 0x64

        gameState = WN_Reads[0]
        waternetState = WN_Reads[1]
        gameRunning = WN_Reads[2]
        spikeState2 = WN_Reads[3]
        swim_oxygenLevel = WN_Reads[4]
        cookies = WN_Reads[5]
        isUnderwater = WN_Reads[6]
        watercatchState = WN_Reads[7]

        WN_writes = []

        # Base variables
        if waternetState == 0x00:
            WN_writes += [(RAM.swim_surfaceDetectionAddress, 0x00000000.to_bytes(4, "little"), "MainRAM")]
            WN_writes += [(RAM.canDiveAddress, 0x00000000.to_bytes(4, "little"), "MainRAM")]
            WN_writes += [(RAM.swim_oxygenReplenishSoundAddress, 0x00000000.to_bytes(4, "little"), "MainRAM")]
            WN_writes += [(RAM.swim_ReplenishOxygenUWAddress, 0x00000000.to_bytes(4, "little"), "MainRAM")]
            WN_writes += [(RAM.swim_replenishOxygenOnEntryAddress, 0x00000000.to_bytes(4, "little"), "MainRAM")]
        elif waternetState == 0x01:
            WN_writes += [(RAM.swim_surfaceDetectionAddress, 0x0801853A.to_bytes(4, "little"), "MainRAM")]
            WN_writes += [(RAM.canDiveAddress, 0x00000000.to_bytes(4, "little"), "MainRAM")]
            WN_writes += [(RAM.swim_oxygenReplenishSoundAddress, 0x00000000.to_bytes(4, "little"), "MainRAM")]
            WN_writes += [(RAM.swim_ReplenishOxygenUWAddress, 0x00000000.to_bytes(4, "little"), "MainRAM")]
            WN_writes += [(RAM.swim_replenishOxygenOnEntryAddress, 0x00000000.to_bytes(4, "little"), "MainRAM")]
        else:
            # (waternetstate > 0x01)
            WN_writes += [(RAM.swim_surfaceDetectionAddress, 0x0801853A.to_bytes(4, "little"), "MainRAM")]
            WN_writes += [(RAM.canDiveAddress, 0x08018664.to_bytes(4, "little"), "MainRAM")]
            WN_writes += [(RAM.swim_oxygenReplenishSoundAddress, 0x0C021DFE.to_bytes(4, "little"), "MainRAM")]
            WN_writes += [(RAM.swim_ReplenishOxygenUWAddress, 0xA4500018.to_bytes(4, "little"), "MainRAM")]
            WN_writes += [(RAM.swim_replenishOxygenOnEntryAddress, 0xA4434DC8.to_bytes(4, "little"), "MainRAM")]

        # Oxygen Handling
        if waternetState == 0x00:
            if gameState == RAM.gameState["InLevel"] or gameState == RAM.gameState["InLevelTT"]:
                if gameRunning == 0x01:
                    # Set the air to the "Limited" value if 2 conditions:
                    # Oxygen is higher that "Limited" value AND spike is Swimming or Grounded
                    if spikeState2 in swimming:
                        if (swim_oxygenLevel > limited_OxygenLevel):
                            WN_writes += [(RAM.swim_oxygenLevelAddress, limited_OxygenLevel.to_bytes(2, "little"), "MainRAM")]
                    else:
                        # if self.waterHeight != 0:
                        # self.waterHeight = 0
                        if spikeState2 in grounded:
                            WN_writes += [(RAM.swim_oxygenLevelAddress, limited_OxygenLevel.to_bytes(2, "little"), "MainRAM")]

                else:
                    # Game Not running
                    if swim_oxygenLevel == 0 and cookies == 0 and gameRunning == 0:
                        # You died while swimming, reset Oxygen to "Limited" value prevent death loops
                        WN_writes += [(RAM.swim_oxygenLevelAddress, limited_OxygenLevel.to_bytes(2, "little"), "MainRAM")]
                        WN_writes += [(RAM.isUnderwater, 0x00.to_bytes(1, "little"), "MainRAM")]

        if waternetState == 0x01:

            if isUnderwater == 0x00 and swim_oxygenLevel != limited_OxygenLevel:
                WN_writes += [(RAM.swim_oxygenLevelAddress, limited_OxygenLevel.to_bytes(2, "little"), "MainRAM")]
            if swim_oxygenLevel == 0 and cookies == 0 and gameRunning == 0:
                # You died while swimming, reset Oxygen to "Limited" value prevent death loops
                WN_writes += [(RAM.swim_oxygenLevelAddress, limited_OxygenLevel.to_bytes(2, "little"), "MainRAM")]
                WN_writes += [(RAM.isUnderwater, 0x00.to_bytes(1, "little"), "MainRAM")]

        # WaterCatch unlocking stuff bellow
        if watercatchState == 0x00:
            WN_writes += [(RAM.canWaterCatchAddress, 0x00.to_bytes(1, "little"), "MainRAM")]
        else:
            WN_writes += [(RAM.canWaterCatchAddress, 0x04.to_bytes(1, "little"), "MainRAM")]

        # Low Oxygen Sounds
        if spikeState2 in swimming:

            # Off
            if ctx.slot_data["lowoxygensounds"] == 0x00:
                WN_writes += [(RAM.swim_oxygenLowLevelSoundAddress, 0x3C028004.to_bytes(4, "little"), "MainRAM")]
                WN_writes += [(RAM.swim_oxygenMidLevelSoundAddress, 0x3C028004.to_bytes(4, "little"), "MainRAM")]
            # Half Beeps
            elif ctx.slot_data["lowoxygensounds"] == 0x01:

                self.lowOxygenCounter += 1
                # Should start at 1
                # print(self.lowOxygenCounter)
                if self.lowOxygenCounter <= 2:
                    WN_writes += [(RAM.swim_oxygenLowLevelSoundAddress, 0x3C02800F.to_bytes(4, "little"), "MainRAM")]
                    WN_writes += [(RAM.swim_oxygenMidLevelSoundAddress, 0x3C02800F.to_bytes(4, "little"), "MainRAM")]
                elif self.lowOxygenCounter <= 3:
                    WN_writes += [(RAM.swim_oxygenLowLevelSoundAddress, 0x3C028004.to_bytes(4, "little"), "MainRAM")]
                    WN_writes += [(RAM.swim_oxygenMidLevelSoundAddress, 0x3C028004.to_bytes(4, "little"), "MainRAM")]
                elif self.lowOxygenCounter > 3:
                    self.lowOxygenCounter = 0

            # On (Vanilla)
            else:
                # print("Vanilla")
                WN_writes += [(RAM.swim_oxygenLowLevelSoundAddress, 0x3C02800F.to_bytes(4, "little"), "MainRAM")]
                WN_writes += [(RAM.swim_oxygenMidLevelSoundAddress, 0x3C02800F.to_bytes(4, "little"), "MainRAM")]
        else:
            if self.lowOxygenCounter != 1:
                self.lowOxygenCounter = 1

        await bizhawk.write(ctx.bizhawk_ctx,WN_writes)


    async def handle_death_link(self, ctx: "BizHawkClientContext", DL_Reads) -> None:
        """
        Checks whether the player has died while connected and sends a death link if so.
        """
        cookies = DL_Reads[0]
        gameRunning = DL_Reads[1]
        gameState = DL_Reads[2]
        menuState2 = DL_Reads[3]
        spikestate2 = DL_Reads[4]

        OnTree = {56, 57, 58, 59, 60}

        DL_writes = []
        DL_writes2 = []
        if self.deathlink == 1:
            if "DeathLink" not in ctx.tags:
                await ctx.update_death_link(True)
                self.previous_death_link = ctx.last_death_link
            if "DeathLink" in ctx.tags and ctx.last_death_link + 1 < time.time():
                if cookies == 0x00 and not self.sending_death_link and gameState in (RAM.gameState["InLevel"],RAM.gameState["TimeStation"]):
                    await self.send_deathlink(ctx)
                elif cookies != 0x00:
                    self.sending_death_link = False
            # Wait on exiting menu before sending deathlink
            if self.pending_death_link and menuState2 != 1:
                DL_writes += [(RAM.cookieAddress, 0x00.to_bytes(1, "little"), "MainRAM")]
                DL_writes += [(RAM.instakillAddress, 0xFF.to_bytes(1, "little"), "MainRAM")]
                if spikestate2 in OnTree:
                    DL_writes2 += [(RAM.Controls_TriggersShapes, 0xFD.to_bytes(1, "little"), "MainRAM")]
                self.pending_death_link = False
                self.sending_death_link = True
                await bizhawk.write(ctx.bizhawk_ctx, DL_writes)
                await bizhawk.write(ctx.bizhawk_ctx, DL_writes2)
        elif self.deathlink == 0:
            await ctx.update_death_link(False)
            self.previous_death_link = ctx.last_death_link

    async def send_deathlink(self, ctx: "BizHawkClientContext") -> None:
        self.sending_death_link = True
        ctx.last_death_link = time.time()
        DeathMessageList = ["`Ohhh noooo!`", "`This bites.`"]
        randomNumber = (round(random() * (len(DeathMessageList) - 1),None))
        DeathMessage = DeathMessageList[randomNumber]
        DeathText = ctx.player_names[ctx.slot] + " says: " + DeathMessage + " (Died)"
        await ctx.send_death(DeathText)


    def on_deathlink(self, ctx: "BizHawkClientContext") -> None:
        ctx.last_death_link = time.time()
        self.pending_death_link = True


    def unlockLevels(self, ctx: "BizHawkClientContext", monkeylevelCounts, gameState, hundoMonkeysCount, reqkeys, newpositions, SAcomplete, GAcomplete):

        key = self.worldkeycount
        token = self.tokencount
        curApesWrite = ""
        reqApesWrite = ""
        hundoWrite = ""
        levellocked = RAM.levelStatus["Locked"].to_bytes(1, byteorder = "little")
        levelopen = RAM.levelStatus["Open"].to_bytes(1, byteorder = "little")
        levelhundo = RAM.levelStatus["Hundo"].to_bytes(1, byteorder = "little")
        allCompleted = True

        debug = False

        levels_keys = hundoMonkeysCount.keys()
        levels_list = list(levels_keys)
        if gameState == RAM.gameState["LevelSelect"] or debug:
            for x in range(len(levels_list)):
                if int.from_bytes(monkeylevelCounts[x], byteorder = "little") < hundoMonkeysCount[levels_list[x]]:
                    # print("Level " + str(x) + " not completed" + str(int.from_bytes(monkeylevelCounts[x])) + "/" + str(hundoMonkeysCount[levels_list[x]]))
                    allCompleted = False
                    break
                    # Does not need to check the rest of the levels, at least 1 is not completed

        if ctx.slot_data["goal"] == GoalOption.option_ppmtoken:
            PPMUnlock = (key >= reqkeys[21] and token >= min(ctx.slot_data["requiredtokens"], ctx.slot_data["totaltokens"]))
        elif ctx.slot_data["goal"] == GoalOption.option_mmtoken or ctx.slot_data["goal"] == GoalOption.option_tokenhunt:
            PPMUnlock = (key >= reqkeys[21])
        else:
            PPMUnlock = (key >= reqkeys[21] and allCompleted)

        # Set unlocked/locked state of levels
        # This does not handle assignment of Specter Coin icons.
        # TODO: Change the assignment of "Hundo" status to assign it to the ENTRANCE that's completed, not the LEVEL
        # Most of this handling is about entrance order - the Hundo check would need to be pulled out of the big if chain because it's about level order right now.
        # Make sure that Hundo doesn't get set on a level that needs to be Locked and that Open doesn't get set on a level that needs to be Hundo.
        levelstates = []
        for index in range(0, 21):
            # Do we have enough keys for this level? If no, lock. If yes, continue.
            if key >= reqkeys[index]:
                # Do we have enough keys for the next level? If no, lock. If yes, open.
                if key >= reqkeys[index + 1]:
                    levelstates.append((RAM.levelAddresses[list(RAM.levelAddresses.keys())[index]], levelopen, "MainRAM"))
                else:
                    levelstates.append((RAM.levelAddresses[list(RAM.levelAddresses.keys())[index]], levellocked, "MainRAM"))
            else:
                levelstates.append((RAM.levelAddresses[list(RAM.levelAddresses.keys())[index]], levellocked, "MainRAM"))

        # Set hundo status on entrances that are open and have all monkeys in them caught.
        # Starts by checking Fossil Field (the level)
        for index in range(0, 21):
            # Is this level a race level?
            if index == 6:
                # Is Stadium Attack completed?
                if SAcomplete == 25:
                    levelstates[newpositions[index]] = (RAM.levelAddresses[list(RAM.levelAddresses.keys())[newpositions[index]]], levelhundo, "MainRAM")
            elif index == 13:
                # Is Gladiator Attack completed?
                if GAcomplete == 25:
                    levelstates[newpositions[index]] = (RAM.levelAddresses[list(RAM.levelAddresses.keys())[newpositions[index]]], levelhundo, "MainRAM")
            else:
                # Standard level
                # Check if the entrance of the indexed level is open.
                # If yes, continue. If no, do nothing, the state is correct.
                # (Index 0) If Fossil Field is at Dark Ruins, this checks the Dark Ruins entrance (index 4).
                if levelstates[newpositions[index]] == (RAM.levelAddresses[list(RAM.levelAddresses.keys())[newpositions[index]]], levelopen, "MainRAM"):
                    # Check if all monkeys of the indexed level are caught.
                    # If yes, set the state to hundo. If no, do nothing, the state is correct.
                    # (Index 0) If Fossil Field is at Dark Ruins, set the Dark Ruins entrance (index 4) to hundo.
                    if int.from_bytes(monkeylevelCounts[index], byteorder = "little") >= hundoMonkeysCount[levels_list[index]]:
                        levelstates[newpositions[index]] = (RAM.levelAddresses[list(RAM.levelAddresses.keys())[newpositions[index]]], levelhundo, "MainRAM")

        # Monkey Madness entrance must be set to locked if Peak Point Matrix should be locked
        if PPMUnlock == False:
            levelstates[20] = ((RAM.levelAddresses[list(RAM.levelAddresses.keys())[20]], levellocked, "MainRAM"))

        # If there is a change in required monkeys count, include it in the writes
        returns = list(levelstates)
        if curApesWrite != "":
            returns.append(curApesWrite)
        if reqApesWrite != "":
            returns.append(reqApesWrite)
        if hundoWrite != "":
            returns.append(hundoWrite)
        return returns


# Mailbox text helper functions
def text_to_bytes(name):
    bytelist = []
    for x in name:
        bytelist.append(character_lookup(x))
    return bytelist


def character_lookup(byte):
    if byte.isspace():  # Space
        return 255
    if byte.isalpha():
        return ord(byte) - 49  # Both uppercase and lowercase letters
    if byte.isdecimal():
        if int(byte) < 6:
            return ord(byte) + 58  # 0-5
        else:
            return ord(byte) + 68  # 6-9
    if ord(byte) == 39:  # Single apostrophe
        return 187
    if ord(byte) == 46:  # Period
        return 172
    if ord(byte) == 47:  # Slash
        return 141
    if ord(byte) == 58:  # Colon
        return 174
