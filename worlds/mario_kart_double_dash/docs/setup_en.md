# Setup Guide for Mario Kart: Double Dash!! Archipelago

## Requirements

You'll need the following components to be able to play MKDD AP:
* [Dolphin Emulator](https://dolphin-emu.org/download/). **We recommend using the latest release.**
    * For Linux users, you can use the flatpak package
    [available on Flathub](https://flathub.org/apps/org.DolphinEmu.dolphin-emu).
* A rom of Mario Kart: Double Dash!! (NTSC-U / USA version)
    * Format (`.iso`, `.rvz`) doesn't matter.

Optionally, you can also download:
* [Universal Tracker](https://github.com/FarisTheAncient/Archipelago/releases)
    * If you have Universal Tracker installed, the client will have a tracker page automatically.

## Setting Up a YAML

All players must provide the room host with a YAML file containing the settings for their world. Modify the template yaml from the [releases](https://github.com/aXu-AP/archipelago-double-dash/releases) page to your liking.
Once you're happy with your settings, provide the room host with your YAML file and proceed to the step "Connecting to a Room". If you want to play by yourself, you need to host the game yourself, see the next section.

## Self-hosting

* Place your YAML file in `Players` folder in your MultiworldGG installation (presumably `C:/Program Files/MultiworldGG/Players`).
* Open MultiworldGG Launcher and click Generate. A console window should pop up, do its stuff and close shortly.
* Click Host and locate your generated seed named `AP_#######.zip` at `output` folder in your MultiworldGG installation (presumably `C:/Program Files/MultiworldGG/output`).

## Connecting to a Room

Unlike most randomizers, MKDD AP doesn't need you to patch your rom beforehand. Everything is done at runtime.
Do note, that using the randomizer unlocks everything in your save of MKDD and you will probably make unrealistically good time trials times. So if you care for your vanilla save, you should do a backup of your save first!
* Open Mario Kart Double Dash Client from MultiworldGG Launcher.
* Open Dolphin and launch the game.
  * At this point, the client should say "Patch Applied".
  * **Important!** Do not go further than the player count selection screen before you are connected to the host!
* Write your host connection info in the box at the top of the client (if you are hosting yourself it's `localhost`) and press enter.
* Write your slot/player name (if you didn't modify the YAML then it's `Player1`) into the box at the bottom and press enter.

## Playing the Game

You should now get checks whenever you finish races. To see what is currently unlocked, type `/unlocked` in the client. To see what checks you can do, use Tracker page located at the top of the client (if you installed Universal Tracker).

## Troubleshooting

* The game crashes when I try to select a character.
  * You probably aren't connected to a server. Restart the game and ensure you have connection.
* I can't select character X.
  * The characters need to be unlocked by completing checks. The game currently doesn't give any visual indication what is unlocked, but you can use `/unlocked` command in the client to see your current status.
  * At the beginning you may have only a few characters unlocked on a specific row. There might not be a path for the cursor to go there. Try picking characters via random (L+R) until you get what you want. Think of this as a part of the game :)
* The client doesn't register any checks.
  * Restart both the game and the client.
* Where's my patch?
  * There's no patch, use vanilla rom.
* Can I use ar/gecko cheat codes?
  * Most of them should work.
  * If you find a cheat that doesn't work and you would like it to work, you can open an issue and we'll try to look into it.
* I unlocked All Cup Tour but it doesn't show up.
  * This is a visual bug. The cup should still be selectable even if it's invisible.