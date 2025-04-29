# Hatsune Miku Project DIVA Mega Mix+ Setup Guide

## Requirements 

Only the base game is required in order to play this game.
DLC can be toggled on in the options.

## Setup Diva Mod

- Install the Archipelago mod, either manually or through the Diva Mod Manager, Mod can be found here: https://gamebanana.com/mods/514140
- If not using Diva Mod Manager, make sure to install Diva Mod Loader beforehand
- ExPatch mod also required if you are unsure if you have all songs & difficulties unlocked: https://gamebanana.com/mods/388083
- If you are unfamiliar with Diva modding, here's a helpful guide, I recommend the mod manager over manual: https://docs.google.com/document/d/1jvG_RGMe_FtlduvD8WwXdfA85I1O4Tde0DfRDM4aeWk/edit
- To play AP with modded songs, follow this guide here: https://docs.google.com/document/d/17NwFcPzmt5fnXz0GBvrJTlF40fCNcv052kWpM0OQ66o/edit?usp=sharing

### Eden Core Specifics (Modded)

- If using Eden Core, Eden Core must be at the end of the mod loading order after Archipelago.
- If using Eden Core, and it is included in your modded Json, it goes before Archipelago in the mod load order like other mods

## Joining a multiworld:

- Run MultiWorldGGLauncher.exe and click "Mega Mix Client".
- On your first launch, the client should ask you to select your Diva mod install folder (example: D:\SteamLibrary\steamapps\common\Hatsune Miku Project DIVA Mega Mix Plus) on steam (this can be changed later via the host.yaml file in your MultiWorldGG base folder).
- Connect to the room via the room URL.
- Launch Mega Mix after connecting
- If your song list in game has changed to the starting songs from MultiWorldGG, you're ready to go! If not, try pressing the reload key and checking the song list again.


## Troubleshooting

- Whenever you get sent a song, to have it show up in the song list you must reload the game with the reload key, it's not a bug if a song doesn't appear until after a reload. However if a song still doesn't appear after a reload please report it in the discord.
- Make sure the client is connected when you beat a song or it won't count the location as checked until you do it again while connected.
- Please make sure you're using the latest version of either Diva Mod Loader, or Diva Mod Manager
- To use the mod with SongLimitPatch or other mods that use SLP (such as EdenCore), in the config.toml file (ArchipelagoMod/config.toml), set the dll option to ArchipelagoModSLP.dll, swap back to the normal DLL if not using a SongLimitPatch mod.