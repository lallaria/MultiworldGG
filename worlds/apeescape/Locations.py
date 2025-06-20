from typing import Optional, Dict, Set
from BaseClasses import Location
from worlds.apeescape.Strings import AELocation, AEDoor

base_location_id = 128000000


class ApeEscapeLocation(Location):
    game: str = "Ape Escape"

GROUPED_LOCATIONS: Dict[str, Set[str]] = {}

location_table = {
    # 1-1 Fossil Field
    AELocation.W1L1Noonan.value: 1,
    AELocation.W1L1Jorjy.value: 2,
    AELocation.W1L1Nati.value: 3,
    AELocation.W1L1TrayC.value: 4,
    # 1-2 Primordial Ooze
    AELocation.W1L2Shay.value: 5,
    AELocation.W1L2DrMonk.value: 6,
    AELocation.W1L2Grunt.value: 7,
    AELocation.W1L2Ahchoo.value: 8,
    AELocation.W1L2Gornif.value: 9,
    AELocation.W1L2Tyrone.value: 10,
    # 1-3 Molten Lava
    AELocation.W1L3Scotty.value: 11,
    AELocation.W1L3Coco.value: 12,
    AELocation.W1L3JThomas.value: 13,
    AELocation.W1L3Mattie.value: 14,
    AELocation.W1L3Barney.value: 15,
    AELocation.W1L3Rocky.value: 16,
    AELocation.W1L3Moggan.value: 17,
    # 2-1 Thick Jungle
    AELocation.W2L1Marquez.value: 18,
    AELocation.W2L1Livinston.value: 19,
    AELocation.W2L1George.value: 20,
    AELocation.W2L1Maki.value: 21,
    AELocation.W2L1Herb.value: 22,
    AELocation.W2L1Dilweed.value: 23,
    AELocation.W2L1Mitong.value: 24,
    AELocation.W2L1Stoddy.value: 25,
    AELocation.W2L1Nasus.value: 26,
    AELocation.W2L1Selur.value: 27,
    AELocation.W2L1Elehcim.value: 28,
    AELocation.W2L1Gonzo.value: 29,
    AELocation.W2L1Alphonse.value: 30,
    AELocation.W2L1Zanzibar.value: 31,
    # 2-2 Dark Ruins
    AELocation.W2L2Mooshy.value: 32,
    AELocation.W2L2Kyle.value: 33,
    AELocation.W2L2Cratman.value: 34,
    AELocation.W2L2Nuzzy.value: 35,
    AELocation.W2L2Mav.value: 36,
    AELocation.W2L2Stan.value: 37,
    AELocation.W2L2Bernt.value: 38,
    AELocation.W2L2Runt.value: 39,
    AELocation.W2L2Hoolah.value: 40,
    AELocation.W2L2Papou.value: 41,
    AELocation.W2L2Kenny.value: 42,
    AELocation.W2L2Trance.value: 43,
    AELocation.W2L2Chino.value: 44,
    # 2-3 Cryptic Relics
    AELocation.W2L3Troopa.value: 45,
    AELocation.W2L3Spanky.value: 46,
    AELocation.W2L3Stymie.value: 47,
    AELocation.W2L3Pally.value: 48,
    AELocation.W2L3Freeto.value: 49,
    AELocation.W2L3Jesta.value: 50,
    AELocation.W2L3Bazzle.value: 51,
    AELocation.W2L3Crash.value: 52,
    # 4-1 Crabby Beach
    AELocation.W4L1CoolBlue.value: 53,
    AELocation.W4L1Sandy.value: 54,
    AELocation.W4L1ShellE.value: 55,
    AELocation.W4L1Gidget.value: 56,
    AELocation.W4L1Shaka.value: 57,
    AELocation.W4L1MaxMahalo.value: 58,
    AELocation.W4L1Moko.value: 59,
    AELocation.W4L1Puka.value: 60,
    # 4-2 Coral Cave
    AELocation.W4L2Chip.value: 61,
    AELocation.W4L2Oreo.value: 62,
    AELocation.W4L2Puddles.value: 63,
    AELocation.W4L2Kalama.value: 64,
    AELocation.W4L2Iz.value: 65,
    AELocation.W4L2Jux.value: 66,
    AELocation.W4L2BongBong.value: 67,
    AELocation.W4L2Pickles.value: 68,
    # 4-3 Dexter's Island
    AELocation.W4L3Stuw.value: 69,
    AELocation.W4L3TonTon.value: 70,
    AELocation.W4L3Murky.value: 71,
    AELocation.W4L3Howeerd.value: 72,
    AELocation.W4L3Robbin.value: 73,
    AELocation.W4L3Jakkee.value: 74,
    AELocation.W4L3Frederic.value: 75,
    AELocation.W4L3Baba.value: 76,
    AELocation.W4L3Mars.value: 77,
    AELocation.W4L3Horke.value: 78,
    AELocation.W4L3Quirck.value: 79,
    # 5-1 Snowy Mammoth
    AELocation.W5L1Popcicle.value: 80,
    AELocation.W5L1Iced.value: 81,
    AELocation.W5L1Denggoy.value: 82,
    AELocation.W5L1Skeens.value: 83,
    AELocation.W5L1Rickets.value: 84,
    AELocation.W5L1Chilly.value: 85,
    # 5-2 Frosty Retreat
    AELocation.W5L2Storm.value: 86,
    AELocation.W5L2Qube.value: 87,
    AELocation.W5L2Gash.value: 88,
    AELocation.W5L2Kundra.value: 89,
    AELocation.W5L2Shadow.value: 90,
    AELocation.W5L2Ranix.value: 91,
    AELocation.W5L2Sticky.value: 92,
    AELocation.W5L2Sharpe.value: 93,
    AELocation.W5L2Droog.value: 94,
    # 5-3 Hot Springs
    AELocation.W5L3Punky.value: 95,
    AELocation.W5L3Ameego.value: 96,
    AELocation.W5L3Roti.value: 97,
    AELocation.W5L3Dissa.value: 98,
    AELocation.W5L3Yoky.value: 99,
    AELocation.W5L3Jory.value: 100,
    AELocation.W5L3Crank.value: 101,
    AELocation.W5L3Claxter.value: 102,
    AELocation.W5L3Looza.value: 103,
    # 7-1 Sushi Temple
    AELocation.W7L1Taku.value: 104,
    AELocation.W7L1Rocka.value: 105,
    AELocation.W7L1Maralea.value: 106,
    AELocation.W7L1Wog.value: 107,
    AELocation.W7L1Long.value: 108,
    AELocation.W7L1Mayi.value: 109,
    AELocation.W7L1Owyang.value: 110,
    AELocation.W7L1QuelTin.value: 111,
    AELocation.W7L1Phaldo.value: 112,
    AELocation.W7L1Voti.value: 113,
    AELocation.W7L1Elly.value: 114,
    AELocation.W7L1Chunky.value: 115,
    # 7-2 Wabi Sabi Wall
    AELocation.W7L2Minky.value: 116,
    AELocation.W7L2Zobbro.value: 117,
    AELocation.W7L2Xeeto.value: 118,
    AELocation.W7L2Moops.value: 119,
    AELocation.W7L2Zanabi.value: 120,
    AELocation.W7L2Buddha.value: 121,
    AELocation.W7L2Fooey.value: 122,
    AELocation.W7L2Doxs.value: 123,
    AELocation.W7L2Kong.value: 124,
    AELocation.W7L2Phool.value: 125,
    # 7-3 Crumbling Castle
    AELocation.W7L3Naners.value: 126,
    AELocation.W7L3Robart.value: 127,
    AELocation.W7L3Neeners.value: 128,
    AELocation.W7L3Gustav.value: 129,
    AELocation.W7L3Wilhelm.value: 130,
    AELocation.W7L3Emmanuel.value: 131,
    AELocation.W7L3SirCutty.value: 132,
    AELocation.W7L3Calligan.value: 133,
    AELocation.W7L3Castalist.value: 134,
    AELocation.W7L3Deveneom.value: 135,
    AELocation.W7L3Igor.value: 136,
    AELocation.W7L3Charles.value: 137,
    AELocation.W7L3Astur.value: 138,
    AELocation.W7L3Kilserack.value: 139,
    AELocation.W7L3Ringo.value: 140,
    AELocation.W7L3Densil.value: 141,
    AELocation.W7L3Figero.value: 142,
    AELocation.W7L3Fej.value: 143,
    AELocation.W7L3Joey.value: 144,
    AELocation.W7L3Donqui.value: 145,
    # 8-1 City Park
    AELocation.W8L1Kaine.value: 146,
    AELocation.W8L1Jaxx.value: 147,
    AELocation.W8L1Gehry.value: 148,
    AELocation.W8L1Alcatraz.value: 149,
    AELocation.W8L1Tino.value: 150,
    AELocation.W8L1QBee.value: 151,
    AELocation.W8L1McManic.value: 152,
    AELocation.W8L1Dywan.value: 153,
    AELocation.W8L1CKHutch.value: 154,
    AELocation.W8L1Winky.value: 155,
    AELocation.W8L1BLuv.value: 156,
    AELocation.W8L1Camper.value: 157,
    AELocation.W8L1Huener.value: 158,
    # 8-2 Specter's Factory
    AELocation.W8L2BigShow.value: 159,
    AELocation.W8L2Dreos.value: 160,
    AELocation.W8L2Reznor.value: 161,
    AELocation.W8L2Urkel.value: 162,
    AELocation.W8L2VanillaS.value: 163,
    AELocation.W8L2Radd.value: 164,
    AELocation.W8L2Shimbo.value: 165,
    AELocation.W8L2Hurt.value: 166,
    AELocation.W8L2String.value: 167,
    AELocation.W8L2Khamo.value: 168,
    # 8-3 TV Tower
    AELocation.W8L3Fredo.value: 169,
    AELocation.W8L3Charlee.value: 170,
    AELocation.W8L3Mach3.value: 171,
    AELocation.W8L3Tortuss.value: 172,
    AELocation.W8L3Manic.value: 173,
    AELocation.W8L3Ruptdis.value: 174,
    AELocation.W8L3Eighty7.value: 175,
    AELocation.W8L3Danio.value: 176,
    AELocation.W8L3Roosta.value: 177,
    AELocation.W8L3Tellis.value: 178,
    AELocation.W8L3Whack.value: 179,
    AELocation.W8L3Frostee.value: 180,
    # 9-1 Monkey Madness
    AELocation.W9L1Goopo.value: 181,
    AELocation.W9L1Porto.value: 182,
    AELocation.W9L1Slam.value: 183,
    AELocation.W9L1Junk.value: 184,
    AELocation.W9L1Crib.value: 185,
    AELocation.W9L1Nak.value: 186,
    AELocation.W9L1Cloy.value: 187,
    AELocation.W9L1Shaw.value: 188,
    AELocation.W9L1Flea.value: 189,
    AELocation.W9L1Schafette.value: 190,
    AELocation.W9L1Donovan.value: 191,
    AELocation.W9L1Laura.value: 192,
    AELocation.W9L1Uribe.value: 193,
    AELocation.W9L1Gordo.value: 194,
    AELocation.W9L1Raeski.value: 195,
    AELocation.W9L1Poopie.value: 196,
    AELocation.W9L1Teacup.value: 197,
    AELocation.W9L1Shine.value: 198,
    AELocation.W9L1Wrench.value: 199,
    AELocation.W9L1Bronson.value: 200,
    AELocation.W9L1Bungee.value: 201,
    AELocation.W9L1Carro.value: 202,
    AELocation.W9L1Carlito.value: 203,
    AELocation.W9L1BG.value: 204,
    AELocation.Specter.value: 205,
    # 9-2 Peak Point Matrix
    AELocation.Specter2.value: 206,

    # Coins
    AELocation.Coin1.value: 301,
    AELocation.Coin2.value: 302,
    AELocation.Coin3.value: 303,
    AELocation.Coin6.value: 306,
    AELocation.Coin7.value: 307,
    AELocation.Coin8.value: 308,
    AELocation.Coin9.value: 309,
    AELocation.Coin11.value: 311,
    AELocation.Coin12.value: 312,
    AELocation.Coin13.value: 313,
    AELocation.Coin14.value: 314,
    AELocation.Coin17.value: 317,
    AELocation.Coin19A.value: 295,
    AELocation.Coin19B.value: 296,
    AELocation.Coin19C.value: 297,
    AELocation.Coin19D.value: 298,
    AELocation.Coin19E.value: 299,
    AELocation.Coin21.value: 321,
    AELocation.Coin23.value: 323,
    AELocation.Coin24.value: 324,
    AELocation.Coin25.value: 325,
    AELocation.Coin28.value: 328,
    AELocation.Coin29.value: 329,
    AELocation.Coin30.value: 330,
    AELocation.Coin31.value: 331,
    AELocation.Coin32.value: 332,
    AELocation.Coin34.value: 334,
    AELocation.Coin35.value: 335,
    AELocation.Coin36A.value: 290,
    AELocation.Coin36B.value: 291,
    AELocation.Coin36C.value: 292,
    AELocation.Coin36D.value: 293,
    AELocation.Coin36E.value: 294,
    AELocation.Coin37.value: 337,
    AELocation.Coin38.value: 338,
    AELocation.Coin39.value: 339,
    AELocation.Coin40.value: 340,
    AELocation.Coin41.value: 341,
    AELocation.Coin44.value: 344,
    AELocation.Coin45.value: 345,
    AELocation.Coin46.value: 346,
    AELocation.Coin49.value: 349,
    AELocation.Coin50.value: 350,
    AELocation.Coin53.value: 353,
    AELocation.Coin54.value: 354,
    AELocation.Coin55.value: 355,
    AELocation.Coin58.value: 358,
    AELocation.Coin59.value: 359,
    AELocation.Coin64.value: 364,
    AELocation.Coin66.value: 366,
    AELocation.Coin73.value: 373,
    AELocation.Coin74.value: 374,
    AELocation.Coin75.value: 375,
    AELocation.Coin77.value: 377,
    AELocation.Coin78.value: 378,
    AELocation.Coin79.value: 379,
    AELocation.Coin80.value: 380,
    AELocation.Coin85.value: 385,
    AELocation.Coin84.value: 384,
    AELocation.Coin82.value: 382,

    # Mailboxes
    AELocation.Mailbox1.value: 401,
    AELocation.Mailbox2.value: 402,
    AELocation.Mailbox3.value: 403,
    AELocation.Mailbox4.value: 404,
    AELocation.Mailbox5.value: 405,
    AELocation.Mailbox6.value: 406,
    AELocation.Mailbox7.value: 407,
    AELocation.Mailbox8.value: 408,
    AELocation.Mailbox9.value: 409,
    AELocation.Mailbox10.value: 410,
    AELocation.Mailbox11.value: 411,
    AELocation.Mailbox12.value: 412,
    AELocation.Mailbox13.value: 413,
    AELocation.Mailbox14.value: 414,
    AELocation.Mailbox15.value: 415,
    AELocation.Mailbox16.value: 416,
    AELocation.Mailbox17.value: 417,
    AELocation.Mailbox18.value: 418,
    AELocation.Mailbox19.value: 419,
    AELocation.Mailbox20.value: 420,
    AELocation.Mailbox21.value: 421,
    AELocation.Mailbox22.value: 422,
    AELocation.Mailbox23.value: 423,
    AELocation.Mailbox24.value: 424,
    AELocation.Mailbox25.value: 425,
    AELocation.Mailbox26.value: 426,
    AELocation.Mailbox27.value: 427,
    AELocation.Mailbox28.value: 428,
    AELocation.Mailbox29.value: 429,
    AELocation.Mailbox30.value: 430,
    AELocation.Mailbox31.value: 431,
    AELocation.Mailbox32.value: 432,
    AELocation.Mailbox33.value: 433,
    AELocation.Mailbox34.value: 434,
    AELocation.Mailbox35.value: 435,
    AELocation.Mailbox36.value: 436,
    AELocation.Mailbox37.value: 437,
    AELocation.Mailbox38.value: 438,
    AELocation.Mailbox39.value: 439,
    AELocation.Mailbox40.value: 440,
    AELocation.Mailbox41.value: 441,
    AELocation.Mailbox42.value: 442,
    AELocation.Mailbox43.value: 443,
    AELocation.Mailbox44.value: 444,
    AELocation.Mailbox45.value: 445,
    AELocation.Mailbox46.value: 446,
    AELocation.Mailbox47.value: 447,
    AELocation.Mailbox48.value: 448,
    AELocation.Mailbox49.value: 449,
    AELocation.Mailbox50.value: 450,
    AELocation.Mailbox51.value: 451,
    AELocation.Mailbox52.value: 452,
    AELocation.Mailbox53.value: 453,
    AELocation.Mailbox54.value: 454,
    AELocation.Mailbox55.value: 455,
    AELocation.Mailbox56.value: 456,
    AELocation.Mailbox57.value: 457,
    AELocation.Mailbox58.value: 458,
    AELocation.Mailbox59.value: 459,
    AELocation.Mailbox60.value: 460,
    AELocation.Mailbox61.value: 461,
    AELocation.Mailbox62.value: 462,
    AELocation.Mailbox63.value: 463,

    # Bosses
    AELocation.Boss73.value: 500,
    AELocation.Boss83.value: 501,
    AELocation.W9L1Professor.value: 502,
    AELocation.W9L1Jake.value: 503
}

#Where RAM.levels[address] : Total monkeys count
hundoMonkeysCount = {
    0x01: 4, # Fossil
    0x02: 6, # Primordial
    0x03: 7, # Molten
    0x04: 14, # Thick
    0x05: 13, # Dark
    0x06: 8, # Cryptic
    0x07: 0, # Stadium
    0x08: 8, # Crabby
    0x09: 8, # Coral
    0x0A: 11, # Dexter
    0x0B: 6, # Snowy
    0x0C: 9, # Frosty
    0x0D: 9, # Hot
    0x0E: 0, # Gladiator
    0x0F: 12, # Sushi
    0x10: 10, # Wabi
    0x11: 20, # Crumbling
    0x14: 13, # City
    0x15: 10, # Factory
    0x16: 12, # TV
    0x18: 24 # Specter
}

# These values are the room ID of the room, and the door ID the room is entered through. To get these, stand near the transition that leads to that entrance. As an example, {45, 5} will spawn Spike at the top of the Bell Tower, as though he entered from outside. 
# Array order : {TargetRoom,TargetDoor,Transition ID}
# -- TargetRoom     : (Exit) If you want to warp to this Room, set the Entering door's TargetRoomAddress value to this
# -- TargetDoor     : (Exit) If you want to warp to this Room, set the Entering door's TargetDoorAddress value to this
# -- Transition ID  : (Enter) Transition ID to use with RAM.transitionAddresses.You should modify the addresses referred by this ID to what you want the target room to be
# Transition ID should be 0 if this is a transition that has no door related to it (Like a level spawn or inaccessible transition)
doorTransitions = {
    AEDoor.FF_ENTRY.value: {1, 0, 0},
    AEDoor.PO_ENTRY.value: {2, 0, 0},
    AEDoor.ML_ENTRY.value: {3, 0, 0},
    AEDoor.ML_ENTRY_VOLCANO.value: {3, 2, 1},
    AEDoor.ML_ENTRY_TRICERATOPS.value: {3, 3,2},
    AEDoor.ML_VOLCANO_ENTRY.value: {4, 0, 1},
    AEDoor.ML_TRICERATOPS_ENTRY.value: {5, 0, 1},
    AEDoor.TJ_ENTRY.value: {6, 0, 0},
    AEDoor.TJ_ENTRY_MUSHROOM.value: {6, 2, 1},
    AEDoor.TJ_ENTRY_FISH.value: {6, 3, 2},
    AEDoor.TJ_ENTRY_BOULDER.value: {6, 4, 3},
    AEDoor.TJ_MUSHROOM_ENTRY.value: {7, 0, 1},
    AEDoor.TJ_FISH_ENTRY.value: {8, 0, 1},
    AEDoor.TJ_FISH_TENT.value: {8, 2, 2},
    AEDoor.TJ_TENT_FISH.value: {9, 0, 1},
    AEDoor.TJ_TENT_BOULDER.value: {9, 2, 2},
    AEDoor.TJ_BOULDER_ENTRY.value: {10, 2, 2},
    AEDoor.TJ_BOULDER_TENT.value: {10, 0, 1},
    AEDoor.DR_ENTRY.value: {11, 0, 0},
    AEDoor.DR_OUTSIDE_FENCE.value: {11, 2, 1},
    AEDoor.DR_OUTSIDE_HOLE.value: {11, 3, 2},
    AEDoor.DR_OUTSIDE_OBELISK_BOTTOM.value: {11, 4, 3},
    AEDoor.DR_OUTSIDE_OBELISK_TOP.value: {11, 5, 4},
    AEDoor.DR_OUTSIDE_WATER_BUTTON.value: {11, 6, 5},
    AEDoor.DR_OUTSIDE_WATER_LEDGE.value: {11, 7, 6},
    AEDoor.DR_FAN_OUTSIDE_FENCE.value: {12, 2, 2},
    AEDoor.DR_FAN_OUTSIDE_HOLE.value: {12, 0, 1},
    AEDoor.DR_OBELISK_BOTTOM.value: {13, 0, 1},
    AEDoor.DR_OBELISK_TOP.value: {13, 2, 2},
    AEDoor.DR_WATER_SIDE.value: {14, 0, 1},
    AEDoor.DR_WATER_LEDGE.value: {14, 2, 2},
    AEDoor.CR_ENTRY.value: {15, 0, 0},
    AEDoor.CR_ENTRY_SIDE_ROOM.value: {15, 2, 1},
    AEDoor.CR_ENTRY_MAIN_RUINS.value: {15, 3, 2},
    AEDoor.CR_SIDE_ROOM_ENTRY.value: {16, 0, 1},
    AEDoor.CR_MAIN_RUINS_ENTRY.value: {17, 0, 1},
    AEDoor.CR_MAIN_RUINS_PILLAR_ROOM.value: {17, 2, 2},
    AEDoor.CR_PILLAR_ROOM_MAIN_RUINS.value: {18, 0, 1},
    AEDoor.SA_ENTRY.value: {19, 0, 0},
    AEDoor.CB_ENTRY.value: {20, 0, 0},
    AEDoor.CB_ENTRY_SECOND_ROOM.value: {20, 2, 1},
    AEDoor.CB_SECOND_ROOM_ENTRY.value: {21, 0, 1},
    AEDoor.CCAVE_ENTRY.value: {22, 0, 0},
    AEDoor.CCAVE_ENTRY_SECOND_ROOM.value: {22, 2, 1},
    AEDoor.CCAVE_SECOND_ROOM_ENTRY.value: {23, 0, 1},
    AEDoor.DI_ENTRY.value: {24, 0, 0},
    AEDoor.DI_ENTRY_STOMACH.value: {24, 2, 1},
    AEDoor.DI_STOMACH_ENTRY.value: {25, 0, 1},
    AEDoor.DI_STOMACH_SLIDE_ROOM.value: {25, 2, 2},
    AEDoor.DI_GALLERY_SLIDE_ELEVATOR.value: {26, 0, 1},
    AEDoor.DI_GALLERY_TENTACLE.value: {26, 2, 2},
    AEDoor.DI_GALLERY_SLIDE_ROOM_TOP.value: {26, 3, 3},
    AEDoor.DI_TENTACLE.value: {27, 0, 1},
    AEDoor.DI_SLIDE_ROOM_STOMACH.value: {28, 0, 1},
    AEDoor.DI_SLIDE_ROOM_GALLERY.value: {28, 2, 2},
    AEDoor.DI_SLIDE_ROOM_GALLERY_WATER.value: {28, 3, 3},
    AEDoor.SM_ENTRY.value: {29, 0, 0},
    AEDoor.FR_ENTRY.value: {30, 0, 0},
    AEDoor.FR_ENTRY_CAVERNS.value: {30, 2, 1},
    AEDoor.FR_WATER_CAVERNS.value: {31, 0, 1},
    AEDoor.FR_CAVERNS_ENTRY.value: {32, 0, 1},
    AEDoor.FR_CAVERNS_WATER.value: {32, 2, 2},
    AEDoor.HS_ENTRY.value: {33, 0, 0},
    AEDoor.HS_ENTRY_HOT_SPRING.value: {33, 2, 1},
    AEDoor.HS_ENTRY_POLAR_BEAR_CAVE.value: {33, 3, 2},
    AEDoor.HS_HOT_SPRING.value: {34, 0, 1},
    AEDoor.HS_POLAR_BEAR_CAVE.value: {35, 0, 1},
    AEDoor.GA_ENTRY.value: {36, 0, 0},
    AEDoor.ST_ENTRY.value: {37, 0, 0},
    AEDoor.ST_ENTRY_TEMPLE.value: {37, 2, 1},
    AEDoor.ST_ENTRY_WELL.value: {37, 3, 2},
    AEDoor.ST_TEMPLE.value: {38, 0, 1},
    AEDoor.ST_WELL.value: {39, 0, 1},
    AEDoor.WSW_ENTRY.value: {40, 0, 0},
    AEDoor.WSW_ENTRY_GONG.value: {40, 2, 1},
    AEDoor.WSW_GONG_ENTRY.value: {41, 0, 1},
    AEDoor.WSW_GONG_MIDDLE.value: {41, 2, 2},
    AEDoor.WSW_MIDDLE_GONG.value: {42, 0, 2},
    AEDoor.WSW_MIDDLE_OBSTACLE.value: {42, 2, 1},
    AEDoor.WSW_OBSTACLE_MIDDLE.value: {43, 0, 2},
    AEDoor.WSW_OBSTACLE_BARREL.value: {43, 2, 1},
    AEDoor.WSW_BARREL_OBSTACLE.value: {44, 0, 1},
    AEDoor.CC_ENTRY.value: {45, 0, 0},
    AEDoor.CC_ENTRY_BASEMENT.value: {45, 4, 1},
    AEDoor.CC_ENTRY_CASTLE.value: {45, 2, 2},
    AEDoor.CC_ENTRY_BELL.value: {45, 5, 3},
    AEDoor.CC_ENTRY_BOSS.value: {45, 6, 4},
    AEDoor.CC_CASTLEMAIN_ENTRY.value: {46, 0, 1},
    AEDoor.CC_CASTLEMAIN_BELL.value: {46, 2, 2},
    AEDoor.CC_CASTLEMAIN_ELEVATOR.value: {46, 3, 3},
    AEDoor.CC_BASEMENT_ENTRY.value: {47, 0, 1},
    AEDoor.CC_BASEMENT_BUTTON_DOWN.value: {47, 2, 4},
    AEDoor.CC_BASEMENT_BUTTON_UP.value: {47, 3, 2},
    AEDoor.CC_BASEMENT_ELEVATOR.value: {47, 4, 3},
    AEDoor.CC_BOSS_ROOM.value: {48, 0, 1},
    AEDoor.CC_BUTTON_BASEMENT_WATER.value: {49, 0, 1},
    AEDoor.CC_BUTTON_BASEMENT_LEDGE.value: {49, 2, 2},
    AEDoor.CC_ELEVATOR_CASTLEMAIN.value: {50, 0, 1},
    AEDoor.CC_ELEVATOR_BASEMENT.value: {50, 2, 2},
    AEDoor.CC_BELL_CASTLE.value: {51, 0, 1},
    AEDoor.CC_BELL_ENTRY.value: {51, 2, 2},
    AEDoor.CP_ENTRY.value: {53, 0, 0},
    AEDoor.CP_OUTSIDE_SEWERS_FRONT.value: {53, 2, 1},
    AEDoor.CP_OUTSIDE_BARREL.value: {53, 3, 2},
    AEDoor.CP_SEWERSFRONT_OUTSIDE.value: {54, 0, 1},
    AEDoor.CP_SEWERSFRONT_BARREL.value: {54, 2, 2},
    AEDoor.CP_BARREL_SEWERS_FRONT.value: {55, 0, 1},
    AEDoor.CP_BARREL_OUTSIDE.value: {55, 2, 2},
    AEDoor.SF_ENTRY.value: {56, 0, 0},
    AEDoor.SF_OUTSIDE_FACTORY.value: {56, 2, 1},
    AEDoor.SF_FACTORY_RC_CAR.value: {57, 2 , 1},
    AEDoor.SF_FACTORY_WHEEL_BOTTOM.value: {57, 3, 2},
    AEDoor.SF_FACTORY_WHEEL_TOP.value: {57, 4, 3},
    AEDoor.SF_FACTORY_MECH.value: {57, 5, 4},
    AEDoor.SF_FACTORY_OUTSIDE.value: {57, 0, 5},
    AEDoor.SF_RC_CAR_FACTORY.value: {58, 0, 1},
    AEDoor.SF_LAVA_MECH.value: {59, 0, 1},
    AEDoor.SF_LAVA_CONVEYOR.value: {59, 2, 2},
    AEDoor.SF_WHEEL_FACTORY_BOTTOM.value: {60, 0, 1},
    AEDoor.SF_WHEEL_FACTORY_TOP.value: {60, 2, 2},
    AEDoor.SF_CONVEYOR_LAVA.value: {61, 0, 1},
    AEDoor.SF_CONVEYOR1_ENTRY.value: {61, 7, 8},
    AEDoor.SF_CONVEYOR2_ENTRY.value: {61, 7, 7},
    AEDoor.SF_CONVEYOR3_ENTRY.value: {61, 6, 6},
    AEDoor.SF_CONVEYOR4_ENTRY.value: {61, 5, 5},
    AEDoor.SF_CONVEYOR5_ENTRY.value: {61, 4, 4},
    AEDoor.SF_CONVEYOR6_ENTRY.value: {61, 3, 3},
    AEDoor.SF_CONVEYOR7_ENTRY.value: {61, 2, 2},
    AEDoor.SF_MECH_FACTORY.value: {62, 0, 1},
    AEDoor.SF_MECH_LAVA.value: {62, 2, 2},
    AEDoor.TVT_ENTRY.value: {63, 0, 0},
    AEDoor.TVT_OUTSIDE_LOBBY.value: {63, 2, 1},
    AEDoor.TVT_WATER_LOBBY.value: {64, 0, 1},
    AEDoor.TVT_LOBBY_OUTSIDE.value: {65, 0, 1},
    AEDoor.TVT_LOBBY_WATER.value: {65, 2, 2},
    AEDoor.TVT_LOBBY_TANK.value: {65, 3, 3},
    AEDoor.TVT_TANK_LOBBY.value: {66, 0, 1},
    AEDoor.TVT_TANK_BOSS.value: {66, 2, 2},
    AEDoor.TVT_TANK_FAN.value: {66, 3, 3},
    AEDoor.TVT_FAN_TANK.value: {67, 0, 1},
    AEDoor.TVT_BOSS_TANK.value: {68, 0, 1},
    AEDoor.MM_SL_HUB.value: {69, 0, 0},
    AEDoor.MM_SL_HUB_COASTER.value: {69, 2, 1},
    AEDoor.MM_SL_HUB_CIRCUS.value: {69, 3, 2},
    AEDoor.MM_SL_HUB_WESTERN.value: {69, 4, 3},
    AEDoor.MM_SL_HUB_GO_KARZ.value: {69, 5, 4},
    AEDoor.MM_SL_HUB_CRATER.value: {69, 6, 5},
    AEDoor.MM_GO_KARZ_SL_HUB.value: {70, 0, 1},
    AEDoor.MM_CIRCUS_SL_HUB.value: {71, 0, 1},
    AEDoor.MM_COASTER_ENTRY_SL_HUB.value: {72, 0, 1},
    AEDoor.MM_COASTER_ENTRY_COASTER1.value: {72, 2, 2}, # IHNN note - Entrance only door, normally inaccessible. Equivalent to 72, 3.
    AEDoor.MM_COASTER_ENTRY_DISEMBARK.value: {72, 3, 0},
    AEDoor.MM_COASTER1_ENTRY.value: {73, 0, 0},
    AEDoor.MM_COASTER1_COASTER2.value: {73, 2, 1}, # IHNN note - Entrance only door, normally inaccessible. Equivalent to 73, 0.
    AEDoor.MM_COASTER2_ENTRY.value: {74, 0, 0},
    AEDoor.MM_COASTER2_HAUNTED_HOUSE.value: {74, 2, 1}, # IHNN note - Entrance only door, normally inaccessible. Equivalent to 74, 0.
    AEDoor.MM_HAUNTED_HOUSE_DISEMBARK.value: {75, 0, 0},
    AEDoor.MM_HAUNTED_HOUSE_COFFIN.value: {75, 3, 1},
    AEDoor.MM_COFFIN_HAUNTED_HOUSE.value: {76, 0, 1},
    AEDoor.MM_COFFIN_COASTER_ENTRY.value: {76, 2, 2}, # IHNN note - Entrance only door, normally inaccessible. Spawns Spike in the center of the coffins.
    AEDoor.MM_WESTERN_SL_HUB.value: {77, 0, 1},
    AEDoor.MM_CRATER_SL_HUB.value: {78, 0, 1},
    AEDoor.MM_CRATER_OUTSIDE_CASTLE.value: {78, 2, 2},
    AEDoor.MM_OUTSIDE_CASTLE_CASTLE_MAIN.value: {79, 2, 1},
    AEDoor.MM_OUTSIDE_CASTLE_SIDE_ENTRY.value: {79, 3, 2},
    AEDoor.MM_OUTSIDE_CASTLE_CRATER.value: {79, 0, 3},
    AEDoor.MM_CASTLE_MAIN_OUTSIDE_CASTLE.value: {80, 0, 1},
    AEDoor.MM_CASTLE_MAIN_MONKEY_HEAD.value: {80, 2, 2},
    AEDoor.MM_CASTLE_MAIN_INSIDE_CLIMB.value: {80, 3, 3},
    AEDoor.MM_CASTLE_MAIN_FROM_OUTSIDE.value: {80, 4, 0},
    AEDoor.MM_CASTLE_MAIN_SPECTER1.value: {80, 5, 4}, # IHNN note - Invalid connection.
    # Thedragon005 note - The connection exists, but it is oneway only (Correspond to entering the transition to specter)
    # The invalid connection here would be AEDoor.MM_SPECTER1_ROOM_CASTLE_MAIN since you cannot exit the Specter fight once in the room
    AEDoor.MM_INSIDE_CLIMB_OUTSIDE_CLIMB.value: {81, 2, 1},
    AEDoor.MM_INSIDE_CLIMB_CASTLE_MAIN.value: {81, 0, 2},
    AEDoor.MM_OUTSIDE_CLIMB_INSIDE_CLIMB.value: {82, 0, 1},
    AEDoor.MM_OUTSIDE_CLIMB_CASTLE_MAIN.value: {82, 2, 2}, # IHNN note - Entrance only door, normally inaccessible. Spawns Spike at the top, by the mech.
    AEDoor.MM_SPECTER1_ROOM.value: {83, 0, 0},
    AEDoor.MM_MONKEY_HEAD_CASTLE_MAIN.value: {84, 0, 1},
    AEDoor.MM_SIDE_ENTRY_OUTSIDE_CASTLE.value: {85, 0, 1},
    # AEDoor.PPM_ENTRY.value: {87, 0, 0}, # IHNN note - noticed this was missing, have not validated the room.
    AEDoor.TIME_ENTRY.value: {88, 0, 0},
    AEDoor.TIME_MAIN_TRAINING.value: {88, 3, 1},
    AEDoor.TIME_MAIN_MINIGAME.value: {88, 2, 2},
    AEDoor.TIME_MINIGAME_MAIN.value: {91, 1, 1},
    AEDoor.TIME_TRAINING_MAIN.value: {90, 0, 1},
    AEDoor.TIME_TRAINING_WATERNET.value: {90, 1, 2},
    AEDoor.TIME_TRAINING_RADAR.value: {90, 2, 3},
    AEDoor.TIME_TRAINING_SLING.value: {90, 3, 4},
    AEDoor.TIME_TRAINING_HOOP.value: {90, 4, 5},
    AEDoor.TIME_TRAINING_FLYER.value: {90, 5, 6},
    AEDoor.TIME_TRAINING_CAR.value: {90, 6, 7},
    AEDoor.TIME_TRAINING_PUNCH.value: {90, 7, 8},
}

def createLocationGroups():
    # Iterate through all locations
    for x in range (0, len(location_table)):
        locname = list(location_table.keys())[x]
        # Add to location group for each level
        if "1-1" in locname:
            GROUPED_LOCATIONS.setdefault("Fossil Field", []).append(locname)
        elif "1-2" in locname:
            GROUPED_LOCATIONS.setdefault("Primordial Ooze", []).append(locname)
        elif "1-3" in locname:
            GROUPED_LOCATIONS.setdefault("Molten Lava", []).append(locname)
        elif "2-1" in locname:
            GROUPED_LOCATIONS.setdefault("Thick Jungle", []).append(locname)
        elif "2-2" in locname:
            GROUPED_LOCATIONS.setdefault("Dark Ruins", []).append(locname)
        elif "2-3" in locname:
            GROUPED_LOCATIONS.setdefault("Cryptic Relics", []).append(locname)
        elif "3-1" in locname:
            GROUPED_LOCATIONS.setdefault("Stadium Attack", []).append(locname)
            GROUPED_LOCATIONS.setdefault("Races", []).append(locname)
        elif "4-1" in locname:
            GROUPED_LOCATIONS.setdefault("Crabby Beach", []).append(locname)
        elif "4-2" in locname:
            GROUPED_LOCATIONS.setdefault("Coral Cave", []).append(locname)
        elif "4-3" in locname:
            GROUPED_LOCATIONS.setdefault("Dexters Island", []).append(locname)
        elif "5-1" in locname:
            GROUPED_LOCATIONS.setdefault("Snowy Mammoth", []).append(locname)
        elif "5-2" in locname:
            GROUPED_LOCATIONS.setdefault("Frosty Retreat", []).append(locname)
        elif "5-3" in locname:
            GROUPED_LOCATIONS.setdefault("Hot Springs", []).append(locname)
        elif "6-1" in locname:
            GROUPED_LOCATIONS.setdefault("Gladiator Attack", []).append(locname)
            GROUPED_LOCATIONS.setdefault("Races", []).append(locname)
        elif "7-1" in locname:
            GROUPED_LOCATIONS.setdefault("Sushi Temple", []).append(locname)
        elif "7-2" in locname:
            GROUPED_LOCATIONS.setdefault("Wabi Sabi Wall", []).append(locname)
        elif "7-3" in locname:
            GROUPED_LOCATIONS.setdefault("Crumbling Castle", []).append(locname)
        elif "8-1" in locname:
            GROUPED_LOCATIONS.setdefault("City Park", []).append(locname)
        elif "8-2" in locname:
            GROUPED_LOCATIONS.setdefault("Specters Factory", []).append(locname)
        elif "8-3" in locname:
            GROUPED_LOCATIONS.setdefault("TV Tower", []).append(locname)
        elif "9-1" in locname:
            GROUPED_LOCATIONS.setdefault("Monkey Madness", []).append(locname)
        elif "Time Station" in locname:
            GROUPED_LOCATIONS.setdefault("Time Station", []).append(locname)

        if "Mailbox" in locname:
            GROUPED_LOCATIONS.setdefault("Mailboxes", []).append(locname)
        elif "Coin" in locname:
            GROUPED_LOCATIONS.setdefault("Specter Coins", []).append(locname)
        elif ("Specter" in locname and "Factory" not in locname) or "Boss" in locname or "Jake" in locname or "Professor" in locname:
            GROUPED_LOCATIONS.setdefault("Bosses", []).append(locname)
        elif "Monkey" in locname and "Madness" not in locname:
            GROUPED_LOCATIONS.setdefault("Monkeys", []).append(locname)

createLocationGroups()
