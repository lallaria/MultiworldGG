from names import sonic_heroes_level_names, sonic_heroes_story_names

key_sanity_key_amounts = [
            [
                3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3
            ],
            [
                3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3
            ],
            [
                2, 3, 2, 3, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3
            ],
            [
                2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3
            ]
        ]



#0x9393165d: "Seaside Hill Sonic Act 1 Bonus Key 1",

id = 0x9393165d


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
