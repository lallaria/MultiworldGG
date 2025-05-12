class RAM:
    monkeyListGlobal = {
        1: 0x0DF828,
        2: 0x0DF829,
        3: 0x0DF82A,
        4: 0x0DF82B,
        5: 0x0DF830,
        6: 0x0DF831,
        8: 0x0DF832,
        7: 0x0DF833,
        10: 0x0DF834,
        9: 0x0DF835,
        11: 0x0DF838,
        12: 0x0DF839,
        13: 0x0DF83A,
        17: 0x0DF83B,
        15: 0x0DF840,
        14: 0x0DF841,
        16: 0x0DF848,
        18: 0x0DF850,
        19: 0x0DF851,
        20: 0x0DF852,
        29: 0x0DF858,
        31: 0x0DF859,
        30: 0x0DF85A,
        21: 0x0DF860,
        22: 0x0DF861,
        23: 0x0DF862,
        25: 0x0DF868,
        24: 0x0DF869,
        26: 0x0DF86A,
        28: 0x0DF870,
        27: 0x0DF871,
        33: 0x0DF878,
        37: 0x0DF879,
        42: 0x0DF87A,
        34: 0x0DF87B,
        32: 0x0DF87C,
        35: 0x0DF880,
        36: 0x0DF881,
        41: 0x0DF888,
        43: 0x0DF889,
        38: 0x0DF88A,
        39: 0x0DF890,
        40: 0x0DF891,
        44: 0x0DF892,
        51: 0x0DF898,
        49: 0x0DF899,
        45: 0x0DF8A0,
        47: 0x0DF8A8,
        46: 0x0DF8A9,
        50: 0x0DF8AA,
        48: 0x0DF8B0,
        52: 0x0DF8B1,
        53: 0x0DF8C0,
        54: 0x0DF8C1,
        55: 0x0DF8C2,
        56: 0x0DF8C3,
        57: 0x0DF8C8,
        60: 0x0DF8C9,
        58: 0x0DF8CA,
        59: 0x0DF8CB,
        61: 0x0DF8D0,
        62: 0x0DF8D1,
        63: 0x0DF8D2,
        64: 0x0DF8D3,
        65: 0x0DF8D8,
        67: 0x0DF8D9,
        66: 0x0DF8DA,
        68: 0x0DF8DB,
        70: 0x0DF8E0,
        69: 0x0DF8E1,
        77: 0x0DF8E8,
        71: 0x0DF8E9,
        78: 0x0DF8EA,
        72: 0x0DF8F0,
        73: 0x0DF8F1,
        74: 0x0DF8F2,
        75: 0x0DF8F3,
        76: 0x0DF8F4,
        79: 0x0DF8F8,
        80: 0x0DF908,
        81: 0x0DF909,
        84: 0x0DF90A,
        82: 0x0DF90B,
        83: 0x0DF90C,
        85: 0x0DF90D,
        86: 0x0DF910,
        87: 0x0DF911,
        91: 0x0DF918,
        93: 0x0DF919,
        92: 0x0DF91A,
        94: 0x0DF91B,
        88: 0x0DF920,
        89: 0x0DF921,
        90: 0x0DF922,
        95: 0x0DF928,
        96: 0x0DF929,
        99: 0x0DF92A,
        100: 0x0DF92B,
        101: 0x0DF930,
        102: 0x0DF931,
        103: 0x0DF932,
        97: 0x0DF938,
        98: 0x0DF939,
        104: 0x0DF948,
        105: 0x0DF949,
        106: 0x0DF94A,
        107: 0x0DF94B,
        109: 0x0DF950,
        110: 0x0DF951,
        108: 0x0DF952,
        114: 0x0DF953,
        115: 0x0DF954,
        113: 0x0DF958,
        111: 0x0DF959,
        112: 0x0DF95A,
        116: 0x0DF960,
        117: 0x0DF961,
        118: 0x0DF968,
        119: 0x0DF969,
        120: 0x0DF96A,
        123: 0x0DF970,
        121: 0x0DF978,
        122: 0x0DF979,
        124: 0x0DF980,
        125: 0x0DF981,
        127: 0x0DF988,
        136: 0x0DF989,
        126: 0x0DF98A,
        128: 0x0DF98B,
        137: 0x0DF98C,
        129: 0x0DF990,
        132: 0x0DF993,
        130: 0x0DF991,
        131: 0x0DF992,
        133: 0x0DF998,
        134: 0x0DF999,
        135: 0x0DF99A,
        138: 0x0DF9A8,
        139: 0x0DF9A9,
        140: 0x0DF9B0,
        141: 0x0DF9B1,
        142: 0x0DF9B2,
        143: 0x0DF9B8,
        144: 0x0DF9B9,
        145: 0x0DF9BA,
        146: 0x0DF9C8,
        147: 0x0DF9C9,
        148: 0x0DF9CA,
        149: 0x0DF9CB,
        152: 0x0DF9D2,
        151: 0x0DF9D1,
        150: 0x0DF9D0,
        153: 0x0DF9D8,
        154: 0x0DF9D9,
        155: 0x0DF9DA,
        156: 0x0DF9DB,
        157: 0x0DF9DC,
        158: 0x0DF9DD,
        159: 0x0DF9E0,
        160: 0x0DF9E1,
        161: 0x0DF9E8,
        162: 0x0DF9F0,
        168: 0x0DFA10,
        164: 0x0DF9F9,
        167: 0x0DFA09,
        166: 0x0DFA08,
        165: 0x0DF9FA,
        163: 0x0DF9F8,
        169: 0x0DFA18,
        170: 0x0DFA20,
        171: 0x0DFA21,
        172: 0x0DFA28,
        173: 0x0DFA29,
        174: 0x0DFA30,
        175: 0x0DFA31,
        176: 0x0DFA32,
        177: 0x0DFA38,
        178: 0x0DFA39,
        179: 0x0DFA3A,
        180: 0x0DFA3B,
        181: 0x0DFA60,
        182: 0x0DFA78,
        183: 0x0DFA80,
        184: 0x0DFA81,
        185: 0x0DFA82,
        186: 0x0DFA88,
        187: 0x0DFA89,
        188: 0x0DFA8A,
        189: 0x0DFA8B,
        190: 0x0DFA90,
        192: 0x0DFA99,
        193: 0x0DFAA0,
        194: 0x0DFAA1,
        196: 0x0DFAA3,
        195: 0x0DFAA2,
        197: 0x0DFAA8,
        201: 0x0DFAC0,
        202: 0x0DFAC1,
        203: 0x0DFAC2,
        204: 0x0DFAC8,
        198: 0x0DFAA9,
        199: 0x0DFAB0,
        200: 0x0DFAB1,
        191: 0x0DFA98
    }

    monkeyListLocal = {
        1: {  # 1-1
            1: 0x0E557A,
            3: 0x0E5A1A,
            2: 0x0E57CA,
            4: 0x0E5C6A
        },
        2: {  # 1-2
            5: 0x0E557A,
            6: 0x0E57CA,
            7: 0x0E5C6A,
            10: 0x0E5EBA,
            9: 0x0E610A,
            8: 0x0E5A1A
        },
        3: {  # 1-3
            11: 0x0E557A,
            12: 0x0E57CA,
            17: 0x0E5C6A,
            13: 0x0E5A1A
        },
        4: {  # volcano
            14: 0x0E57CA,
            15: 0x0E557A
        },
        5: {  # triceratops
            16: 0x0E557A
        },
        6: {  # 2-1
            18: 0x0E557A,
            19: 0x0E57CA,
            20: 0x0E5A1A
        },
        7: {  # mushroom area
            29: 0x0E557A,
            30: 0x0E5A1A,
            31: 0x0E57CA
        },
        8: {  # fish room
            23: 0x0E5A1A,
            21: 0x0E557A,
            22: 0x0E57CA
        },
        9: {  # tent/vine room
            24: 0x0E57CA,
            25: 0x0E557A,
            26: 0x0E5A1A
        },
        10: {  # boulder room
            27: 0x0E57CA,
            28: 0x0E557A
        },
        11: {  # 2-2
            32: 0x0E5EBA,
            33: 0x0E557A,
            34: 0x0E5C6A,
            37: 0x0E57CA,
            42: 0x0E5A1A
        },
        12: {  # fan basement
            35: 0x0E557A,
            36: 0x0E57CA
        },
        13: {  # obelisk inside
            38: 0x0E5A1A,
            41: 0x0E557A,
            43: 0x0E57CA
        },
        14: {  # water basement
            39: 0x0E557A,
            40: 0x0E57CA,
            44: 0x0E5A1A
        },
        15: {  # 2-3
            49: 0x0E57CA,
            51: 0x0E557A
        },
        16: {  # side room
            45: 0x0E557A
        },
        17: {  # main ruins
            47: 0x0E557A,
            50: 0x0E5A1A,
            46: 0x0E57CA
        },
        18: {  # pillar room
            48: 0x0E557A,
            52: 0x0E57CA
        },
        19: {  # 3-1

        },
        20: {  # 4-1
            53: 0x0E557A,
            54: 0x0E57CA,
            55: 0x0E5A1A,
            56: 0x0E5C6A
        },
        21: {  # second room
            57: 0x0E557A,
            58: 0x0E5A1A,
            59: 0x0E5C6A,
            60: 0x0E57CA
        },
        22: {  # 4-2
            61: 0x0E557A,
            62: 0x0E57CA,
            63: 0x0E5A1A,
            64: 0x0E5C6A
        },
        23: {  # second room
            65: 0x0E5A1A,
            67: 0x0E57CA,
            68: 0x0E5C6A,
            66: 0x0E557A
        },
        24: {  # 4-3
            69: 0x0E57CA,
            70: 0x0E557A
        },
        25: {  # stomach
            71: 0x0E57CA,
            77: 0x0E557A,
            78: 0x0E5A1A
        },
        26: {  # gallery/boulder
            72: 0x0E557A,
            73: 0x0E57CA,
            74: 0x0E5A1A,
            75: 0x0E5C6A,
            76: 0x0E5EBA
        },
        27: {  # tentacle room
            79: 0x0E557A
        },
        28: {  # slide room

        },
        29: {  # 5-1
            80: 0x0E557A,
            81: 0x0E57CA,
            84: 0x0E5A1A,
            83: 0x0E5C6A,
            85: 0x0E610A,
            82: 0x0E5EBA
        },
        30: {  # 5-2
            86: 0x0E557A,
            87: 0x0E57CA
        },
        31: {  # water room
            91: 0x0E557A,
            92: 0x0E5A1A,
            93: 0x0E57CA,
            94: 0x0E5C6A
        },
        32: {  # caverns
            88: 0x0E557A,
            90: 0x0E5A1A,
            89: 0x0E57CA
        },
        33: {  # 5-3
            95: 0x0E557A,
            96: 0x0E57CA,
            99: 0x0E5A1A,
            100: 0x0E5C6A
        },
        34: {  # hot spring
            101: 0x0E557A,
            102: 0x0E57CA,
            103: 0x0E5A1A
        },
        35: {  # polar bear cave
            98: 0x0E57CA,
            97: 0x0E557A
        },
        36: {  # 6-1

        },
        37: {  # 7-1
            104: 0x0E557A,
            105: 0x0E57CA,
            106: 0x0E5A1A,
            107: 0x0E5C6A
        },
        38: {  # temple
            108: 0x0E5A1A,
            110: 0x0E57CA,
            109: 0x0E557A,
            114: 0x0E5C6A,
            115: 0x0E5EBA
        },
        39: {  # well
            111: 0x0E57CA,
            112: 0x0E5A1A,
            113: 0x0E557A
        },
        40: {  # 7-2
            116: 0x0E557A,
            117: 0x0E57CA
        },
        41: {  # gong room
            118: 0x0E557A,
            119: 0x0E57CA,
            120: 0x0E5A1A
        },
        42: {  # middle room
            123: 0x0E557A
        },
        43: {  # obstacle course
            122: 0x0E57CA,
            121: 0x0E557A,
        },
        44: {  # barrel room
            124: 0x0E557A,
            125: 0x0E57CA
        },
        45: {  # 7-3
            126: 0x0E5A1A,
            127: 0x0E557A,
            128: 0x0E5C6A,
            137: 0x0E5EBA,
            136: 0x0E57CA
        },
        46: {  # castle main
            129: 0x0E557A,
            131: 0x0E5A1A,
            130: 0x0E57CA,
            132: 0x0E5C6A
        },
        47: {  # flooded basement
            133: 0x0E557A,
            134: 0x0E57CA,
            135: 0x0E5A1A
        },
        49: {  # button room
            139: 0x0E57CA,
            138: 0x0E557A
        },
        50: {  # elevator room
            140: 0x0E557A,
            141: 0x0E57CA,
            142: 0x0E5A1A
        },
        51: {  # bell tower
            145: 0x0E5A1A,
            144: 0x0E57CA,
            143: 0x0E557A
        },
        52: {

        },
        53: {  # 8-1
            146: 0x0E557A,
            149: 0x0E5C6A,
            147: 0x0E57CA,
            148: 0x0E5A1A
        },
        54: {  # sewers front
            151: 0x0E57CA,
            152: 0x0E5A1A,
            150: 0x0E557A
        },
        55: {  # barrel room
            155: 0x0E5A1A,
            153: 0x0E557A,
            156: 0x0E5C6A,
            157: 0x0E5EBA,
            154: 0x0E57CA,
            158: 0x0E610A
        },
        56: {  # 8-2
            159: 0x0E557A,
            160: 0x0E57CA
        },
        57: {  # main factory
            161: 0x0E557A
        },
        58: {  # rc car room
            162: 0x0E557A
        },
        59: {  # lava room
            163: 0x0E557A,
            164: 0x0E57CA,
            165: 0x0E5A1A
        },
        60: {

        },
        61: {  # conveyor room
            166: 0x0E557A,
            167: 0x0E57CA
        },
        62: {  # mech room
            168: 0x0E557A
        },
        63: {  # 8-3
            169: 0x0E557A
        },
        64: {  # water basement
            171: 0x0E57CA,
            170: 0x0E557A
        },
        65: {  # lobby
            172: 0x0E557A,
            173: 0x0E57CA
        },
        66: {  # tank room
            174: 0x0E557A,
            175: 0x0E57CA,
            176: 0x0E5A1A
        },
        67: {  # fan room
            177: 0x0E557A,
            179: 0x0E5A1A,
            180: 0x0E5C6A,
            178: 0x0E57CA
        },
        68: {

        },
        69: {  # MM Lobby

        },
        71: {

        },
        72: {  # coaster entry
            181: 0x0E557A
        },
        73: {  # coaster 1

        },
        74: {  # coaster 2

        },
        75: {  # haunted house
            182: 0x0E557A
        },
        76: {  # coffin room
            183: 0x0E557A,
            184: 0x0E57CA,
            185: 0x0E5A1A
        },
        77: {  # western land
            187: 0x0E57CA,
            186: 0x0E557A,
            188: 0x0E5A1A,
            189: 0x0E5C6A
        },
        78: {  # crater
            190: 0x0E557A
        },
        79: {  # outside castle
            192: 0x0E557A,
            191: 0X0E57CA
        },
        80: {  # castle main
            194: 0x0E57CA,
            195: 0x0E5A1A,
            196: 0x0E5C6A,
            193: 0x0E557A
        },
        81: {  # inside climb
            197: 0x0E557A,
            198: 0x0E57CA
        },
        82: {  # outside climb
            199: 0x0E557A,
            200: 0x0E57CA
        },
        84: {  # Monkey head
            201: 0x0E557A,
            202: 0x0E57CA,
            203: 0x0E5A1A
        },
        85: {  # side entry
            204: 0x0E557A
        }

    }
    mailboxListLocal = {
        1: {  # 1-1
            401 : 65,
            402 : 66,
            403 : 19
        },
        2: {  # 1-2
            404 : 68,
            405 : 69,
            406 : 70,
            407 : 67
        },
        3: {  # 1-3
            408 : 103,
            409 : 21
        },
        4: {  # volcano
            410 : 100
        },
        5: {  # triceratops
            411: {101, 116},
            412 : 41
        },
        6: {  # 2-1
            413 : 72,
            414 : 71
        },
        7: {  # mushroom area
            415 : {38,99},
            416 : 24
        },
        8: {  # fish room
            417 : 73,
            418 : 71,
            419 : 104
        },
        9: {  # tent/vine room
            420 : 48
        },
        10: {  # boulder room
            421 : 23
        },
        11: {  # 2-2
            422 : 105,
            423 : {49,103},
            424 : 22,
            425 : 81,
        },
        12: {  # fan basement
            426 : 80,
            427 : {70,97}
        },
        13: {  # obelisk inside
            428 : {52,97}
        },
        #14: {  # water basement

        #},
        15: {  # 2-3
            429 : 50,
            430 : 112
        },
        #16: {  # side room

        #},
        17: {  # main ruins
            431 : 33,
            432 : 37
        },
        18: {  # pillar room
            433 : 67
        },
        #19: {  # 3-1

        #},
        20: {  # 4-1
            434 : 25,
            435 : {22,82}
        },
        21: {  # second room
            436 : 72
        },
        #22: {  # 4-2

        #},
        23: {  # second room
            437 : 53,
            438 : 54
        },
        24: {  # 4-3
            439 : 39,
            440 : 55
        },
        #25: {  # stomach

        #},
        26: {  # gallery/boulder
            442 : {32,72}
        },
        #27: {  # tentacle room

        #},
        28: {  # slide room
            441 : 40
        },
        29: {  # 5-1
            443 : 86,
            444 : 18,
            445 : 87
        },
        #30: {  # 5-2

        #},
        #31: {  # water room

        #},
        32: {  # caverns
            446 : 35
        },
        33: {  # 5-3
            447 : 20
        },
        34: {  # hot spring
            448 : 51
        },
        35: {  # polar bear cave
            449 : 85
        },
        #36: {  # 6-1

        #},
        #37: {  # 7-1

        #},
        38: {  # temple
            450 : 57,
            451 : 65
        },
        39: {  # well
            452 : 68
        },
        #40: {  # 7-2

        #},
        41: {  # gong room
            453 : {25,56}
        },
        42: {  # middle room
            454 : 34,
            455 : 36
        },
        43: {  # obstacle course
            456 : 64
        },
        #44: {  # barrel room

        #},
        45: {  # 7-3
            457 : 69
        },
        #46: {  # castle main

        #},
        #47: {  # flooded basement

        #},
        #49: {  # button room

        #},
        #50: {  # elevator room

        #},
        #51: {  # bell tower

        #},
        #52: {

        #},
        #53: {  # 8-1

        #},
        #54: {  # sewers front

        #},
        #55: {  # barrel room

        #},
        56: {  # 8-2
            458 : 83
        },
        #57: {  # main factory

        #},
        #58: {  # rc car room

        #},
        #59: {  # lava room

        #},
        #60: {

        #},
        #61: {  # conveyor room

        #},
        #62: {  # mech room

        #},
        #63: {  # 8-3

        #},
        #64: {  # water basement

        #},
        #65: {  # lobby

        #},
        #66: {  # tank room

        #},
        #67: {  # fan room

        #},
        #68: {

        #},
        #69: {  # MM Lobby

        #},
        #71: {

        #},
        72: {  # coaster entry
            459 : 84
        },
        #73: {  # coaster 1

        #},
        #74: {  # coaster 2

        #},
        #75: {  # haunted house

        #},
        #76: {  # coffin room

        #},
        #77: {  # western land

        #},
        #78: {  # crater

        #},
        #79: {  # outside castle

        #},
        #80: {  # castle main

        #},
        #81: {  # inside climb

        #},
        #82: {  # outside climb

        #},
        #84: {  # Monkey head

        #},
        #85: {  # side entry

        #},
        88: {  # Time station - Hub
            460 : 113,
            461 : 114
        },
        91: {  # Time station - Mini-game Corner
            462: 116
        },
        90: {  # Time station - Training Space
            463 : 115
        }



    }
    bossListLocal = {
        48: {  # CrC boss room
            500: 0x0E69E1
        },
        68: {  # TVT boss room
            501: 0x143E1F
        },
        70: {  # MM_Jake
            503: 0x1422E6
        },
        71: {  # Circus (Professor)
            502: 0x0E6BA9
        },
        # Victory conditions calculated separately, no values there
        83: {  # Specter 1 Phase 1

        },
        86: {  # Specter 1 Phase 2

        },
        87: {  # Specter 2

        }
    }

    items = {
        "Club": 0x1,
        "Net": 0x2,
        "Radar": 0x4,
        "Sling": 0x8,
        "Hoop": 0x10,
        "Punch": 0x20,
        "Flyer": 0x40,
        "Car": 0x80,
        "Key": 0x100,
        "Victory": 0x200,
        "WaterNet": 0x400,
        "ProgWaterNet": 0x401,
        "WaterCatch": 0x402,
        "CB_Lamp": 0x150,
        "DI_Lamp": 0x151,
        "CrC_Lamp": 0x152,
        "CP_Lamp": 0x153,
        "SF_Lamp": 0x154,
        "TVT_Lobby_Lamp": 0x155,
        "TVT_Tank_Lamp": 0x156,
        "MM_Lamp": 0x157,
        "MM_DoubleDoorKey": 0x403,
        "Token": 0x300,
        "Nothing": 0x0,
        "Shirt": 0x210,
        "Triangle": 0x211,
        "BigTriangle": 0x212,
        "Cookie": 0x213,
        "Flash": 0x214,
        "Rocket": 0x215,
        "BiggerTriangle": 0x216,
        "FiveCookies": 0x217,
        "ThreeFlash": 0x218,
        "ThreeRocket": 0x219,
        "BananaPeelTrap": 0x250,
        "GadgetShuffleTrap": 0x251

    }

    caughtStatus = {
        "Unloaded": 0x00,
        "OutOfRender": 0x01,
        "Uncaught": 0x04,
        "Caught": 0x03,
        "PrevCaught": 0x02
    }

    levelStatus = {
        "Locked": 0x00,
        "Complete": 0x01,
        "Hundo": 0x02,
        "Open": 0x03
    }

    gameState = {
        "Sony": 0x0,
        "Menu": 0x3,
        "Cutscene": 0x8,
        "LevelSelect": 0x9,
        "LevelIntro": 0xA,
        "InLevel": 0xB,
        "Cleared": 0xC,
        "TimeStation": 0xD,
        "Save/Load": 0xE,
        "GameOver": 0xF,
        "NewGadget": 0x11,
        "LevelIntroTT": 0x12,
        "InLevelTT": 0x13,
        "ClearedTT": 0x14,
        "Memory": 0x15,
        "JakeIntro": 0x17,
        "Jake": 0x18,
        "JakeCleared": 0x19,
        "Cutscene2": 0x1A,
        "Book": 0x1C,
        "Credits1": 0x1D,
        "Credits2": 0x1E,
        "PostCredits": 0x23,
        "Demo": 0x24
    }

    levelAddresses = {
        11: 0xdfc71,
        12: 0xdfc72,
        13: 0xdfc73,
        21: 0xdfc74,
        22: 0xdfc75,
        23: 0xdfc76,
        31: 0xdfc77,
        41: 0xdfc78,
        42: 0xdfc79,
        43: 0xdfc7A,
        51: 0xdfc7B,
        52: 0xdfc7C,
        53: 0xdfc7D,
        61: 0xdfc7E,
        71: 0xdfc7F,
        72: 0xdfc80,
        73: 0xdfc81,
        81: 0xdfc84,
        82: 0xdfc85,
        83: 0xdfc86,
        91: 0xdfc88,
        92: 0xdfc8e
    }

    levelMonkeyCount = {
        11: 0xdfc99,
        12: 0xdfc9a,
        13: 0xdfc9b,
        21: 0xdfc9c,
        22: 0xdfc9d,
        23: 0xdfc9e,
        31: 0xdfc9f, # Stadium Attack - unused
        41: 0xdfca0,
        42: 0xdfca1,
        43: 0xdfca2,
        51: 0xdfca3,
        52: 0xdfca4,
        53: 0xdfca5,
        61: 0xdfca6, # Gladiator Attack - unused
        71: 0xdfca7,
        72: 0xdfca8,
        73: 0xdfca9,
        81: 0xdfcac,
        82: 0xdfcad,
        83: 0xdfcae,
        91: 0xdfcb0
    }

    # Array order : bytesToWrite, OpenValue, ClosedValue
    doors_addresses = {
        69: { # MM_DoubleDoor
            0x0E7901: [1,0x00,0x10],  # MM_DoubleDoorVisualL1
            0x0E7905: [1,0x10,0x00],  # MM_DoubleDoorVisualL2
            0x0E790D: [1,0xF0,0x00],  # MM_DoubleDoorVisualL3
            0x0E7911: [1,0x00,0x10],  # MM_DoubleDoorVisualL4
            0x0E7921: [1,0x00,0x10],  # MM_DoubleDoorVisualR1
            0x0E7925: [1,0xF0,0x00],  # MM_DoubleDoorVisualR2
            0x0E792D: [1,0x10,0x00],  # MM_DoubleDoorVisualR3
            0x0E7931: [1,0x00,0x10],  # MM_DoubleDoorVisualR4
            0x170B34: [2,0xFC50,0xFE00],  # MM_DoubleDoorHitboxL1
            0x170B38: [2,0x1680,0x18D0],  # MM_DoubleDoorHitboxL2
            0x170B3A: [2,0x0050,0x0200],  # MM_DoubleDoorHitboxL3
            0x170B3E: [2,0x0200,0x0050],  # MM_DoubleDoorHitboxL4
            0x170B6C: [2,0x03B0,0x0200],  # MM_DoubleDoorHitboxR1
            0x170B70: [2,0x1680,0x18D0],  # MM_DoubleDoorHitboxR2
            0x170B72: [2,0x0050,0x0200],  # MM_DoubleDoorHitboxR3
            0x170B76: [2,0x0200,0x0050],  # MM_DoubleDoorHitboxR4
        }
    }

    #Old values, not used but let them here just in case
    #localLamp_localUpdate = 0x097474 # Default: 9062007A. Set this to 0 to disable
    #globalLamp_localUpdate = 0x097574 # Default: 9082007A. Set this to 0 to disable
    #globalLamp_globalUpdate = 0x097568  # 0x097568 Default: 1444000F. Set this to 0 to disable

    # More precise addresses for local monkeys/events
    localLamp_MonkeyDetect = 0x097464
    globalLamp_MonkeyDetect1 = 0x097564
    globalLamp_MonkeyDetect2 = 0x097560

    lampDoors_update = {
        'localLamp_MonkeyDetect_ON':0x3C02800E,
        'localLamp_MonkeyDetect_OFF': 0x00000000,

        'globalLamp_MonkeyDetect1_ON': 0x02712021,
        'globalLamp_MonkeyDetect1_OFF': 0x00000000,
        'globalLamp_MonkeyDetect2_ON': 0x96420126,
        'globalLamp_MonkeyDetect2_OFF': 0x00000000,
    }
    lampDoors_toggles = {
        # CBLamp
        # Array order : bytesToWrite, OpenValue, ClosedValue
        20: {  # CB_LampDoor
            0x0C01AB: [1,0xF4,0xF8],  #CB_LampDoor_Visual1 Open = F4
            0x0C01AF: [1,0x00,0x80],  #CB_LampDoor_Visual2 Open = 00
            0x177B77: [1,0xF4,0xF8],  #CB_LampDoor_Hitbox Open = F4
        },
        53: {  # CP_Lamp
            0x0E7901:[1,0x00,0x10],  # CP_LampDoor_Visual1 Open = 00
            0x0E7903:[1,0x10,0x00],  # CP_LampDoor_Visual2 Open = 10
            0x0E7907:[1,0xF0,0x00],  # CP_LampDoor_Visual3 Open = F0
            0x0E7909:[1,0x00,0x10],  # CP_LampDoor_Visual4 Open = 00
            0x17ABA0:[2,0xE0C0,0xE200],  # CP_LampDoor_Hitbox1 Open = E0C0
            0x17ABA6:[2,0x0040,0x0180],  # CP_LampDoor_Hitbox2 Open = 0040
            0x17ABA9:[2,0x8003,0x8000],  # CP_LampDoor_Hitbox3 Open = 8003
        },
        79: {  # MM_Lamp
            0x0E79D1:[1,0x00,0x10],  # MM_LampDoorL_Visual1 Open = 00
            0x0E79C1:[1,0x00,0x10],  # MM_LampDoorL_Visual2 Open = 00
            0x0E79C5:[1,0xF0,0x00],  # MM_LampDoorL_Visual3 Open = F0
            0x0E79CD:[1,0x10,0x00],  # MM_LampDoorL_Visual4 Open = 10
            0x0E79E1:[1,0x00,0x10],  # MM_LampDoorR_Visual1 Open = 00
            0x0E79E5:[1,0x10,0x00],  # MM_LampDoorR_Visual2 Open = 10
            0x0E79ED:[1,0xF0,0x00],  # MM_LampDoorR_Visual3 Open = F0
            0x0E79F1:[1,0x00,0x10],  # MM_LampDoorR_Visual4 Open = 00
            0x173C08:[2,0xFD40,0xFE80],  # MM_LampDoorL_Hitbox1 Open = FD40
            0x173C0C:[4,0x00400B80,0x018009C0],  # MM_LampDoorL_Hitbox2 Open = 00400B80
            0x173C12:[2,0x0180,0x0040],  # MM_LampDoorL_Hitbox3 Open = 0180
            0x173CB0:[2,0x02C0,0x0180],  # MM_LampDoorR_Hitbox1 Open = 02C0
            0x173CB4:[4,0x00400B80,0x018009C0],  # MM_LampDoorR_Hitbox2 Open = 00400B80
            0x173CBA:[2,0x0180,0x0040]  # MM_LampDoorR_Hitbox3 Open = 0180
        },
        26: {  # DI_Lamp
            0x0BFDAB:[1,0xF2,0xF6],  # DI_LampDoor_Visual1 Open = F2 | Closed = F6
            0x0BFDAF:[1,0x00,0x80],  # DI_LampDoor_Visual2 Open = 00 | Closed = 80
            0x169653:[1,0xF2,0xF6],  # DI_LampDoor_Hitbox Open = F2 | Closed = F6
        },
        46: {  # CrC_Lamp
            0x0E7981:[1,0x00,0x10],  # CrC_LampDoorL_Visual1 Open = 00
            0x0E7985:[1,0xF0,0x00],  # CrC_LampDoorL_Visual2 Open = F0
            0x0E798D:[1,0x10,0x00],  # CrC_LampDoorL_Visual3 Open = 10
            0x0E7991:[1,0x00,0x10],  # CrC_LampDoorL_Visual4 Open = 00
            0x0E79A1:[1,0x00,0x10],  # CrC_LampDoorR_Visual1 Open = 00
            0x0E79A5:[1,0x10,0x00],  # CrC_LampDoorR_Visual2 Open = 10
            0x0E79AD:[1,0xF0,0x00],  # CrC_LampDoorR_Visual3 Open = F0
            0x0E79B1:[1,0x00,0x10],  # CrC_LampDoorR_Visual4 Open = 00
            0x1710C0:[2,0x0040,0x0100],  # CrC_LampDoorL_Hitbox1 Open = 0040
            0x1710C4:[4,0x00400400,0x010002C0],  # CrC_LampDoorL_Hitbox2 Open = 00400400
            0x1710CA:[2,0x0100,0x0040],  # CrC_LampDoorL_Hitbox3 Open = 0100
            0x1710F8:[2,0x03C0,0x0300],  # CrC_LampDoorR_Hitbox1 Open = 03C0
            0x1710FC:[4,0x00400400,0x010002C0],  # CrC_LampDoorR_Hitbox2 Open = 00400400
            0x171102:[2,0x0100,0x0040],  # CrC_LampDoorR_Hitbox3 Open = 0100
        },
        57: {  # SF_Lamp
            0x0C04AD:[1,0x0B,0x0D],  # SF_LampDoor_Visual1 Open = 0B
            0x0C04AF:[1,0x00,0x80],  # SF_LampDoor_Visual2 Open = 00
            0x0C056D:[1,0x11,0x0F],  # SF_LampDoor_Visual3 Open = 11
            0x0C056F:[1,0x00,0x80],  # SF_LampDoor_Visual4 Open = 00
            0x16A499:[1,0x0B,0x0D],  # SF_LampDoor_Hitbox1 Open = 0B
            0x16A461:[1,0x11,0x0F],  # SF_LampDoor_Hitbox2 Open = 11
        },
        65: {  # TVT_LobbyLamp
            0x0C042D:[1,0xFF,0xFD],  # TvtL_LampDoorL_Visual1 Open = FF
            0x0C042F:[1,0x00,0x80],  # TvtL_LampDoorL_Visual2 Open = 00
            0x0C046D:[1,0xF9,0xFB],  # TvtL_LampDoorR_Visual1 Open = F9
            0x0C046F:[1,0x00,0x80],  # TvtL_LampDoorR_Visual2 Open = 00
            0x170C51:[1,0xFF,0xFD],  # TvtL_LampDoorL_Hitbox1 Open = FF
            0x170C65:[1,0x80,0x00],  # TvtL_LampDoorL_Hitbox2 Open = 80
            0x170C89:[1,0xF9,0xFB],  # TvtL_LampDoorR_Hitbox1 Open = F9
            0x170C9D:[1,0x80,0x00],  # TvtL_LampDoorR_Hitbox2 Open = 80
        },
        66: {  # TVT_TankLamp
            0x0C05AC:[4,0x00000DC0,0x80000F40],  # TvtTR_LampDoorL_Visual Open = 00000DC0
            0x0C056C:[4,0x00001240,0x800010C0],  # TvtTR_LampDoorR_Visual Open = 00001240
            0x16C294:[2,0x0DC0,0x0F40],  # TvtTR_LampDoorL_Hitbox1 Open = 0DC0
            0x16C2A9:[1,0x80,0x00],  # TvtTR_LampDoorL_Hitbox2 Open = 80
            0x16C2CC:[2,0x1240,0x10C0],  # TvtTR_LampDoorR_Hitbox1 Open = 1240
            0x16C2E1:[1,0x80,0x00],  # TvtTR_LampDoorR_Hitbox2 Open = 80
        },
    }

    # A bit is 1 if the gadget is unlocked. First bit is club, second is net, etc.
    unlockedGadgetsAddress = 0x0F51C4
    # the gadgets on triangle, square, circle, X on successive bytes
    # club = 0, net = 1, radar = 2, sling = 3, hoop = 4, punch = 5, flyer = 6, car = 7, empty = 255
    triangleGadgetAddress = 0x0F51A8
    squareGadgetAddress = 0x0F51A9
    circleGadgetAddress = 0x0F51AA
    crossGadgetAddress = 0x0F51AB
    # which gadget is currently selected for use
    heldGadgetAddress = 0x0EC2D2
    radarFixAddress = 0x0F5125
    hoopFixAddress = 0x0F5124 # 2 bytes


    tempWaterNetAddress = 0x0DFBE2
    tempWaterCatchAddress = 0x0DFBE3

    temp_MMLobbyDoorAddress = 0x0DFC58


    isUnderwater = 0x0F4DCA
    canDiveAddress = 0x061970 #08018664 - default value (4 bytes)
    canWaterCatchAddress = 0x063C35 # 04 - default value
    swim_oxygenLevelAddress = 0x0F4DC8 # 0x258 = 20 seconds, 0x64 = 3 seconds
    swim_oxygenReplenishSoundAddress = 0x06140C # Default: 0C021DFE, disable: 00000000 4 bytes
    swim_ReplenishOxygenUWAddress = 0x06141C # Default: A4500018, Disable: 00000000 4 bytes
    swim_replenishOxygenOnEntryAddress = 0x0665E8  # Default: A4434DC8, Disable: 00000000 4 bytes
    swim_surfaceDetectionAddress = 0x061420 # Default: 0801853A, disable: 0
    swim_oxygenLowLevelSoundAddress = 0x061458  # Default: 3C02800F, disable: 3C028004 4 bytes
    swim_oxygenMidLevelSoundAddress = 0x061490  # Default: 3C02800F, disable: 3C028004 4 bytes
    
    MM_Professor_RescuedAddress = 0x0DFDDC # Not Rescued = 0, Rescued = 5
    MM_Clown_State = 0x174072
    MM_Natalie_RescuedAddress = 0x0DFDDD # Not Rescued = 0, Rescued = 5
    MM_Natalie_CutsceneState = 0x0DFDDE # play cutscene = 0x00, cutscene played = 0x0D
    MM_Natalie_Rescued_Local = 0x16F34E # When in Room 76: Natalie rescued = 0x01
    MM_Jake_DefeatedAddress = 0x0DFDE0 # Not defeated = 0, Defeated = 5


    temp_MM_Jake_DefeatedAddress = 0x0DFC5A
    temp_MM_Professor_RescuedAddress = 0x0DFC5C
    temp_MM_Natalie_RescuedAddress = 0x0DFC5E

    MM_Lobby_DoubleDoor_OpenAddress = 0x174F5E # Set to 3 for electric fence. If JakeDefeated = 5 it will open the door
    MM_Lobby_JakeDoor_HitboxAddress = 0x1711DD # Set to 128 to remove the hitbox
    MM_Lobby_JakeDoorFenceAddress = 0x174FA6 # Maybe not used
    MM_Lobby_DoorDetection = 0x0963C8 # 4b: Default to 8C820000. 8C800000 Prevent the door detection code from kicking in

    MM_NatalieDoor_Visual1 = 0x0BFCEF # Open 0x00
    MM_NatalieDoor_Visual2 = 0x0BFE0F # Open 0x00
    MM_NatalieDoor_Hitbox = 0x167965  # Open 0x80

    gameRunningAddress = 0x0B01C0

    newGameAddress = 0x137734
    loadGameAddress = 0x137734

    trainingRoomProgressAddress = 0x0DFDCC
    GadgetTrainingsUnlockAddress = 0x0978E8 # 4 Bytes -> Prevent the checkup for activating Training Rooms Gadget Trainings (Default: 8C63FDCC, Disable : 0x00000000)
    currentRoomIdAddress = 0x0F4476
    currentLevelAddress = 0x0F4474
    gameStateAddress = 0x0F4470

    jakeVictoryAddress = 0x0F447A
    unlockedLevelAddress = 0x0DFC70
    requiredApesAddress = 0x0F44D8
    currentApesAddress = 0x0F44B6
    hundoApesAddress = 0x0F44D6
    localApeStartAddress = 0x0DFE00
    startingCoinAddress = 0x0DFB70
    endingCoinAddress = 0x0DFBD2 # Not used,could be used for a loop if current coin system is buggy
    temp_startingCoinAddress = 0x0DFBF0 # Copy all 64 bytes of coin here while entering Level Select
    blank_coinTable = 0x00FF00FF00FF00FF00FF00FF00FF00FF00FF00FF00FF00FF00FF00FF00FF00FF00FF00FF00FF00FF00FF00FF00FF00FF00FF00FF00FF00FF00FF00FF00FF00FF00FF00FF00FF00FF00FF00FF00FF00FF00FF00FF00FF00FF00FF00FF00FF00FF00FF00FF
    blank_coinTable2 = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
    totalCoinsAddress = 0x0F44BA


    SA_CompletedAddress = 0x0DFDD0 # Completed = 0x19, not completed = 00
    Temp_SA_CompletedAddress = 0x0DFC56
    GA_CompletedAddress = 0x0DFDD1 # Completed = 0x19, not completed = 00
    Temp_GA_CompletedAddress = 0x0DFC57


    levelselectFonts = 0x139CF6 # 0x36 = Classic One  0x26 = Current One
    time_attack_Times = 0x0DFD44

    # Custom write/read addresses
    tempLastReceivedArchipelagoID = 0x0DFBD8
    lastReceivedArchipelagoID = 0x0E00E8

    tempKeyCountFromServer = 0x0DFBDE
    keyCountFromServer = 0x0E00EE

    tempTokenCountFromServer = 0x0DFBEC
    tokenCountFromServer = 0x0E00FC

    tempGadgetStateFromServer = 0x0DFBE0
    gadgetStateFromServer = 0x0E00F0

    DR_Block_Pushed = 0x18459A # Address is more of "Entry is open", but same result at the end

    DI_Button_Pressed = 0x1693A6 # Activated = 0x01
    DI_Button_DoorVisual = 0x0BFC8F # Activated = 0x00
    DI_Button_DoorHitBox = 0x1676F7 # Activated = 0xDC
    DI_Button_Visual1 = 0x0BFCB8 # 4 bytes : Activated = 80162250
    DI_Button_Visual2 = 0x0BFCBC # 4 bytes : Activated = 80162268
    DI_Button_Visual3 = 0x0BFCC0 # 4 bytes : Activated = 80162390
    DI_Button_Visual4 = 0x0BFCC4 # 4 bytes : Activated = 80162288

    CrC_Basement_ButtonPressed = 0x184D46 # Pressed = 0x01
    CrC_Basement_DoorHitBox1 = 0x1810A8 #[4b] Activated = F200F808
    CrC_Basement_DoorHitBox2 = 0x1810AC #[4b] Activated =  0008FB00
    CrC_Basement_DoorHitBox3 = 0x1810B0 #[4b] Activated =  01000400
    CrC_Basement_DoorVisual1 = 0x0E7AC1 # Activated = 0x00
    CrC_Basement_DoorVisual2 = 0x0E7ACD # Activated = 0xF0
    CrC_Basement_ButtonVisual1 = 0x0C1518 # [4b] Activated = 80178ADC
    CrC_Basement_ButtonVisual2 = 0x0C151C # [4b] Activated = 80178AF4
    CrC_Basement_ButtonVisual3 = 0x0C1520 # [4b] Activated = 80178C14
    CrC_Basement_ButtonVisual4 = 0x0C1524 # [4b] Activated = 80178B0C


    CrC_Water_ButtonPressed = 0x173242 # 1 byte : While in room 49 -> Pressed = 0x01, Unpressed = 0x00 -> Send event object
    CrC_Water_DoorVisual = 0x0C05AE  # 1 byte : Open = 0x00 , Closed = 0x16
    # CrC_Button_Visual1 = 0x0C0778 # 4 bytes : Activated =
    # CrC_Button_Visual2 = 0x0C077C  # 4 bytes : Activated =
    # CrC_Button_Visual3 = 0x0C0780  # 4 bytes : Activated =
    # CrC_Button_Visual4 = 0x0C0784  # 4 bytes : Activated =
    # Set TR4_TransitionEnabled to 0x00 to permit access to the transition, 0x03 to deny transition

    MM_Painting_Button = 0x17EACE # Active 0x01 ROOM = 82
    MM_Painting_Visual = 0x0C1569 # Active Value = 0x06
    MM_Painting_HitBox = 0x18CF31  # Active Value = 0x06
    MM_Painting_VisualStair1 = 0x0C0EAE # Active Value = 0x03
    MM_Painting_VisualStair2 = 0x0C0ECE # Active Value = 0x03
    MM_Painting_VisualStair3 = 0x0C0EEE # Active Value = 0x03
    MM_Painting_HitBoxStair1 = 0x18CEA1 # Active Value = 0x00
    MM_Painting_HitBoxStair2 = 0x18CED9 # Active Value = 0x00
    MM_Painting_HitBoxStair3 = 0x18CF11 # Active Value = 0x00
    MM_Painting_VisualFence = 0x0C0F4E # Active Value = 0x00
    MM_Painting_HitBoxFence = 0x18CF81 # Active Value = 0x80

    MM_MonkeyHead_Button = 0x174ECE # Active 0x01 ROOM = 84
    MM_MonkeyHead_Door = 0x0AFA22 # Lasers = 0x00 NO LASERS = 0x01

    TVT_Lobby_Button = 0x1710E6 # Active 0x01 ROOM = 65

    TVT_Lobby_Water_HitBox = 0x170EFF # Active Value = 0
    TVT_Lobby_Water_DoorHitbox1 = 0x170E5D # Active Value = 80
    TVT_Lobby_Water_DoorHitbox2 = 0x170E25 # Active Value = 80
    TVT_Lobby_Water_DoorVisualP1 = 0x0C04CF # Active Value = 0
    TVT_Lobby_Water_DoorVisualP2 = 0x0C04EF # Active Value = 0
    TVT_Lobby_Water_BackColor1 = 0x0C0698 # Active Value = AC78
    TVT_Lobby_Water_BackColor2 = 0x0C069C # Active Value = AC90
    TVT_Lobby_Water_BackColor3 = 0x0C06A0 # Active Value = AE14
    TVT_Lobby_Water_BackColor4 = 0x0C06A4 # Active Value = AC9C
    TVT_Lobby_Water_BackColor5 = 0x0C06B8 # Active Value = B1B8
    TVT_Lobby_Water_ColorS1P1 = 0x0C06BC # Active Value = B1D0
    TVT_Lobby_Water_ColorS1P2 = 0x0C06C0 # Active Value = B2EC
    TVT_Lobby_Water_TunnelColorS1P1 = 0x0C06C4 # Active Value = B1E4
    TVT_Lobby_Water_TunnelColorS1P2 = 0x0C07B8 # Active Value = B9A0
    TVT_Lobby_Water_TunnelColorS2P1 = 0x0C07BC # Active Value = B9B8
    TVT_Lobby_Water_TunnelColorS2P2 = 0x0C07C0 # Active Value = BB44
    TVT_Lobby_Water_TunnelColorS2P3 = 0x0C07C4 # Active Value = B9C4
    TVT_Lobby_WaterVisual1 = 0x0C07EA # Active Value = F70C
    TVT_Lobby_WaterVisual2 = 0x0C07EF # Active Value = 0
    TVT_Lobby_WaterVisual3 = 0x0C080A # Active Value = F70C
    TVT_Lobby_WaterVisual4 = 0x0C080F # Active Value = 0


    tempCB_LampAddress = 0x0DFBE4
    tempDI_LampAddress = 0x0DFBE5
    tempCrC_LampAddress = 0x0DFBE6
    tempCP_LampAddress = 0x0DFBE7
    tempSF_LampAddress = 0x0DFBE8
    tempTVT_Lobby_LampAddress = 0x0DFBE9
    tempTVT_Tank_LampAddress = 0x0DFBEA
    tempMM_LampAddress = 0x0DFBEB

    currentLoadedSave = 0x0E0034 # Not used for now, but could be used somehow
    menuStateAddress = 0x0A9A1B
    menuState2Address = 0x0A9A23
    Controls_DPAD_STARTSELECT_L3R3 = 0x0B87A2
    Controls_TriggersShapes = 0x0B87A3

    punchVisualAddress = 0x0E78C0
    transitionPhase = 0x0F447C # Default: 8C63FDCC
    # 0x01 = ?? Maybe spawning
    # 0x02 = Black screen fading out
    # 0x03 = in level, not near a transition
    # 0x04 or 0x05 = near a transition
    # 0x06 = Starting transition
    # 0x19 = Spawning in air


    # Junk addresses
    energyChipsAddress = 0x0F44B8
    cookieAddress = 0x0EC2C8
    instakillAddress = 0x0EC2C9
    tankLife = 0x0BF826
    livesAddress = 0x0F448C
    flashAddress = 0x0F51C1
    rocketAddress = 0x0F51C2

    # LevelSelection addresses (Number -1)
    selectedWorldAddress = 0x139BC4
    selectedLevelAddress = 0x139BCC
    worldIsScrollingRight = 0x139BD9 # 2 bytes: 0xFFFF = you are changing to the next world
    worldScrollToRightDPAD = 0x1381D4 # 2 bytes: Enabled = 0009, Disabled = 0000
    worldScrollToRightR1 = 0x138270  # 2 bytes: Enabled = 0009, Disabled = 0000

    enteredWorldAddress = 0x0F461C
    enteredLevelAddress = 0x0F461D
    startOfLevelNames = 0x1399E8
    startOfEraNames = 0x139B20

    # Rooms ER values here
    Spike_X_PosAddress = 0x0EC204
    Spike_Y_PosAddress = 0x0EC208
    Spike_Z_PosAddress = 0x0EC20C
    Nearby_RoomIDAddress = 0x0E38B4
    Nearby_DoorIDAddress   = 0x0E38A4

    TargetRoomID1Address = 0x154264
    TR1_DoorIDAddress = 0x154268
    TargetRoomID2Address = 0x15428C
    TR2_DoorIDAddress = 0x154290
    TargetRoomID3Address = 0x1542B4
    TR3_DoorIDAddress = 0x1542B8
    TargetRoomID4Address = 0x1542DC
    TR4_DoorIDAddress = 0x1542E0
    TR4_TransitionEnabled = 0x1542BC # For CrC_Boss_Door -> Blocked value : 0x03, Opened Value : 0x00
    TargetRoomID5Address = 0x154304
    TR5_DoorIDAddress = 0x154308
    TargetRoomID6Address = 0x15432C
    TR6_DoorIDAddress = 0x154330
    TargetRoomID7Address = 0x154354
    TR7_DoorIDAddress = 0x154358
    TargetRoomID8Address = 0x15437C
    TR8_DoorIDAddress = 0x154380

    localLevelState = 0x0F447E # Same as level state, but can be changed to impact some behaviors (Like Kickout Prevention)

    kickoutofLevelAddress = 0x097B98  # 4 bytes: Default 84830188, Disable kickout = 00000000 (050E67EC)
    kickoutofLevelAddress2 = 0x097B70  # BETTER 4 bytes: Default 24020001, Disable kickout = 00000000

    CrC_BossPhaseAddress = 0x17475E
    CrC_BossLife = 0x0E69E1

    # 0 :not started
    # 1 and 2 : In cinematic
    # 3 : In fight
    # 4 : Opening door
    # 5 : Victory

    TVT_BossPhase = 0x17C5A2
    TVT_BossLife = 0x143E1F
    # 1 In cinematic for boss
    # 2 Boss in waiting
    # 3 Boss in progress

    CrC_DoorVisual = 0x0C062B
    CrC_DoorHitBox = 0x164FFB

    CrC_kickoutofLevelAddress = 0x097B20  # 4 bytes: Default 86020166, Disable kickout = 00000000
    CrC_kickoutofLevelAddress2 = 0x097B24 # 4 bytes: Default 84830188, Disable kickout = 00000000
    TVT_kickoutofLevelAddress = 0x097B00  # 4 bytes: Default 84830188, Disable kickout = 00000000

    # 1 = "Net down"
    # 8 = "Net down + can catch"
    gadgetUseStateAddress = 0x0B20CC
    spikeStateAddress = 0x0EC250
    spikeState2Address = 0x0EC23E
    spikeIdleTimer = 0x0EC328 # Put this to 0x0000 to wake up
    spikeGroundStateAddress = 0x0EC23D
    spikeHittableAddress = 0x0EC227
    spikeUltraInstinctAddress = 0x0EC2E2



    # Specter bosses values
    S1_P1_Life = 0x1408FB
    S1_P2_State = 0x144A04
    S1_P2_Life = 0x144A06
    S1_P1_FightTrigger = 0x16A5B2 # 1 byte. Put to 0x0D to prevent the fight, 0x00 to allow the fight
    S1_Cutscene_Redirection = 0x137C28  # 4 bytes. When GameState is 0A, change the last 2 bytes to redirect another gamestate after the cutscene (Redirect to time station = 2403000D)
    S2_isCaptured = 0x142328
    S2_Cutscene_Redirection = 0x05C5F0  # 4 bytes. Change the last 2 bytes to redirect another gamestate after the cutscene (Redirect to time station = 2403000D)

    # S1_LArm_Life = 0x14474E
    # S1_RArm_Life = 0x1446B6

    timeStationMailboxStart = 0x0C1798
    gotMailAddress = 0x0BBD99
    gotMailAddress_PAL = 0x0BBE59
    # DIFF = NTSC + C0
    # Seems to be shared with other variables,
    # Detect when readingMail = 2 then check what mailbox it is
    mailboxIDAddress = 0x0A6CD2
    mailboxIDAddress_PAL = 0x0A6DB2
    #DIFF = NTSC + E0
    # Associate by room just to be sure, since some of them have the same ID (Ex.: Thick Jungle have 2 IDs = 71)
    levels = {
        "Fossil": 0x01,
        "Primordial": 0x02,
        "Molten": 0x03,
        "Thick": 0x04,
        "Dark": 0x05,
        "Cryptic": 0x06,
        "Stadium": 0x07,
        "Crabby": 0x08,
        "Coral": 0x09,
        "Dexter": 0x0A,
        "Snowy": 0x0B,
        "Frosty": 0x0C,
        "Hot": 0x0D,
        "Gladiator": 0x0E,
        "Sushi": 0x0F,
        "Wabi": 0x10,
        "Crumbling": 0x11,
        "City": 0x14,
        "Factory": 0x15,
        "TV": 0x16,
        "Specter": 0x18,
        "S_Jake": 0x19,
        "S_Circus": 0x1A,
        "S_Coaster": 0x1B,
        "S_Western Land": 0x1C,
        "S_Castle": 0x1D,
        "Peak": 0x1E,
        "Time": 0x1F,
        "Training": 0x20
    }

