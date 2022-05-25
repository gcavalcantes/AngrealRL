from __future__ import annotations
from lib2to3.pytree import Base

from typing import TYPE_CHECKING

from components.base_component import BaseComponent
from equipment_types import EquipamentType

if TYPE_CHECKING:
    from entity import Item

class Equippable(BaseComponent):
    parent: Item

    def __init__(
        self,
        equipment_type: EquipamentType,
        power_bonus: int = 0,
        defense_bonus: int = 0,
    ):
        self.equipment_type = equipment_type

        self.power_bonus = power_bonus
        self.defense_bonus = defense_bonus

class Dagger(Equippable):
    def __init__(self) -> None:
        super().__init__(equipment_type=EquipamentType.WEAPON, power_bonus=2)


class Sword(Equippable):
    def __init__(self) -> None:
        super().__init__(equipment_type=EquipamentType.WEAPON, power_bonus=4)


class LeatherArmor(Equippable):
    def __init__(self) -> None:
        super().__init__(equipment_type=EquipamentType.ARMOR, defense_bonus=1)


class ChainMail(Equippable):
    def __init__(self) -> None:
        super().__init__(equipment_type=EquipamentType.ARMOR, defense_bonus=3)