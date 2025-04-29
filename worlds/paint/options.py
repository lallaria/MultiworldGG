from dataclasses import dataclass

from Options import Range, PerGameCommonOptions, Toggle, Choice


class LogicPercent(Range):
    """Sets the maximum percent similarity required for a check to be in logic.
    Higher values are more difficult and items/locations will not be generated beyond this number."""
    display_name = "Logic Percent"
    range_start = 50
    range_end = 95
    default = 80


class GoalPercent(Range):
    """Sets the percent similarity required to achieve your goal.
    If this number is higher than the value for logic percent,
    reaching goal will be in logic upon obtaining all progression items."""
    display_name = "Goal Percent"
    range_start = 50
    range_end = 95
    default = 80


class GoalImage(Range):
    """Sets the numbered image you will be required to match.
    See https://github.com/MarioManTAW/jspaint/tree/master/images/archipelago
    for a list of possible images or choose random.
    This can also be overwritten client-side by using File->Open."""
    display_name = "Goal Image"
    range_start = 1
    range_end = 1
    default = "random"

class StartingTool(Choice):
    """Sets which tool (other than Magnifier) you will be able to use from the start."""
    option_brush = 0
    option_pencil = 1
    option_eraser = 2
    option_airbrush = 3
    option_line = 4
    option_rectangle = 5
    option_ellipse = 6
    option_rounded_rectangle = 7
    default = 0

class TrapCount(Range):
    """Sets the number of filler items to be replaced by random traps."""
    display_name = "Trap Count"
    range_start = 0
    range_end = 50
    default = 0

class DeathLink(Toggle):
    """If on, using the Undo or Clear Image functions will send a death to all other players with death link on.
    Receiving a death will clear the image and reset the history.
    This option also prevents Undo and Clear Image traps from being generated in the item pool."""
    display_name = "Death Link"

@dataclass
class PaintOptions(PerGameCommonOptions):
    logic_percent: LogicPercent
    goal_percent: GoalPercent
    goal_image: GoalImage
    starting_tool: StartingTool
    trap_count: TrapCount
    death_link: DeathLink
