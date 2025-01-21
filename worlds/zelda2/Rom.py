import hashlib
import os
import Utils
import typing
import struct
from worlds.Files import APProcedurePatch, APTokenMixin, APTokenTypes, APPatchExtension
from typing import TYPE_CHECKING, Optional
from logging import warning
from .game_data import world_version

if TYPE_CHECKING:
    from . import Z2World

md5 = "764d36fa8a2450834da5e8194281035a"


class LocalRom(object):

    def __init__(self, file: bytes, name: Optional[str] = None) -> None:
        self.file = bytearray(file)
        self.name = name

    def read_byte(self, offset: int) -> int:
        return self.file[offset]

    def read_bytes(self, offset: int, length: int) -> bytes:
        return self.file[offset:offset + length]

    def write_byte(self, offset: int, value: int) -> None:
        self.file[offset] = value

    def write_bytes(self, offset: int, values) -> None:
        self.file[offset:offset + len(values)] = values

    def get_bytes(self) -> bytes:
        return bytes(self.file)


def patch_rom(world, rom, player: int):

    if world.options.random_tunic_color:
        shield_color = world.random.randint(0x10, 0x3E)
        tunic_color = world.random.randint(0x10, 0x3E)

        rom.write_bytes(0x00E8E, bytearray([shield_color])) #Shield palette
        rom.write_bytes(0x040B1, bytearray([tunic_color])) # Normal palette
        rom.write_bytes(0x040C1, bytearray([tunic_color])) # Normal palette
        rom.write_bytes(0x040D1, bytearray([tunic_color])) # Normal palette
        rom.write_bytes(0x040D1, bytearray([tunic_color])) # Normal palette
        rom.write_bytes(0x17C1B, bytearray([tunic_color])) # File select
        rom.write_bytes(0x1C466, bytearray([tunic_color])) # Loading
        rom.write_bytes(0x1C47E, bytearray([tunic_color])) # Map palette

    if world.options.random_palace_graphics:
        for i in range(7):
            base_color = world.random.randint(0x00, 0x0C)
            secondary_color = base_color + 0x20
            if base_color >= 0x10:
                tertiary_color = base_color - 0x10
            else:
                tertiary_color = 0x0F
            rom.write_bytes(0x10486 + (16 * i), bytearray([base_color, secondary_color]))
            rom.write_bytes(0x13F16 + (16 * i), bytearray([base_color, secondary_color]))
            rom.write_bytes(0x13F05 + (16 * i), bytearray([tertiary_color]))
        rom.copy_bytes(0x29650, 0x20, 0x3AB00)
        rom.copy_bytes(0x2B650, 0x20, 0x3AB20)
        rom.copy_bytes(0x2D650, 0x20, 0x3AB40)
        rom.copy_bytes(0x33650, 0x20, 0x3AB60)
        rom.copy_bytes(0x35650, 0x20, 0x3AB80)
        rom.copy_bytes(0x37650, 0x20, 0x3ABA0)
        rom.copy_bytes(0x39650, 0x20, 0x3ABC0)

    rom.write_bytes(0x17B10, bytearray([world.options.required_crystals.value]))
    rom.write_bytes(0x17AF3, bytearray([world.options.starting_attack.value]))
    rom.write_bytes(0x17AF4, bytearray([world.options.starting_magic.value]))
    rom.write_bytes(0x17AF5, bytearray([world.options.starting_life.value]))
    rom.write_bytes(0x2B70, bytearray([world.options.palace_respawn.value]))
    rom.write_bytes(0x2B70, bytearray([world.options.palace_respawn.value]))
    rom.write_bytes(0x17DB3, bytearray([world.options.starting_lives.value]))

    if world.options.fast_great_palace:
        rom.write_bytes(0x1472C, bytearray([0xAA]))
        rom.write_bytes(0x147D5, bytearray([0x03]))

    if world.options.keep_exp:
        rom.write_bytes(0x21DA, bytearray([0x59, 0x07]))
        rom.write_bytes(0x21DD, bytearray([0x59, 0x07]))
        rom.write_bytes(0x2C40, bytearray([0x01]))

    if world.options.remove_early_boulder:
        rom.write_bytes(0x05189, bytearray([0x09])) #Remove the boulder blocking the west coast

    #if world.options.better_boots:

    from Main import __version__
    rom.name = bytearray(f'Zelda2AP{__version__.replace(".", "")[0:3]}_{player}_{world.multiworld.seed:11}\0', "utf8")[:21]
    rom.name.extend([0] * (21 - len(rom.name)))
    rom.write_bytes(0x00FFC0, rom.name)

    rom.write_file("token_patch.bin", rom.get_token_binary())


class Z2ProcPatch(APProcedurePatch, APTokenMixin):
    hash = md5
    game = "Zelda II: The Adventure of Link"
    patch_file_ending = ".apz2"
    result_file_ending = ".nes"
    name: bytearray
    procedure = [
        ("apply_bsdiff4", ["z2_base.bsdiff4"]),
        ("apply_tokens", ["token_patch.bin"]),
        ("repoint_vanilla_tables", [])
    ]

    @classmethod
    def get_source_data(cls) -> bytes:
        return get_base_rom_bytes()

    def write_byte(self, offset, value):
        self.write_token(APTokenTypes.WRITE, offset, value.to_bytes(1, "little"))

    def write_bytes(self, offset, value: typing.Iterable[int]):
        self.write_token(APTokenTypes.WRITE, offset, bytes(value))
    
    def copy_bytes(self, source, amount, destination):
        self.write_token(APTokenTypes.COPY, destination, (amount, source))


class Z2PatchExtensions(APPatchExtension):
    game = "Zelda II: The Adventure of Link"

    @staticmethod
    def repoint_vanilla_tables(caller: APProcedurePatch, rom: LocalRom) -> bytes:
        rom = LocalRom(rom)
        version_check = rom.read_bytes(0x3FF0A0, 16)
        version_check = version_check.split(b'\x00', 1)[0]
        version_check_str = version_check.decode("ascii")
        client_version = world_version
        if client_version != version_check_str and version_check_str != "":
            raise Exception(f"Error! Patch generated on EarthBound APWorld version {version_check_str} doesn't match client version {client_version}! " +
                            f"Please use EarthBound APWorld version {version_check_str} for patching.")

        return rom.get_bytes()


def get_base_rom_bytes(file_name: str = "") -> bytes:
    base_rom_bytes = getattr(get_base_rom_bytes, "base_rom_bytes", None)
    if not base_rom_bytes:
        file_name = get_base_rom_path(file_name)
        base_rom_bytes = bytes(Utils.read_snes_rom(open(file_name, "rb")))

        basemd5 = hashlib.md5()
        basemd5.update(base_rom_bytes)
        rom_hash = basemd5.hexdigest
        if basemd5.hexdigest() != md5:
            raise Exception('Supplied Base Rom does not match known MD5 for US(1.0) release. '
                            'Get the correct game and version, then dump it')
        get_base_rom_bytes.base_rom_bytes = base_rom_bytes
    return base_rom_bytes


def get_base_rom_path(file_name: str = "") -> str:
    options: Utils.OptionsType = Utils.get_options()
    if not file_name:
        file_name = options["zelda2_options"]["rom_file"]
    if not os.path.exists(file_name):
        file_name = Utils.user_path(file_name)
    return file_name


# Fix hint text, I have a special idea where I can give it info on a random region
