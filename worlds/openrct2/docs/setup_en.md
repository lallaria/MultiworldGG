# OpenRCT2 Setup Guide:


## Quick Links
- [Main Page](../../../games/OpenRCT2/info/en)
- [Options Page](../../../games/OpenRCT2/player-options)
- [OpenRCT2 Plugins](https://openrct2plugins.org/)

## Required Software

- Any Operating System capable of running both Archipelago and OpenRCT2 (Linux, Mac, or Windows are all fine)
- One of the following:  
  - [Roller Coaster Tycoon 2](https://www.humblebundle.com/store/rollercoaster-tycoon-2-triple-thrill-pack) for PC
    - (Optional if you want RCT1 scenarios)
     [Roller Coaster Tycoon](https://www.humblebundle.com/store/rollercoaster-tycoon-deluxe)
  - [Roller Coaster Tycoon Classic](https://www.humblebundle.com/store/rollercoaster-tycoon-classic) for PC  
- [OpenRCT2](https://openrct2.io/)

## Optional Software
- [Archipelago Scenarios](https://github.com/Crazycolbster/rollercoaster-tycoon-randomizer/releases/tag/v0.1.16-beta) that can be selected as scenarios for your seed.

## Overview

You'll be using OpenRCT2 to run the Archipelago plugin, which will connect to the built-in OpenRCT2 client in \
Archipelago to join multiworlds. This will first entail installing OpenRCT2 and the plugin, and finally connecting\
the game to the client, and the client to the server.

### Install

If you haven't installed OpenRCT2 or the base game(s), follow the guide for your operating system on the official\
[OpenRCT2 Website](https://docs.openrct2.io/en/latest/).

### Install the Roller Coaster Tycoon Randomizer Plugin

* Once OpenRCT2 is up and running, you'll need to install the 
[Roller Coaster Tycoon Randomizer plugin](https://openrct2plugins.org/plugin/R_kgDOGmXTVQ/rollercoaster-tycoon-randomizer).
* On the main menu of OpenRCT2, click the toolbox menu icon and select "Open custom content folder".
* Save the `.js` file to the "plugin" folder within.
* If you have the "Archipelago Madness" scenarios, copy the .park files to the "scenario" folder.

## Generate a MultiWorld Game

1. Visit the [Player Options](../../../games/OpenRCT2/player-options) page and configure the game-specific options to taste.

* By default, these options will only use levels from Roller Coaster Tycoon 2. If you own Roller Coaster Tycoon 1 or any of the expansion packs for either game, you may select the scenario for use in your game of MultiworldGG.

2. Export your yaml file and use it to generate a new randomized game or generate a game on the spot.

*For instructions on how to generate an MultiworldGG game, refer to the [MultiworldGG Setup Guide](../../../../tutorial/Archipelago/setup/en).*

## Joining a MultiWorld Game

1. Launch the game.

2. Select the scenario you chose in your options file. If this was randomized, or you otherwise don't know what scenario to select, you can either look at the spoiler log or select any scenario. Upon attempting to start, the
game will inform you which scenario you should be playing.

3. Launch the OpenRCT2 Client from the MultiworldGG program.

4. Click the "Archipelago" button on the menu that pops up in your scenario. Once the client is launched, they should automatically connect, and you can connect to the server. 
Type your server address and port in the "Connect" box at the top of the client, connect.

5. When asked by the client, put in the name for your slot and confirm.

6.  You'll be able to select the "Start Game!" button. If the randomizer menu doesn't appear at the start of the scenario, select the "RCTRando Options" menu item from the map tab and ensure the "Enable Randomizer" box is checked.

7. Begin your game of MultiworldGG! All your locations/checks/goals can be found in the "Archipelago Checks!" menu under the map tab.

## Game Commands

Game commands may only be executed from within OpenRCT2, by typing the following from the unlock shop, including the 
exclamation points: `!!`.

- `!!help` Prints the help menu.
- `!!toggleDeathLink` Enables/Disables Deathlink in game.
- `!!setMaxSpeed x` Sets the maximum speed the game will allow, from 1 to 5.
- `!!resendChecks` Resends all the purchased checks, in case the connector is bad at its job.
- `!!addSkip` Cheats in a skip for the unlock shop. This is on the honor system.

## Multiplayer

At the moment, same-world multiplayer is not available, and is planned for release in the short to medium term.