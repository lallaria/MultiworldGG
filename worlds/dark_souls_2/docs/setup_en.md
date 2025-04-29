# Dark Souls II Randomizer Setup Guide

## Installing the mod

The mod works with a single `dinput8.dll` file.

- Download the dll and apworld files from the [latest release](https://github.com/WildBunnie/DarkSoulsII-Archipelago/releases) for your game version.
- Rename the dll file to `dinput8.dll`.
- Place the `dinput8.dll` file inside the `Game` folder in the game folder, next to the executable.
- If playing on linux add `WINEDLLOVERRIDES="dinput8.dll=n,b" %command%` to the game's launch options on steam.

### Joining a game

- (Optional) Backup your save just to make sure the mod doesn't mess with it.
- Simply launch the game and a console will launch together with it.
- In that console type `/connect server_address:port slot_name password`, replacing the correct values. The password is optional and the slot name is the name you placed in the yaml file.
- For example, if you host in MultiworldGG's website it would look something like `/connect multiworldgg:12345 JohnSouls`.
- Start a new game and enjoy.

## Frequently Asked Questions

### **Do I need to play in offline mode? Is it safe to play online?**
The mod forces the game to start in offline mode. We do not offer a version of the mod that works online. If you have a firewall rule to block Dark Souls II it will make the mod unable to communicate with archipelago (unless it's hosted locally) so you will have to deactivate that rule to play the mod.

### **I get `Access is denied` when trying to connect to archipelago.**
This happens if you have a rule in your firewall blocking Dark Souls II like mentioned above.

### The game crashes when joining a server.
This can happen for multiple reasons:
  - Verify that you are on the lastest version of the game, anything but the latest steam version is unsuported.