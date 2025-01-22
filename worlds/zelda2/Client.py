import logging
import struct
import time
from struct import pack
from .game_data import location_table
from typing import TYPE_CHECKING, Dict, Set

from NetUtils import ClientStatus
import worlds._bizhawk as bizhawk
from worlds._bizhawk.client import BizHawkClient
import time

if TYPE_CHECKING:
    from worlds._bizhawk.context import BizHawkClientContext

EXPECTED_ROM_NAME = "LEGEND OF ZELDA2"


class Zelda2Client(BizHawkClient):
    game = "Zelda II: The Adventure of Link"
    system = ("NES")
    location_map = location_table

    def __init__(self) -> None:
        super().__init__()

    async def validate_rom(self, ctx: "BizHawkClientContext") -> bool:
        from CommonClient import logger

        try:
            # Check ROM name/patch version
            rom_name_bytes = (
                await bizhawk.read(ctx.bizhawk_ctx, [(0x1FFE0, 16, "PRG ROM")])
            )[0]

            rom_name = bytes([byte for byte in rom_name_bytes if byte != 0]).decode(
                "ascii"
            )
            if not rom_name.startswith(EXPECTED_ROM_NAME):
                logger.info(
                    "ERROR: Rom is not valid!"
                )
                return False
        except UnicodeDecodeError:
            return False
        except bizhawk.RequestFailedError:
            return False  # Should verify on the next pass

        ctx.game = self.game
        ctx.items_handling = 0b111

        return True

    async def set_auth(self, ctx: "BizHawkClientContext") -> None:
        from CommonClient import logger

        slot_name_length = await bizhawk.read(ctx.bizhawk_ctx, [(0x1A2B0, 1, "CHR ROM")])
        slot_name_bytes = await bizhawk.read(
            ctx.bizhawk_ctx, [(0x1A2B1, slot_name_length[0][0], "CHR ROM")]
        )
        ctx.auth = bytes([byte for byte in slot_name_bytes[0] if byte != 0]).decode(
            "utf-8"
        )

    def on_package(self, ctx: "BizHawkClientContext", cmd: str, args: dict) -> None:
        if cmd != "Bounced":
            return
        if "tags" not in args:
            return

    async def game_watcher(self, ctx: "BizHawkClientContext") -> None:
        from CommonClient import logger

        if ctx.server_version.build > 0:
            ctx.connected = True
        else:
            ctx.connected = False
            ctx.refresh_connect = True

        if ctx.slot_data != None:
            ctx.data_present = True
        else:
            ctx.data_present = False

        if ctx.server is None or ctx.server.socket.closed or ctx.slot_data is None:
            return

        read_state = await bizhawk.read(ctx.bizhawk_ctx, [(0x7A10, 1, "SYSTEM BUS"), # Item that the server has sent
                                                            (0x0600, 0xDF, "RAM"), # Table of flags for locations
                                                            (0x0736, 1, "RAM"), # Game state
                                                            (0x7A18, 2, "SYSTEM BUS"), #NPC checks, stored separately
                                                            (0x076C, 1, "RAM"), # State I read for the goal
                                                            (0x7A1C, 2, "SYSTEM BUS")]) # total number of items gotten from the server

        currently_obtained_item = int.from_bytes(read_state[0], "little")
        loc_array = bytearray(read_state[1])
        game_state = int.from_bytes(read_state[2], "little")
        special_checks = int.from_bytes(read_state[3], "little")
        goal_trigger = int.from_bytes(read_state[4], "little")
        total_received_items = int.from_bytes(read_state[5], "big")

        # is_dead = int.from_bytes(read_state[4], "little")

        if currently_obtained_item > 0x00:
            return

        if game_state != 0x0B: # Are we in side-scroll mode?
            return

        new_checks = []

        for loc_id, loc_pointer in self.location_map.items():
            if loc_id not in ctx.locations_checked:
                location = loc_array[loc_pointer]
                if location == 0:
                    new_checks.append(loc_id)

            if loc_id in ctx.checked_locations:
                loc_array[loc_pointer] = 0 

        await bizhawk.write(ctx.bizhawk_ctx, [(0x0500, loc_array, "RAM")])
                
        for new_check_id in new_checks:
            ctx.locations_checked.add(new_check_id)
            location = ctx.location_names[new_check_id]
            await ctx.send_msgs([{"cmd": "LocationChecks", "locations": [new_check_id]}])

        if total_received_items < len(ctx.items_received):
            item = ctx.items_received[total_received_items]
            total_received_items += 1

            if item.item in item_ids:
                ram_item = item_ids[item.item]
                await bizhawk.write(ctx.bizhawk_ctx, [(0x780, bytes([item.item]), "SRAM")])
                await bizhawk.write(ctx.bizhawk_ctx, [(0x781, bytes([total_received_items]), "SRAM")])

        if not ctx.finished_game and goal_trigger == 0x04:
            await ctx.send_msgs([{
                "cmd": "StatusUpdate",
                "status": ClientStatus.CLIENT_GOAL
            }])


