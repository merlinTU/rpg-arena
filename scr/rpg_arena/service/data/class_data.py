from dataclasses import dataclass
from rpg_arena.entity.unit_class import UnitClass

@dataclass
class ClassStats:
    base_hp: int
    base_str: int
    base_magic: int
    base_skill: int
    base_speed: int
    base_luck: int
    base_defense: int
    base_res: int

    growth_hp: float
    growth_str: float
    growth_magic: float
    growth_skill: float
    growth_speed: float
    growth_luck: float
    growth_defense: float
    growth_res: float

CLASS_DATA = {
    UnitClass.MERCENARY: ClassStats(
        base_hp=5, base_str=3, base_magic=0,
        base_skill=0, base_speed=0, base_luck=0,
        base_defense=2, base_res=0,

        growth_hp=0.10, growth_str=0.10, growth_magic=0,
        growth_skill=0.10, growth_speed=0.10,
        growth_luck=0.10, growth_defense=0.15, growth_res=0.05
    ),

    UnitClass.MAGE: ClassStats(
        base_hp=0, base_str=0, base_magic=5,
        base_skill=0, base_speed=2, base_luck=0,
        base_defense=0, base_res=5,

        growth_hp=0.0, growth_str=0.0, growth_magic=0.25,
        growth_skill=0.10, growth_speed=0.10,
        growth_luck=0.05, growth_defense=0, growth_res=0.20
    ),

    UnitClass.FIGHTER: ClassStats(
        base_hp=10, base_str=5, base_magic=0,
        base_skill=0, base_speed=0, base_luck=0,
        base_defense=0, base_res=0,

        growth_hp=0.25, growth_str=0.20, growth_magic=0.0,
        growth_skill=0.05, growth_speed=0.1,
        growth_luck=0.10, growth_defense=0.0, growth_res=0.0
    )
}