import dataclasses
from typing import override, Any, TYPE_CHECKING

from BaseClasses import CollectionState
from NetUtils import JSONMessagePart
from Options import DeathLink
from rule_builder.field_resolvers import FieldResolver, FromWorldAttr
from rule_builder.options import OptionFilter
from rule_builder.rules import Has, CanReachRegion, Filtered, Rule
from .Options import IncludePurpleSO, IncludeSocks, IncludeSkills, IncludeLevelItems
from .constants import ConnectionNames, ItemNames, LocationNames, RegionNames, game_name

if TYPE_CHECKING:
    from . import BattleForBikiniBottom

so_values = {
    ItemNames.so_100: 0,
    ItemNames.so_250: 0,
    ItemNames.so_500: 500,
    ItemNames.so_750: 750,
    ItemNames.so_1000: 1000,
}


@dataclasses.dataclass()
class HasSOAmount(Rule["BattleForBikiniBottom"], game=game_name):
    amount: float = 1

    @override
    def _instantiate(self, world: "BattleForBikiniBottom") -> Rule.Resolved:
        return self.Resolved(
            self.amount,
            player=world.player,
            caching_enabled=getattr(world, "rule_caching_enabled", False),
        )

    class Resolved(Rule.Resolved):
        amount: float = 0

        @override
        def _evaluate(self, state: CollectionState) -> bool:
            return sum(
                state.count(item_name, self.player) * amount for item_name, amount in so_values.items()) >= self.amount

        @override
        def item_dependencies(self) -> dict[str, set[int]]:
            return {
                ItemNames.so: {id(self)}}

        @override
        def explain_json(self, state: CollectionState | None = None) -> list[JSONMessagePart]:
            verb = "Missing " if state and not self(state) else "Has "
            messages: list[JSONMessagePart] = [{
                "type": "text",
                "text": verb}]
            messages.append({
                "type": "color",
                "color": "cyan",
                "text": str(self.amount)})
            messages.append({
                "type": "text",
                "text": "x "})
            if state:
                color = "green" if self(state) else "salmon"
                messages.append({
                    "type": "color",
                    "color": color,
                    "text": ItemNames.so})
            else:
                messages.append({
                    "type": "item_name",
                    "flags": 0b001,
                    "text": ItemNames.so,
                    "player": self.player})
            return messages

        @override
        def explain_str(self, state: CollectionState | None = None) -> str:
            if state is None:
                return str(self)
            prefix = "Has" if self(state) else "Missing"
            count = f"{self.amount}x "
            return f"{prefix} {count}{ItemNames.so}"

        @override
        def __str__(self) -> str:
            count = f"{self.amount}x "
            return f"Has {count}{ItemNames.so}"


can_farm_so = Filtered(
    (CanReachRegion(RegionNames.gl01) & Has(ItemNames.cruise_bubble))
    | CanReachRegion(RegionNames.db02),
    options=[OptionFilter(DeathLink, DeathLink.option_false)]
)
only_when_socks_included = {
    "options": [OptionFilter(IncludeSocks, IncludeSocks.option_true)],
    "filtered_resolution": True}
only_when_purple_so_included = {
    "options": [OptionFilter(IncludePurpleSO, IncludePurpleSO.option_true)],
    "filtered_resolution": True}
only_when_purple_so_excluded = {
    "options": [OptionFilter(IncludePurpleSO, IncludePurpleSO.option_false)],
    "filtered_resolution": True}
only_when_skills_included = {
    "options": [OptionFilter(IncludeSkills, IncludeSkills.option_true)],
    "filtered_resolution": True}
only_when_skills_excluded = {
    "options": [OptionFilter(IncludeSkills, IncludeSkills.option_false)],
    "filtered_resolution": True}

only_when_level_items_included = {
    "options": [OptionFilter(IncludeLevelItems, IncludeLevelItems.option_true)],
    "filtered_resolution": True}
only_when_level_items_excluded = {
    "options": [OptionFilter(IncludeLevelItems, IncludeLevelItems.option_false)],
    "filtered_resolution": True}


def sock_only_rule(rule: Rule) -> Rule:
    return Filtered(rule, **only_when_socks_included)


def purple_so_only_rule(rule: Rule) -> Rule:
    return Filtered(rule, **only_when_purple_so_included)


def purple_so_excluded_rule(rule: Rule) -> Rule:
    return Filtered(rule, **only_when_purple_so_excluded)


def skills_only_rule(rule: Rule) -> Rule:
    return Filtered(rule, **only_when_skills_included)


def skills_excluded_rule(rule: Rule) -> Rule:
    return Filtered(rule, **only_when_skills_excluded)


def level_item_only_rule(rule: Rule) -> Rule:
    return Filtered(rule, **only_when_level_items_included)


def level_item_excluded_rule(rule: Rule) -> Rule:
    return Filtered(rule, **only_when_level_items_excluded)


@dataclasses.dataclass(frozen=True)
class RequiredSpatLimitedResolver(FieldResolver, game=game_name):
    value: int

    @override
    def resolve(self, world: "BattleForBikiniBottom") -> Any:
        return min(self.value, world.options.required_spatulas.value)


logic = [
    # connections
    {
        ConnectionNames.pineapple_hub1: Has(ItemNames.spat, count=1),
        ConnectionNames.hub1_bb01: Has(ItemNames.spat, count=FromWorldAttr(f"gate_costs.{ConnectionNames.hub1_bb01}")),
        ConnectionNames.hub1_gl01: Has(ItemNames.spat, count=FromWorldAttr(f"gate_costs.{ConnectionNames.hub1_gl01}")),
        ConnectionNames.hub1_b1: Has(ItemNames.spat, count=FromWorldAttr(f"gate_costs.{ConnectionNames.hub1_b1}")),
        ConnectionNames.hub2_rb01: Has(ItemNames.spat, count=FromWorldAttr(f"gate_costs.{ConnectionNames.hub2_rb01}")),
        ConnectionNames.hub2_sm01: Has(ItemNames.spat, count=FromWorldAttr(f"gate_costs.{ConnectionNames.hub2_sm01}")),
        ConnectionNames.hub2_b2: Has(ItemNames.spat, count=FromWorldAttr(f"gate_costs.{ConnectionNames.hub2_b2}")) &
                                 skills_only_rule(Has(ItemNames.bubble_bowl) | Has(ItemNames.cruise_bubble)),
        ConnectionNames.hub3_kf01: Has(ItemNames.spat, count=FromWorldAttr(f"gate_costs.{ConnectionNames.hub3_kf01}")),
        ConnectionNames.hub3_gy01: Has(ItemNames.spat, count=FromWorldAttr(f"gate_costs.{ConnectionNames.hub3_gy01}")),
        ConnectionNames.cb_b3: Has(ItemNames.spat, count=FromWorldAttr(f"gate_costs.{ConnectionNames.cb_b3}")) &
                               skills_only_rule(Has(ItemNames.cruise_bubble)),
        ConnectionNames.bc01_bc02: skills_only_rule(Has(ItemNames.bubble_bowl)),
        ConnectionNames.bc02_bc03: skills_only_rule(Has(ItemNames.bubble_bowl)),
        ConnectionNames.bc02_bc05: skills_only_rule(Has(ItemNames.bubble_bowl)) &
                                   level_item_only_rule(Has(ItemNames.lvl_itm_bc, count=4)),
        ConnectionNames.kf04_kf05: skills_only_rule(Has(ItemNames.cruise_bubble)),
        ConnectionNames.kf04_kf02: skills_only_rule(Has(ItemNames.cruise_bubble)),
        ConnectionNames.kf01_kf05: skills_only_rule(Has(ItemNames.cruise_bubble)),

        ConnectionNames.gy03_gy04: level_item_only_rule(Has(ItemNames.lvl_itm_gy, count=4)),
    },
    # locations
    {
        ItemNames.spat: {
            LocationNames.spat_ks_01: (
                    Has(ItemNames.spat, count=RequiredSpatLimitedResolver(5), **only_when_purple_so_excluded) &
                    Filtered(can_farm_so | HasSOAmount(amount=3000 / 2), **only_when_purple_so_included)
            ),
            LocationNames.spat_ks_02: (
                    Has(ItemNames.spat, count=RequiredSpatLimitedResolver(10), **only_when_purple_so_excluded) &
                    Filtered(can_farm_so | HasSOAmount(amount=6500 / 2), **only_when_purple_so_included)
            ),
            LocationNames.spat_ks_03: (
                    Has(ItemNames.spat, count=RequiredSpatLimitedResolver(15), **only_when_purple_so_excluded) &
                    Filtered(can_farm_so | HasSOAmount(amount=10500 / 2), **only_when_purple_so_included)
            ),
            LocationNames.spat_ks_04: (
                    Has(ItemNames.spat, count=RequiredSpatLimitedResolver(20), **only_when_purple_so_excluded) &
                    Filtered(can_farm_so | HasSOAmount(amount=15000 / 2), **only_when_purple_so_included)
            ),
            LocationNames.spat_ks_05: (
                    Has(ItemNames.spat, count=RequiredSpatLimitedResolver(25), **only_when_purple_so_excluded) &
                    Filtered(can_farm_so | HasSOAmount(amount=20000 / 2), **only_when_purple_so_included)
            ),
            LocationNames.spat_ks_06: (
                    Has(ItemNames.spat, count=RequiredSpatLimitedResolver(30), **only_when_purple_so_excluded) &
                    Filtered(can_farm_so | HasSOAmount(amount=25500 / 2), **only_when_purple_so_included)
            ),
            LocationNames.spat_ks_07: (
                    Has(ItemNames.spat, count=RequiredSpatLimitedResolver(35), **only_when_purple_so_excluded) &
                    Filtered(can_farm_so | HasSOAmount(amount=32000 / 2), **only_when_purple_so_included)
            ),
            LocationNames.spat_ks_08: (
                    Has(ItemNames.spat, count=RequiredSpatLimitedResolver(40), **only_when_purple_so_excluded) &
                    Filtered(can_farm_so | HasSOAmount(amount=39500 / 2), **only_when_purple_so_included)
            ),
            LocationNames.spat_ps_01: Has(ItemNames.sock, count=10),
            LocationNames.spat_ps_02: Has(ItemNames.sock, count=20),
            LocationNames.spat_ps_03: Has(ItemNames.sock, count=30),
            LocationNames.spat_ps_04: Has(ItemNames.sock, count=40),
            LocationNames.spat_ps_05: Has(ItemNames.sock, count=50),
            LocationNames.spat_ps_06: Has(ItemNames.sock, count=60),
            LocationNames.spat_ps_07: Has(ItemNames.sock, count=70),
            LocationNames.spat_ps_08: Has(ItemNames.sock, count=80),

            LocationNames.spat_hb_02: skills_only_rule(Has(ItemNames.bubble_bowl) | Has(ItemNames.cruise_bubble)),
            LocationNames.spat_hb_03: skills_only_rule(Has(ItemNames.cruise_bubble)),
            LocationNames.spat_bb_08: skills_only_rule(Has(ItemNames.cruise_bubble)),
            LocationNames.spat_bc_01: skills_only_rule(Has(ItemNames.bubble_bowl)),
            LocationNames.spat_kf_02: level_item_excluded_rule(
                skills_only_rule(Has(ItemNames.cruise_bubble))) & level_item_only_rule(
                Has(ItemNames.lvl_itm_kf1, count=6)),
            LocationNames.spat_kf_05: skills_only_rule(Has(ItemNames.cruise_bubble)),
            LocationNames.spat_kf_06: skills_only_rule(Has(ItemNames.cruise_bubble)) & level_item_only_rule(
                Has(ItemNames.lvl_itm_kf2, count=6)),
            LocationNames.spat_gy_02: skills_only_rule(Has(ItemNames.cruise_bubble)),
            LocationNames.spat_gy_03: skills_only_rule(Has(ItemNames.cruise_bubble)),
            LocationNames.spat_db_02: skills_only_rule(Has(ItemNames.bubble_bowl)),
            LocationNames.spat_b3_02: skills_only_rule(Has(ItemNames.bubble_bowl) & Has(ItemNames.cruise_bubble)),

            LocationNames.spat_jf_08: level_item_only_rule(Has(ItemNames.lvl_itm_jf)),
            LocationNames.spat_bb_01: level_item_only_rule(Has(ItemNames.lvl_itm_bb, count=11)),
            LocationNames.spat_gl_03: level_item_only_rule(Has(ItemNames.lvl_itm_gl, count=5)),
            LocationNames.spat_rb_03: level_item_only_rule(Has(ItemNames.lvl_itm_rb, count=6)),
            LocationNames.spat_bc_03: level_item_only_rule(Has(ItemNames.lvl_itm_bc, count=4)),
            LocationNames.spat_gy_06: level_item_only_rule(Has(ItemNames.lvl_itm_gy, count=4)),
            LocationNames.spat_gy_07: level_item_only_rule(Has(ItemNames.lvl_itm_gy, count=4)),
        },
        ItemNames.sock: {
            LocationNames.sock_jf01_06: skills_only_rule(Has(ItemNames.bubble_bowl) | Has(ItemNames.cruise_bubble)),
            LocationNames.sock_jf03_02: skills_only_rule(Has(ItemNames.cruise_bubble)),
            LocationNames.sock_bb04_01: skills_only_rule(Has(ItemNames.cruise_bubble)),
            LocationNames.sock_bc01_01: skills_only_rule(Has(ItemNames.bubble_bowl)),
            LocationNames.sock_kf01_03: skills_only_rule(Has(ItemNames.bubble_bowl)),
            LocationNames.sock_kf04_01: skills_only_rule(Has(ItemNames.cruise_bubble)),

            LocationNames.sock_sm03_01: level_item_only_rule(Has(ItemNames.lvl_itm_sm, count=8)),
        },

        ItemNames.golden_underwear: {
            LocationNames.golden_under_02: skills_only_rule(Has(ItemNames.bubble_bowl) | Has(ItemNames.cruise_bubble)),
            LocationNames.golden_under_03: skills_only_rule(Has(ItemNames.cruise_bubble)),
        },

        ItemNames.lvl_itm: {
            LocationNames.lvl_itm_kf1_01: skills_only_rule(Has(ItemNames.cruise_bubble)),
            LocationNames.lvl_itm_kf1_02: skills_only_rule(Has(ItemNames.cruise_bubble)),
            LocationNames.lvl_itm_kf1_03: skills_only_rule(Has(ItemNames.cruise_bubble)),
            LocationNames.lvl_itm_kf1_06: skills_only_rule(Has(ItemNames.cruise_bubble)),
            LocationNames.lvl_itm_kf2_01: skills_only_rule(Has(ItemNames.cruise_bubble)),
            LocationNames.lvl_itm_kf2_02: skills_only_rule(Has(ItemNames.cruise_bubble)),
            LocationNames.lvl_itm_kf2_03: skills_only_rule(Has(ItemNames.cruise_bubble)),
            LocationNames.lvl_itm_kf2_04: skills_only_rule(Has(ItemNames.cruise_bubble)),
            LocationNames.lvl_itm_kf2_05: skills_only_rule(Has(ItemNames.cruise_bubble)),
            LocationNames.lvl_itm_kf2_06: skills_only_rule(Has(ItemNames.cruise_bubble)),
        },
        ItemNames.so_purple: {
            LocationNames.purple_so_bb04_01: skills_only_rule(Has(ItemNames.cruise_bubble)),
            LocationNames.purple_so_bc01_01: skills_only_rule(Has(ItemNames.bubble_bowl) | Has(ItemNames.cruise_bubble)),
            LocationNames.purple_so_bc02_01: skills_only_rule(Has(ItemNames.bubble_bowl)),
            LocationNames.purple_so_bc02_02: skills_only_rule(Has(ItemNames.bubble_bowl)),
            LocationNames.purple_so_kf01_01: skills_only_rule(Has(ItemNames.cruise_bubble)),
            LocationNames.purple_so_kf04_01: skills_only_rule(Has(ItemNames.cruise_bubble)),

            LocationNames.purple_so_gy03_01: level_item_only_rule(Has(ItemNames.lvl_itm_gy, count=4)),
        }
    }
]