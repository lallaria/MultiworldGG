# Here Comes Niko! Setup Guide

## Required Software

- [Here Comes Niko!](https://store.steampowered.com/app/925950/Here_Comes_Niko/) (Steam)
- [Here Comes Niko! Randomizer Mod](https://github.com/niieli/NikoArchipelagoMod/releases/latest)
- [BepInEx 5.4.21 (Unity Mono x64)](https://github.com/BepInEx/BepInEx/tree/v5.4.21)

## Installation

### Install BepInEx

1. Download [BepInEx 5.4.21 (Unity Mono x64)](https://github.com/BepInEx/BepInEx/tree/v5.4.21)
2. Extract the contents of the BepInEx .zip file into your Here Comes Niko! game directory:
   - Default Steam path: `C:\Program Files (x86)\Steam\steamapps\common\Here Comes Niko`
   - If using a custom installation, adjust accordingly.
3. Run the game once to allow BepInEx to create necessary folders.

### Install The Here Comes Niko! Randomizer Mod

1. Download the latest release of the [Here Comes Niko! Randomizer Mod](https://github.com/niieli/NikoArchipelagoMod/releases/latest).
2. Navigate to your game directory and open the `BepInEx/plugins` folder.
3. Extract the contents of the downloaded .zip file **directly** into the `BepInEx/plugins` folder.
   - Ensure the mod file path is **`BepInEx/plugins/NikoArchipelago.dll`**, not inside a subfolder like `BepInEx/plugins/NikoArchipelagoMod/NikoArchipelago.dll`.
4. Launch the game, if the mod is installed correctly, the title screen will be modified.

## Connecting

1. Open the in-game menu and click on the **Archipelago logo**.
2. Enter your **connection information** on the left side.
3. Click **Connect**—you should load into **Home** with a blank save.
   - If a save with the same **name, seed, and slot number** exists, it will load that save instead.
4. To delete Archipelago saves, go to:
   - `...\AppData\LocalLow\Frog Vibes\Here Comes Niko!\Archipelago`