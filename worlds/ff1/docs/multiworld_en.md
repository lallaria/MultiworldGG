# Final Fantasy 1 (NES) Multiworld Setup Guide

## Required Software

- The FF1Client
    - Bundled with MultiworldGG: [MultiworldGG Releases Page](https://github.com/MultiworldGG/MultiworldGG/releases)
- The BizHawk emulator. Versions 2.3.1 and higher are supported. Version 2.7 is recommended
    - [BizHawk at TASVideos](https://tasvideos.org/BizHawk)
- Your legally obtained Final Fantasy (USA Edition) ROM file, probably named `Final Fantasy (USA).nes`. Neither
  Multiworld.gg nor the Final Fantasy Randomizer Community can supply you with this.

## Installation Procedures

1. Download and install the latest version of MultiworldGG.
    1. On Windows, download Setup.Archipelago.<HighestVersion\>.exe and run it
2. Assign EmuHawk version 2.3.1 or higher as your default program for launching `.nes` files.
    1. Extract your BizHawk folder to your Desktop, or somewhere you will remember. Below are optional additional steps
       for loading ROMs more conveniently
        1. Right-click on a ROM file and select **Open with...**
        2. Check the box next to **Always use this app to open .nes files**
        3. Scroll to the bottom of the list and click the grey text **Look for another App on this PC**
        4. Browse for `EmuHawk.exe` located inside your BizHawk folder (from step 1) and click **Open**.

## Obtaining your MultiworldGG yaml file and randomized ROM

Unlike most other Multiworld.gg games Final Fantasy 1 is randomized by the main randomizer at
the [Final Fantasy Randomizer Homepage](https://finalfantasyrandomizer.com/).

Generate a game by going to the site and performing the following steps:

1. Select the randomization options (also known as `Flags` in the community) of your choice. If you do not know what you
   prefer, or it is your first time we suggest starting with the 'Shard Hunt' preset (which requires you to collect a
   number of shards to go to the end dungeon) or the 'Beginner' preset if you prefer to kill the original fiends.
2. Go to the `Goal` tab and ensure `Archipelago` is enabled. Set your player name to any name that represents you.
3. Upload your `Final Fantasy(USA).nes` (and click `Remember ROM` for the future!)
4. Press the `NEW` button beside `Seed` a few times
5. Click `GENERATE ROM`

It should download two files. One is the `*.nes` file which your emulator will run, and the other is the yaml file
required by MultiworldGG

At this point, you are ready to join the multiworld. If you are uncertain on how to generate, host, or join a multiworld,
please refer to the [game agnostic setup guide](/tutorial/MultiworldGG/setup/en).

## Running the Client Program and Connecting to the Server

Once the MultiworldGG server has been hosted:

1. Navigate to your MultiworldGG install folder and run `MultiworldGGFF1Client.exe`
2. Notice the `/connect command` on the server hosting page (It should look like `/connect multiworld.gg:*****`
   where ***** are numbers)
3. Type the connect command into the client OR add the port to the pre-populated address on the top bar (it should
   already say `multiworld.gg`) and click `connect`

### Running Your Game and Connecting to the Client Program

1. Open EmuHawk 2.3.1 or higher and load your ROM OR click your ROM file if it is already associated with the
   extension `*.nes`
2. Navigate to where you installed MultiworldGG, then to `data/lua`, and drag+drop the `connector_ff1.lua` script onto
   the main EmuHawk window.
    1. You could instead open the Lua Console manually, click `Script` 〉 `Open Script`, and navigate to
       `connector_ff1.lua` with the file picker.
    2. If it gives a `NLua.Exceptions.LuaScriptException: .\socket.lua:13: module 'socket.core' not found:` exception
       close your emulator entirely, restart it and re-run these steps
    3. If it says `Must use a version of BizHawk 2.3.1 or higher`, double-check your BizHawk version by clicking **
       Help** -> **About**

## Play the game

When the client shows both NES and server are connected, you are good to go. You can check the connection status of the
NES at any time by running `/nes`

### Other Client Commands

All other commands may be found on the [MultiworldGG Server and Client Commands Guide](/tutorial/MultiworldGG/commands/en)
.
