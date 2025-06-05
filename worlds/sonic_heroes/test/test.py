sonic_heroes_story_names: dict[int, str] = {
    0: "Sonic",
    1: "Dark",
    2: "Rose",
    3: "Chaotix"
}

sonic_heroes_level_names: dict[int, str] = {
    1: "Seaside Hill",
    2: "Ocean Palace",
    3: "Grand Metropolis",
    4: "Power Plant",
    5: "Casino Park",
    6: "Bingo Highway",
    7: "Rail Canyon",
    8: "Bullet Station",
    9: "Frog Forest",
    10: "Lost Jungle",
    11: "Hang Castle",
    12: "Mystic Mansion",
    13: "Egg Fleet",
    14: "Final Fortress"
}

key_sanity_key_amounts = [
            [
                3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3
            ],
            [
                3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3
            ],
            [
                2, 3, 3, 3, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3
            ],
            [
                3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3
            ]
        ]


checkpoint_amounts = [ #total 246
            [ #Sonic
                5, 4, 4, 4, 3, 4, 6, 4, 3, 5, 3, 4, 5, 3 #57
            ],
            [ #Dark
                4, 5, 4, 4, 3, 4, 6, 5, 3, 5, 3, 4, 5, 3 #50
            ],
            [ #Rose
                2, 2, 3, 2, 1, 3, 4, 2, 2, 3, 3, 2, 2, 2 #33
            ],
            [ #Chaotix
                4, 2, 4, 3, 3, 2, 5, 4, 3, 4, 2, 5, 4, 3 #48
            ],
            [ #SuperHard
                4, 5, 4, 4, 3, 4, 6, 4, 3, 5, 3, 5, 5, 3 #58
            ]
        ]

"""

id = 0x9393165d# "Seaside Hill Sonic Act 1 Bonus Key 1",

#Act 1
for storynum in range(len(key_sanity_key_amounts)):
    for missionindex in range(len(key_sanity_key_amounts[storynum])):
        for x in range(key_sanity_key_amounts[storynum][missionindex]):
            if x + 1 == 4:
                print(f"{hex(id)}: \"SUPER SECRET HIDDEN Act 1 Bonus Key\",")
            else:
                print(f"{hex(id)}: \"{sonic_heroes_level_names[missionindex + 1]} {sonic_heroes_story_names[storynum]} Act 1 Bonus Key {x + 1}\",")
            id += 1

#Act 2
for storynum in range(len(key_sanity_key_amounts)):
    for missionindex in range(len(key_sanity_key_amounts[storynum])):
        for x in range(key_sanity_key_amounts[storynum][missionindex]):
            if x + 1 == 4:
                print(f"{hex(id)}: \"SUPER SECRET HIDDEN Act 2 Bonus Key\",")
            else:
                print(f"{hex(id)}: \"{sonic_heroes_level_names[missionindex + 1]} {sonic_heroes_story_names[storynum]} Act 2 Bonus Key {x + 1}\",")
            id += 1


#No Act
for storynum in range(len(key_sanity_key_amounts)):
    for missionindex in range(len(key_sanity_key_amounts[storynum])):
        for x in range(key_sanity_key_amounts[storynum][missionindex]):
            if x + 1 == 4:
                print(f"{hex(id)}: \"SUPER SECRET HIDDEN Bonus Key\",")
            else:
                print(f"{hex(id)}: \"{sonic_heroes_level_names[missionindex + 1]} {sonic_heroes_story_names[storynum]} Bonus Key {x + 1}\",")
            id += 1


        
     
id = 0x93932000#: "Seaside Hill Sonic Checkpoint 1"       

#No Act
for storynum in range(4):
    for missionindex in range(14):
        for x in range(checkpoint_amounts[storynum][missionindex]):
            print(
                f"{hex(id)}: \"{sonic_heroes_level_names[missionindex + 1]} {sonic_heroes_story_names[storynum]} Checkpoint {x + 1}\",")
            id += 1

#Act 1
for storynum in range(4):
    for missionindex in range(14):
        for x in range(checkpoint_amounts[storynum][missionindex]):
            print(
                f"{hex(id)}: \"{sonic_heroes_level_names[missionindex + 1]} {sonic_heroes_story_names[storynum]} Act 1 Checkpoint {x + 1}\",")
            id += 1

#Act 2
for storynum in range(4):
    for missionindex in range(14):
        for x in range(checkpoint_amounts[storynum][missionindex]):
            print(
                f"{hex(id)}: \"{sonic_heroes_level_names[missionindex + 1]} {sonic_heroes_story_names[storynum]} Act 2 Checkpoint {x + 1}\",")
            id += 1



#Super Hard
for missionindex in range(14):
    for x in range(checkpoint_amounts[4][missionindex]):
        print(f"{hex(id)}: \"{sonic_heroes_level_names[missionindex + 1]} Super Hard Mode Checkpoint {x + 1}\",")
        id += 1

"""