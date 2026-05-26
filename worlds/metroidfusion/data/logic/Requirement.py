from typing import TYPE_CHECKING, Self
from abc import ABC, abstractmethod

if TYPE_CHECKING:
    from ... import MetroidFusionOptions


class RequirementBase(ABC):
    """
    Defines a set of requirements for a Connection or Location.

    The parameters are unpacked into a series of logical requirements where all housed in ``items_needed`` and
    one each of entries in each list housed in ``requirements`` must be met for this Requirement to be passed.

    Requirements logic is: (list1 AND list2 AND list3...)
    where (list_requirement1 OR list_requirement2 OR list_requirement3...)

    If there are any ``hard_items_needed``,
    the end possibilities that do not contain all of these items will be removed.

    :param name: A String to label this Requirement. Defaults to the class name.
    :param items_needed: A set of items as Strings. Defaults to an empty set.
    :param hard_items_needed: A set of items as Strings. Defaults to an empty set.
    :param energy_tanks_needed: An integer number of energy tanks required. Defaults to 0.
    :param missile_ammo_needed: An integer number of missiles required. Defaults to 0.
    :param power_bomb_ammo_needed: An integer number of power bombs required. Defaults to 0.
    :param requirements: A list of lists of Requirement objects. Defaults to an empty list.
    """
    name: str
    items_needed: set[str]
    hard_items_needed: set[str]
    energy_tanks_needed: int
    missile_ammo_needed: int
    power_bomb_ammo_needed: int
    requirements: list[list[Self]]

    @abstractmethod
    def __init__(self,
                 name: str = None,
                 items_needed: set[str] = None,
                 hard_items_needed: set[str] = None,
                 energy_tanks_needed: int = 0,
                 missile_ammo_needed: int = 0,
                 power_bomb_ammo_needed: int = 0,
                 *requirements: list[Self],
                 **kwargs):
        if name is None:
            self.name = self.__class__.__name__
        else:
            self.name = name
        if items_needed is None:
            items_needed = set()
        self.items_needed = items_needed
        if hard_items_needed is None:
            hard_items_needed = set()
        self.hard_items_needed = hard_items_needed
        self.requirements = [requirement for requirement in requirements]
        self.energy_tanks_needed = energy_tanks_needed
        self.missile_ammo_needed = missile_ammo_needed
        self.power_bomb_ammo_needed = power_bomb_ammo_needed

    def __repr__(self):
        return_string = f"Name: {self.name}\n"
        return_string += f"ItemsNeeded: [{', '.join(self.items_needed)}]\n"
        return_string += f"HardItemsNeeded: [{', '.join(self.hard_items_needed)}]\n"
        return_string += f"EnergyTanks: {self.energy_tanks_needed}\n"
        return_string += f"MissileAmmo: {self.missile_ammo_needed}\n"
        return_string += f"PowerBombAmmo: {self.power_bomb_ammo_needed}\n"
        return_string += "Requirements: ["
        if self.requirements:
            return_string += f"\n\t[{', '.join(req.name for req_list in self.requirements for req in req_list)}]"
            return_string += "\n]"
        else:
            return_string += "]"
        return return_string

    def __str__(self):
        return self.__repr__()

    @staticmethod
    def check_option_enabled(options: "MetroidFusionOptions") -> bool:
        return True


class Requirement(RequirementBase):
    """
    Defines a single Requirement to be fulfilled that can contain sub-requirements.

    :param name: The name for this Requirement. Defaults to the class name if not already provided.
    :param requirements: Any number of lists of Requirement objects treated as sub-requirements.
        Each list is treated as an OR logic block.
        If there are more than one list, they are treated as list1 AND list2...

    :key items_needed: A set of items that must be in the inventory.
    :key hard_items_needed: A set of items that are absolutely required to fulfill this Requirement.
        Affects final calculation of possibilities to fulfill this Requirement.
    :key energy_tanks_needed: An integer representing the minimum amount of energy tanks to fulfill this Requirement.
    :key missile_ammo_needed: An integer representing the minimum amount of missile ammo to fulfill this Requirement.
        The final calculation will summate this with all sub-requirements.
    :key power_bomb_ammo_needed: An integer representing the minimum amount of power bomb ammo
        to fulfill this Requirement. The final calculation will summate this with all sub-requirements.
    """

    def __init__(self,
                 name = None,
                 *requirements: list[RequirementBase], **kwargs):
        super().__init__(name,
                         kwargs.pop('items_needed', None),
                         kwargs.pop('hard_items_needed', None),
                         kwargs.pop('energy_tanks_needed', 0),
                         kwargs.pop('missile_ammo_needed', 0),
                         kwargs.pop('power_bomb_ammo_needed', 0),
                         *requirements,
                         **kwargs)


class PONRRequirement(Requirement):
    """
    Defines a set of requirements to be used when Point of No Returns are disabled.
    These should always be more minimal than any surrounding requirements.

    :param name: The name for this Requirement. Defaults to "Point of No Return Requirement"
    :param requirements: Any number of lists of Requirement objects treated as sub-requirements.
        Each list is treated as an OR logic block.
        If there are more than one list, they are treated as list1 AND list2...

    :key items_needed: A set of items that must be in the inventory.
        Defaults to ``{"Point of No Return"}`` or adds that element to the passed set.
    :key hard_items_needed: A set of items that are absolutely required to fulfill this Requirement.
        Affects final calculation of possibilities to fulfill this Requirement.
    :key energy_tanks_needed: An integer representing the minimum amount of energy tanks to fulfill this Requirement.
    :key missile_ammo_needed: An integer representing the minimum amount of missile ammo to fulfill this Requirement.
        The final calculation will summate this with all sub-requirements.
    :key power_bomb_ammo_needed: An integer representing the minimum amount of power bomb ammo
        to fulfill this Requirement. The final calculation will summate this with all sub-requirements.
    """

    def __init__(self,
                 name = "Point of No Return Requirement",
                 *requirements: list[RequirementBase],
                 **kwargs):
        items_needed: set[str] = kwargs.pop('items_needed', {"Point of No Return"})
        items_needed.add("Point of No Return")
        kwargs['items_needed'] = items_needed
        super().__init__(name, *requirements, **kwargs)

    @staticmethod
    def check_option_enabled(options: "MetroidFusionOptions") -> bool:
        return options.PointOfNoReturnsInLogic == True
