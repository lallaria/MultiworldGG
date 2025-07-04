# Pokémon Crystal

## Where is the options page?

You can read through all the options and generate a YAML [here](../player-options).

## What does randomization do to this game?

Some changes have been made to the logic for this randomizer:

- The trainer battle on Route 30 is resolved as soon as you talk to Mr. Pokémon, skipping a visit to Professor Elm
- The director is always in the underground warehouse, even when Radio Tower isn't occupied
- The card key door in Goldenrod Department Store B1F unlocks with the Card Key in your Pack
- Time based checks such as the Day of the Week siblings and the Celadon Mansion roof guy are always available
    - The hidden items under Freida and Wesley have been moved a tile across to remain accessible
- The Ship between Olivine and Vermilion is always present in non-Johto-Only-games, even before entering Hall of Fame,
  and available to
  ride with the S.S. Ticket
- Magnet train between Goldenrod and Saffron is available to ride with the Pass before power is restored to Kanto
- Misty is always in Cerulean Gym
- A ledge on Route 45 has been moved so all items and trainers can be accessed in 2 passthroughs
- If the HM Badges Requirement option is set to `add_kanto`, HMs can be used with the following badges in addition to
  their vanilla badges:
    - HM01 Cut - Cascade Badge
    - HM02 Fly - Thunder Badge
    - HM03 Surf - Soul Badge
    - HM04 Strength - Rainbow Badge
    - HM05 Flash - Boulder Badge
    - HM06 Whirlpool - Volcano Badge
    - HM07 Waterfall - Earth Badge
- Tin Tower 1F is logically accessible once you obtain the Clear Bell.
- Ho-Oh is accessible once the aforementioned condition is met, and you have the Rainbow Wing. Both are items in the
  multiworld

## What items and locations get randomized?

By default, items from item balls and items given by NPCs are randomized.
Badges can be either vanilla, shuffled or randomized. Pokégear and its card modules can be vanilla or shuffled.
If Johto Only mode is enabled, items in Kanto will not be randomized and Kanto will be inaccessible.

There are options to include more items in the pool:

- Randomize Hidden Items: Adds hidden items to the pool
- Randomize Berry Trees: Adds berry tree items to the pool
- Trainersanity: Adds a reward for beating trainers to the pool
- Dexsanity: A Pokémon's Dex entry can hold a check. This is tied to specific Pokémon
- Dexcountsanity: A certain amount of Dex entries hold checks. This is not tied to specific Pokémon but a total

## What other changes are made to the game?

Many additional quality of life changes have been implemented:

- A new text speed option, Instant, is added to the options menu in game. This speeds up text and allows holding A to
  quickly speed through dialog
- When battle scenes are turned off, HP reduction and XP gain animations are skipped
- You can hold B to run
- Lag in menu has been removed
- The Bicycle can be used indoors
- If a repel runs out and you have more in your Pack, it will prompt to use another
- You may advance to Violet City after speaking to Mr. Pokémon, without returning to New Bark Town first
- Pokémon growth rates are normalized (Medium-Fast for non-Legendary Pokémon, Slow for Legendary Pokémon)
- The clock reset password system has been removed, you can reset the clock with Down + Select + B on the title screen
- Trade evolutions have been changed to make them possible in a solo run of the game:
    - Regular trade evolutions now evolve at level 37
    - Held item trade evolutions evolve when their evolution item is used on them, as you would an evolution stone
- Espeon and Umbreon evolve with the Sun Stone and Moon Stone respectively
- The Celebi Event can be activated by giving the multiworld item GS-Ball to Kurt after clearing Slowpoke Well
- You can respawn all static events by talking to the Time Capsule person in the second floor of any PokéCenter
- You can teleport back to your starting town by selecting "Warp to Home" in the main menu before you load into the
  overworld

## What does another world's item look like in Pokémon Crystal?

Items from other worlds will print the item name and the name of the receiving player when collected. Due to
limitations with the game's text, these names are truncated at 16 characters, and special characters not found in the
font are replaced with question marks.

## When the player receives an item, what happens?

A sound effect will play when an item is received if the Item Receive Sound option is enabled. Different sounds will
play to distinguish progression items and traps.

## Can I play offline?

Yes, the game does not need to be connected to the client for solo seeds. Connection is only required for sending and
receiving items.
