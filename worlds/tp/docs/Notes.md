# Commands

wsl bash "worlds/twilight_princess_apworld/build/build.sh"
wsl dos2unix /mnt/c/Users/Ethan/Documents/Projects/Twilight_Princess_apworld/build/build.sh

python -u "worlds\twilight_princess_apworld\build\run_test.py"
python fuzz.py -r100 -j 10 -m 1-3 -m worlds\twilight_princess_apworld\docs\fuzzmeta.yaml -g "twilight_princess_apworld"
python -u "worlds\twilight_princess_apworld\build\fuzzParser.py"

# Testing procedure

1. Run testing suite
2. Generate template yaml and replace into folder
3. Generate with the new yaml
4. Fuzzing
5. Use Debug client to ensure server data works

# Things to add

Cave of orderals ignore
dungeon rewards pregression

build out generation logic to handle intergration settings
-If faron woods closed and dungeon items are any_dungeon overide to make forest temple items own_dungeon
-If faron woods closed pre-fill items into world to ensure accessiblity of later locations.
-Boss Rewards
--Search through prority item pool and choose items to place on bosses. Or place shadows / shards

# Failed Seeds

657286117, 972369101
Palace of twilight small keys fail to place when Any-Own Dungeon

# Setting encode

castleRequirements
-0: Open
-1: Fused Shadows
-2: Mirron Shards
-3: All Dungeons
-4: Vanilla
palaceRequirements
-0: Open
-1: Fused Shadow
-2: Mirror Shards
-3: Vanilla
faronWoodsLogic
-0: Open
-1: Closed
smallKeySettings
-0: Vanilla
-1: Own Dungeon
-2: Any Dungeon
-3: Keysanity
-4: Keysy
bigKeySettings
-0: Vanilla
-1: Own Dungeon
-2: Any Dungeon
-3: Keysanity
-4: Keysy
mapAndCompasSettings
-0: Vanilla
-1: Own Dungeon
-2: Any Dungeon
-3: Anywhere
-4: Start With
skipPrologue
-true
-false
faronTwilightCleared
-true
-false
EldinTwilightCleared
-true
-false
lanayruTwilightCleared
-true
-false
skipMdh
-true
-false
skipMinorCutscenes
-true
-false
fastIronBoots
-true
-false
quickTransform
-true
-false
transformAnywhere
-true
-false
increaseWallet
-true
-false
modifyShopModels
-true
-false
goronMinesEntrance
-0: Closed
-1: No Wrestling
-2: Open
skipLakebedEntrance
-true
-false
skipArbitersEntrance
-true
-false
skipSnowpeakEntrance
-true
-false
totEntrance
-0: Closed
-1: Open Grove
-2: Open
cityInTheSkyEnterance
-true
-false
instantText
-true
-false
openMap
-true
-false
increaseSpinnerSpeed
-true
-false
openDot
-true
-false
damageMagnification
-1: Vanilla
-2: Double
-3: Triple
-4: Quadruple
-5: OHKO
bonksDoDamage
-true
-false
skipMajorCutscenes
-true
-false
startingToD
-0: Morning
-1: Noon (s)
-2: Evening
-3: Night
startingItems
-list of hexs
