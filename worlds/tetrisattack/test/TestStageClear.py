﻿from worlds.tetrisattack import VersusGoal
from worlds.tetrisattack.Options import StarterPack, StageClearMode, PuzzleGoal
from worlds.tetrisattack.test import TetrisAttackTestBase


class TestStageClearFalsePuzzleStart(TetrisAttackTestBase):
    options = {
        "stage_clear_goal": True,
        "puzzle_goal": PuzzleGoal.option_no_puzzle,
        "versus_goal": VersusGoal.option_no_vs,
        "starter_pack": StarterPack.option_puzzle_level_1,
        "stage_clear_filler": 0
    }


class TestStageClearRound6Start(TetrisAttackTestBase):
    options = {
        "stage_clear_goal": True,
        "puzzle_goal": PuzzleGoal.option_no_puzzle,
        "versus_goal": VersusGoal.option_no_vs,
        "starter_pack": StarterPack.option_stage_clear_round_6,
        "stage_clear_filler": 0
    }

    def test_incremental_unlocks(self) -> None:
        locations = ["Stage Clear 3-5 Clear"]
        items = [["Stage Clear Round 3 Gate",
                  "Stage Clear Progressive Round 3 Unlock",
                  "Stage Clear Progressive Round 3 Unlock",
                  "Stage Clear Progressive Round 3 Unlock",
                  "Stage Clear Progressive Round 3 Unlock",
                  "Stage Clear Progressive Round 3 Unlock"]]
        self.assertAccessDependency(locations, items, only_check_listed=True)


class TestStageClearWholeRounds(TetrisAttackTestBase):
    options = {
        "stage_clear_goal": True,
        "puzzle_goal": PuzzleGoal.option_no_puzzle,
        "versus_goal": VersusGoal.option_no_vs,
        "stage_clear_mode": StageClearMode.option_whole_rounds,
        "stage_clear_filler": 0
    }


class TestStageClearIndividualStages(TetrisAttackTestBase):
    options = {
        "stage_clear_goal": True,
        "puzzle_goal": PuzzleGoal.option_no_puzzle,
        "versus_goal": VersusGoal.option_no_vs,
        "stage_clear_mode": StageClearMode.option_individual_stages,
        "stage_clear_filler": 0
    }


class TestStageClearSkippableStages(TetrisAttackTestBase):
    options = {
        "stage_clear_goal": True,
        "puzzle_goal": PuzzleGoal.option_no_puzzle,
        "versus_goal": VersusGoal.option_no_vs,
        "stage_clear_mode": StageClearMode.option_skippable,
        "stage_clear_filler": 0
    }


class TestStageClearSkippableStagesWithRoundGates(TetrisAttackTestBase):
    options = {
        "stage_clear_goal": True,
        "puzzle_goal": PuzzleGoal.option_no_puzzle,
        "versus_goal": VersusGoal.option_no_vs,
        "stage_clear_mode": StageClearMode.option_skippable_with_round_gate,
        "stage_clear_filler": 0
    }


class TestStageClearMaxFiller(TetrisAttackTestBase):
    options = {
        "stage_clear_goal": True,
        "puzzle_goal": PuzzleGoal.option_no_puzzle,
        "versus_goal": VersusGoal.option_no_vs,
        "starter_pack": StarterPack.option_stage_clear_round_6,
        "stage_clear_mode": StageClearMode.option_whole_rounds,
        "stage_clear_filler": 1,
        "special_stage_traps": 30
    }
