﻿from typing import TYPE_CHECKING

from BaseClasses import CollectionState
from .Options import StarterPack, StageClearMode, PuzzleMode, PuzzleGoal, PuzzleInclusion, VersusGoal, VersusInclusion, \
    VersusMode
from .data.Constants import versus_unlock_names

if TYPE_CHECKING:
    from . import TetrisAttackWorld


def stage_clear_round_completable(world: "TetrisAttackWorld", state: CollectionState, round_number: int):
    if not stage_clear_round_accessible(world, state, round_number):
        return False

    match world.options.stage_clear_mode:
        case StageClearMode.option_whole_rounds:
            return True
        case StageClearMode.option_individual_stages \
             | StageClearMode.option_incremental \
             | StageClearMode.option_incremental_with_round_gate:
            return state.has(f"Stage Clear Progressive Round {round_number} Unlock", world.player, 5)
        case StageClearMode.option_skippable \
             | StageClearMode.option_skippable_with_round_gate:
            return (state.has(f"Stage Clear {round_number}-1 Unlock", world.player)
                    and state.has(f"Stage Clear {round_number}-2 Unlock", world.player)
                    and state.has(f"Stage Clear {round_number}-3 Unlock", world.player)
                    and state.has(f"Stage Clear {round_number}-4 Unlock", world.player)
                    and state.has(f"Stage Clear {round_number}-5 Unlock", world.player))
        case _:
            raise Exception(
                f"Cannot determine round completion from Stage Clear mode {world.options.stage_clear_mode}")


def stage_clear_stage_completable(world: "TetrisAttackWorld", state, round_number: int, stage_number: int):
    if not stage_clear_round_accessible(world, state, round_number):
        return False

    match world.options.stage_clear_mode:
        case StageClearMode.option_whole_rounds \
             | StageClearMode.option_individual_stages:
            return True
        case StageClearMode.option_incremental \
             | StageClearMode.option_incremental_with_round_gate:
            return state.has(f"Stage Clear Progressive Round {round_number} Unlock", world.player, stage_number)
        case StageClearMode.option_skippable \
             | StageClearMode.option_skippable_with_round_gate:
            return state.has(f"Stage Clear {round_number}-{stage_number} Unlock", world.player)
        case _:
            raise Exception(
                f"Cannot determine stage completion from Stage Clear mode {world.options.stage_clear_mode}")


def stage_clear_round_accessible(world: "TetrisAttackWorld", state, round_number: int):
    match world.options.stage_clear_mode:
        case StageClearMode.option_whole_rounds \
             | StageClearMode.option_skippable_with_round_gate \
             | StageClearMode.option_incremental_with_round_gate:
            return state.has(f"Stage Clear Round {round_number} Gate", world.player)
        case StageClearMode.option_individual_stages:
            return state.has(f"Stage Clear Progressive Round {round_number} Unlock", world.player, 5)
        case StageClearMode.option_incremental \
             | StageClearMode.option_skippable:
            return True
        case _:
            raise Exception(
                f"Cannot determine round accessibility from Stage Clear mode {world.options.stage_clear_mode}")


def stage_clear_round_clears_included(world: "TetrisAttackWorld"):
    if not world.options.stage_clear_goal and not world.options.stage_clear_inclusion:
        return False
    if world.options.stage_clear_filler:
        return True
    match world.options.stage_clear_mode:
        case StageClearMode.option_whole_rounds \
             | StageClearMode.option_skippable_with_round_gate \
             | StageClearMode.option_incremental_with_round_gate:
            return True
        case StageClearMode.option_individual_stages:
            # Due to branching logic in the fill stage, not adding filler leads to unbeatable seeds
            # TODO: Check for other filler options before forcing round clear locations, or find a way to fill the locations smarter
            return True
        case StageClearMode.option_incremental \
             | StageClearMode.option_skippable:
            return False
        case _:
            raise Exception(
                f"Cannot determine round clear inclusions from Stage Clear mode {world.options.stage_clear_mode}")


def stage_clear_individual_clears_included(world: "TetrisAttackWorld"):
    if not world.options.stage_clear_goal and not world.options.stage_clear_inclusion:
        return False
    if world.options.stage_clear_filler:
        return True
    match world.options.stage_clear_mode:
        case StageClearMode.option_whole_rounds:
            return False
        case StageClearMode.option_individual_stages \
             | StageClearMode.option_incremental \
             | StageClearMode.option_incremental_with_round_gate \
             | StageClearMode.option_skippable_with_round_gate \
             | StageClearMode.option_skippable:
            return True
        case _:
            raise Exception(
                f"Cannot determine individual clear inclusions from Stage Clear mode {world.options.stage_clear_mode}")


def stage_clear_progressive_unlocks_included(world: "TetrisAttackWorld"):
    if not world.options.stage_clear_goal and not world.options.stage_clear_inclusion:
        return False
    match world.options.stage_clear_mode:
        case StageClearMode.option_whole_rounds \
             | StageClearMode.option_skippable_with_round_gate \
             | StageClearMode.option_skippable:
            return False
        case StageClearMode.option_individual_stages \
             | StageClearMode.option_incremental \
             | StageClearMode.option_incremental_with_round_gate:
            return True
        case _:
            raise Exception(
                f"Cannot determine progressive unlock inclusions from Stage Clear mode {world.options.stage_clear_mode}")


def stage_clear_individual_unlocks_included(world: "TetrisAttackWorld"):
    if not world.options.stage_clear_goal and not world.options.stage_clear_inclusion:
        return False
    match world.options.stage_clear_mode:
        case StageClearMode.option_whole_rounds \
             | StageClearMode.option_individual_stages \
             | StageClearMode.option_incremental \
             | StageClearMode.option_incremental_with_round_gate:
            return False
        case StageClearMode.option_skippable_with_round_gate \
             | StageClearMode.option_skippable:
            return True
        case _:
            raise Exception(
                f"Cannot determine individual unlock inclusions from Stage Clear mode {world.options.stage_clear_mode}")


def stage_clear_round_gates_included(world: "TetrisAttackWorld"):
    if not world.options.stage_clear_goal and not world.options.stage_clear_inclusion:
        return False
    match world.options.stage_clear_mode:
        case StageClearMode.option_whole_rounds \
             | StageClearMode.option_incremental_with_round_gate \
             | StageClearMode.option_skippable_with_round_gate:
            return True
        case StageClearMode.option_individual_stages \
             | StageClearMode.option_incremental \
             | StageClearMode.option_skippable:
            return False
        case _:
            raise Exception(
                f"Cannot determine round gate inclusions from Stage Clear mode {world.options.stage_clear_mode}")


def stage_clear_able_to_win(world: "TetrisAttackWorld", state):
    if world.options.starter_pack == StarterPack.option_stage_clear_round_6:
        return state.has("Stage Clear Last Stage", world.player)
    return stage_clear_round_completable(world, state, 6)


def round_clear_has_special(round_index: int, trap_count: int):
    match trap_count:
        case 1:
            if round_index == 3:
                return True
        case 2:
            if round_index == 3 or round_index == 6:
                return True
        case 3:
            if round_index == 2 or round_index == 4 or round_index == 6:
                return True
        case 4:
            if round_index == 2 or round_index == 3 or round_index == 4 or round_index == 5:
                return True
        case 5:
            if round_index != 6:
                return True
        case 6:
            return True
    return False


def stage_clear_has_special(round_index: int, stage_index: int, trap_count: int):
    if trap_count > 6:
        before_clear = round((round_index * 5 + stage_index - 6) * trap_count / 30)
        after_clear = round((round_index * 5 + stage_index - 5) * trap_count / 30)
        return before_clear != after_clear
    return False


def puzzle_level_completable(world: "TetrisAttackWorld", state: CollectionState, level_number: int):
    if not puzzle_level_accessible(world, state, level_number):
        return False

    base_name = "Puzzle"
    if level_number > 6:
        level_number -= 6
        base_name = "Extra Puzzle"

    match world.options.puzzle_mode:
        case PuzzleMode.option_whole_levels:
            return True
        case PuzzleMode.option_individual_stages \
             | PuzzleMode.option_incremental \
             | PuzzleMode.option_incremental_with_level_gate:
            return state.has(f"{base_name} Progressive Level {level_number} Unlock", world.player, 10)
        case PuzzleMode.option_skippable \
             | PuzzleMode.option_skippable_with_level_gate:
            return (state.has(f"{base_name} {level_number}-01 Unlock", world.player)
                    and state.has(f"{base_name} {level_number}-02 Unlock", world.player)
                    and state.has(f"{base_name} {level_number}-03 Unlock", world.player)
                    and state.has(f"{base_name} {level_number}-04 Unlock", world.player)
                    and state.has(f"{base_name} {level_number}-05 Unlock", world.player)
                    and state.has(f"{base_name} {level_number}-06 Unlock", world.player)
                    and state.has(f"{base_name} {level_number}-07 Unlock", world.player)
                    and state.has(f"{base_name} {level_number}-08 Unlock", world.player)
                    and state.has(f"{base_name} {level_number}-09 Unlock", world.player)
                    and state.has(f"{base_name} {level_number}-10 Unlock", world.player))
        case _:
            raise Exception(
                f"Cannot determine round completion from Stage Clear mode {world.options.puzzle_mode}")


def puzzle_stage_completable(world: "TetrisAttackWorld", state, level_number: int, stage_number: int):
    if not puzzle_level_accessible(world, state, level_number):
        return False

    base_name = "Puzzle"
    if level_number > 6:
        level_number -= 6
        base_name = "Extra Puzzle"

    match world.options.puzzle_mode:
        case PuzzleMode.option_whole_levels \
             | PuzzleMode.option_individual_stages:
            return True
        case PuzzleMode.option_incremental \
             | PuzzleMode.option_incremental_with_level_gate:
            return state.has(f"{base_name} Progressive Level {level_number} Unlock", world.player, stage_number)
        case PuzzleMode.option_skippable \
             | PuzzleMode.option_skippable_with_level_gate:
            if stage_number >= 10:
                return state.has(f"{base_name} {level_number}-10 Unlock", world.player)
            return state.has(f"{base_name} {level_number}-0{stage_number} Unlock", world.player)
        case _:
            raise Exception(
                f"Cannot determine stage completion from Puzzle mode {world.options.puzzle_mode}")


def puzzle_level_accessible(world: "TetrisAttackWorld", state, level_number: int):
    base_name = "Puzzle"
    if level_number > 6:
        level_number -= 6
        base_name = "Extra Puzzle"

    match world.options.puzzle_mode:
        case PuzzleMode.option_whole_levels \
             | PuzzleMode.option_skippable_with_level_gate \
             | PuzzleMode.option_incremental_with_level_gate:
            return state.has(f"{base_name} Level {level_number} Gate", world.player)
        case PuzzleMode.option_individual_stages:
            return state.has(f"{base_name} Progressive Level {level_number} Unlock", world.player, 10)
        case PuzzleMode.option_incremental \
             | PuzzleMode.option_skippable:
            return True
        case _:
            raise Exception(
                f"Cannot determine round accessibility from Puzzle mode {world.options.puzzle_mode}")


def puzzle_round_clears_included(world: "TetrisAttackWorld"):
    if world.options.puzzle_goal == PuzzleGoal.option_no_puzzle and world.options.puzzle_inclusion == PuzzleInclusion.option_no_puzzle:
        return False
    if world.options.puzzle_filler:
        return True
    match world.options.puzzle_mode:
        case PuzzleMode.option_whole_levels \
             | PuzzleMode.option_skippable_with_level_gate \
             | PuzzleMode.option_incremental_with_level_gate:
            return True
        case PuzzleMode.option_individual_stages:
            # Due to branching logic in the fill stage, not adding filler leads to unbeatable seeds
            # TODO: Check for other filler options before forcing round clear locations, or find a way to fill the locations smarter
            return True
        case PuzzleMode.option_incremental \
             | PuzzleMode.option_skippable:
            return False
        case _:
            raise Exception(
                f"Cannot determine round clear inclusions from Puzzle mode {world.options.puzzle_mode}")


def puzzle_individual_clears_included(world: "TetrisAttackWorld"):
    if world.options.puzzle_goal == PuzzleGoal.option_no_puzzle and world.options.puzzle_inclusion == PuzzleInclusion.option_no_puzzle:
        return False
    if world.options.puzzle_filler:
        return True
    match world.options.puzzle_mode:
        case PuzzleMode.option_whole_levels:
            return False
        case PuzzleMode.option_individual_stages \
             | PuzzleMode.option_incremental \
             | PuzzleMode.option_incremental_with_level_gate \
             | PuzzleMode.option_skippable_with_level_gate \
             | PuzzleMode.option_skippable:
            return True
        case _:
            raise Exception(
                f"Cannot determine individual clear inclusions from Puzzle mode {world.options.puzzle_mode}")


def puzzle_progressive_unlocks_included(world: "TetrisAttackWorld"):
    if world.options.puzzle_goal == PuzzleGoal.option_no_puzzle and world.options.puzzle_inclusion == PuzzleInclusion.option_no_puzzle:
        return False
    match world.options.puzzle_mode:
        case PuzzleMode.option_whole_levels \
             | PuzzleMode.option_skippable_with_level_gate \
             | PuzzleMode.option_skippable:
            return False
        case PuzzleMode.option_individual_stages \
             | PuzzleMode.option_incremental \
             | PuzzleMode.option_incremental_with_level_gate:
            return True
        case _:
            raise Exception(
                f"Cannot determine progressive unlock inclusions from Puzzle mode {world.options.puzzle_mode}")


def puzzle_individual_unlocks_included(world: "TetrisAttackWorld"):
    if world.options.puzzle_goal == PuzzleGoal.option_no_puzzle and world.options.puzzle_inclusion == PuzzleInclusion.option_no_puzzle:
        return False
    match world.options.puzzle_mode:
        case PuzzleMode.option_whole_levels \
             | PuzzleMode.option_individual_stages \
             | PuzzleMode.option_incremental \
             | PuzzleMode.option_incremental_with_level_gate:
            return False
        case PuzzleMode.option_skippable_with_level_gate \
             | PuzzleMode.option_skippable:
            return True
        case _:
            raise Exception(
                f"Cannot determine individual unlock inclusions from Puzzle mode {world.options.puzzle_mode}")


def puzzle_level_gates_included(world: "TetrisAttackWorld"):
    if world.options.puzzle_goal == PuzzleGoal.option_no_puzzle and world.options.puzzle_inclusion == PuzzleInclusion.option_no_puzzle:
        return False
    match world.options.puzzle_mode:
        case PuzzleMode.option_whole_levels \
             | PuzzleMode.option_incremental_with_level_gate \
             | PuzzleMode.option_skippable_with_level_gate:
            return True
        case PuzzleMode.option_individual_stages \
             | PuzzleMode.option_incremental \
             | PuzzleMode.option_skippable:
            return False
        case _:
            raise Exception(
                f"Cannot determine level gate inclusions from Puzzle mode {world.options.puzzle_mode}")


def puzzle_able_to_win(world: "TetrisAttackWorld", state):
    match world.options.puzzle_goal:
        case PuzzleGoal.option_puzzle:
            return puzzle_level_completable(world, state, 6)
        case PuzzleGoal.option_extra_puzzle:
            return puzzle_level_completable(world, state, 12)
        case PuzzleGoal.option_puzzle_and_extra_puzzle:
            return puzzle_level_completable(world, state, 6) and puzzle_level_completable(world, state, 12)
        case PuzzleGoal.option_puzzle_or_extra_puzzle:
            return puzzle_level_completable(world, state, 6) or puzzle_level_completable(world, state, 12)
        case _:
            raise Exception(f"Cannot determine puzzle clearability from goal {world.options.puzzle_goal}")


def versus_progressive_unlocks_included(world: "TetrisAttackWorld"):
    if world.options.versus_goal == VersusGoal.option_no_vs and not world.options.versus_inclusion:
        return False
    return world.options.versus_mode == VersusMode.option_minimum_progressive or world.options.versus_mode == VersusMode.option_goal_progressive


def versus_individual_unlocks_included(world: "TetrisAttackWorld"):
    if world.options.versus_goal == VersusGoal.option_no_vs and not world.options.versus_inclusion:
        return False
    return world.options.versus_mode == VersusMode.option_minimum_difficulty or world.options.versus_mode == VersusMode.option_goal_difficulty


def versus_stage_completable(world: "TetrisAttackWorld", state, stage_number: int, difficulty_level: int):
    if stage_number > 8 and not cave_of_wickedness_accessible(world, state):
        return False
    return state.has("Vs. Progressive Stage Unlock", world.player, stage_number) or state.has(
        versus_unlock_names[stage_number - 1], world.player)


def cave_of_wickedness_accessible(world: "TetrisAttackWorld", state):
    return state.has("Mt. Wickedness Gate", world.player)


def versus_able_to_win(world: "TetrisAttackWorld", state):
    match world.options.versus_goal:
        case VersusGoal.option_easy:
            return versus_stage_completable(world, state, 10, 1)
        case VersusGoal.option_normal:
            return versus_stage_completable(world, state, 11, 2)
        case VersusGoal.option_hard:
            return versus_stage_completable(world, state, 12, 3)
        case VersusGoal.option_very_hard:
            return versus_stage_completable(world, state, 12, 4)
        case _:
            raise Exception(f"Cannot determine versus clearability from goal {world.options.versus_goal}")


def versus_stage_clears_included(world: "TetrisAttackWorld"):
    if world.options.versus_goal == VersusGoal.option_no_vs and not world.options.versus_inclusion:
        return False
    return True


def goal_locations_included(world: "TetrisAttackWorld"):
    mode_count = 0
    if world.options.stage_clear_goal or world.options.stage_clear_inclusion:
        mode_count += 1
    if world.options.puzzle_goal != PuzzleGoal.option_no_puzzle or world.options.puzzle_inclusion != PuzzleInclusion.option_no_puzzle:
        mode_count += 1
    if world.options.versus_goal != VersusGoal.option_no_vs or world.options.versus_inclusion:
        mode_count += 1
    return mode_count > 1


def able_to_win(world: "TetrisAttackWorld", state):
    if world.options.stage_clear_goal and not stage_clear_able_to_win(world, state):
        return False
    if world.options.puzzle_goal != PuzzleGoal.option_no_puzzle and not puzzle_able_to_win(world, state):
        return False
    if world.options.versus_goal != VersusGoal.option_no_vs and not versus_able_to_win(world, state):
        return False
    return True


def get_starting_sc_round(world: "TetrisAttackWorld"):
    include_puzzle = world.options.puzzle_goal != PuzzleGoal.option_no_puzzle or world.options.puzzle_inclusion != PuzzleInclusion.option_no_puzzle
    include_vs = world.options.versus_goal != VersusGoal.option_no_vs or world.options.versus_inclusion
    starting_sc_round = world.options.starter_pack + 1
    if starting_sc_round > 6 and not include_puzzle and not include_vs:
        starting_sc_round = 1
    return starting_sc_round


def get_starting_puzzle_level(world: "TetrisAttackWorld") -> int:
    include_stage_clear = world.options.stage_clear_goal or world.options.stage_clear_inclusion
    include_vs = world.options.versus_goal != VersusGoal.option_no_vs or world.options.versus_inclusion
    starting_puzzle_level = world.options.starter_pack + 1 - StarterPack.option_puzzle_level_1
    if starting_puzzle_level < 1 and not include_stage_clear and not include_vs:
        starting_puzzle_level = 1
    if starting_puzzle_level > 0 and not normal_puzzle_set_included(world):
        starting_puzzle_level += 6
    return starting_puzzle_level

def get_starting_vs_flag(world: "TetrisAttackWorld") -> bool:
    include_stage_clear = world.options.stage_clear_goal or world.options.stage_clear_inclusion
    include_puzzle = world.options.puzzle_goal != PuzzleGoal.option_no_puzzle or world.options.puzzle_inclusion != PuzzleInclusion.option_no_puzzle
    if not include_stage_clear and not include_puzzle:
        return True
    return world.options.starter_pack == StarterPack.option_vs_two_stages

def normal_puzzle_set_included(world: "TetrisAttackWorld"):
    return (world.options.puzzle_goal == PuzzleGoal.option_puzzle
            or world.options.puzzle_goal == PuzzleGoal.option_puzzle_and_extra_puzzle
            or world.options.puzzle_goal == PuzzleGoal.option_puzzle_or_extra_puzzle
            or world.options.puzzle_inclusion == PuzzleInclusion.option_puzzle
            or world.options.puzzle_inclusion == PuzzleInclusion.option_puzzle_and_extra_puzzle)


def extra_puzzle_set_included(world: "TetrisAttackWorld"):
    return (world.options.puzzle_goal == PuzzleGoal.option_extra_puzzle
            or world.options.puzzle_goal == PuzzleGoal.option_puzzle_and_extra_puzzle
            or world.options.puzzle_goal == PuzzleGoal.option_puzzle_or_extra_puzzle
            or world.options.puzzle_inclusion == PuzzleInclusion.option_extra_puzzle
            or world.options.puzzle_inclusion == PuzzleInclusion.option_puzzle_and_extra_puzzle)
