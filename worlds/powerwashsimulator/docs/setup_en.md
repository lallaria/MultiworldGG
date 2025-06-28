# Powerwash Simulator Setup Guide

## How to install
- Download [BepInEx 6.0.0-pre1](https://github.com/BepInEx/BepInEx/releases/download/v6.0.0-pre.1/BepInEx_UnityIL2CPP_x64_6.0.0-pre.1.zip).
- Extract the BepInEx zip folder you downloaded from the previous step into your game's install directory (For example: C:\Program Files (x86)\Steam\steamapps\common\PowerWash Simulator)
- Launch the game and close it. This will finalize the BepInEx installation.
- Download and extract the `SW_CreeperKing.ArchipelagoMod.Zip` from the [release page](https://github.com/SWCreeperKing/PowerwashSimAP/releases/latest).
    - Copy the `SW_CreeperKing.ArchipelagoMod` folder from the release zip into `BepInEx/plugins` under your game's install directory.
    - If there is no `BepInEx/plugins` folder: 
      - try running as administrator
      - if using linux/wine: type "WINEDLLOVERRIDES="winhttp=n,b" %command%" into launch options
      - check to see if your antivirus or something else that maybe interfering with BepInEx
- Launch the game again and you should see the connection input on the top left of the title screen!
- To uninstall the mod, either remove/delete the `SW_CreeperKing.ArchipelagoMod` folder from the plugins folder or rename the winhttp.dll file located in the game's root directory (this will disable all installed mods from running).