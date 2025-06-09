﻿from worlds.tetrisattack import VersusGoal
from worlds.tetrisattack.Options import StarterPack, StageClearMode, PuzzleGoal, VersusMode
from worlds.tetrisattack.test import TetrisAttackTestBase


class TestVersusMinimumDifficulty(TetrisAttackTestBase):
    options = {
        "stage_clear_goal": False,
        "puzzle_goal": PuzzleGoal.option_no_puzzle,
        "versus_goal": VersusGoal.option_very_hard,
        "starter_pack": StarterPack.option_stage_clear_round_1,
        "versus_mode": VersusMode.option_minimum_difficulty
    }

class TestVersusMinimumProgressive(TetrisAttackTestBase):
    options = {
        "stage_clear_goal": False,
        "puzzle_goal": PuzzleGoal.option_no_puzzle,
        "versus_goal": VersusGoal.option_very_hard,
        "starter_pack": StarterPack.option_vs_two_stages,
        "versus_mode": VersusMode.option_minimum_progressive
    }

class TestVersusGoalDifficulty(TetrisAttackTestBase):
    options = {
        "stage_clear_goal": False,
        "puzzle_goal": PuzzleGoal.option_no_puzzle,
        "versus_goal": VersusGoal.option_very_hard,
        "starter_pack": StarterPack.option_vs_two_stages,
        "versus_mode": VersusMode.option_goal_difficulty
    }

class TestVersusEasyProgressive(TetrisAttackTestBase):
    options = {
        "stage_clear_goal": False,
        "puzzle_goal": PuzzleGoal.option_no_puzzle,
        "versus_goal": VersusGoal.option_easy,
        "starter_pack": StarterPack.option_vs_two_stages
    }
