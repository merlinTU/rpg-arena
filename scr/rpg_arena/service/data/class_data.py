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
        base_skill=0, base_speed=3, base_luck=2,
        base_defense=2, base_res=0,

        growth_hp=0.10, growth_str=0.10, growth_magic=0,
        growth_skill=0.10, growth_speed=0.10,
        growth_luck=0.10, growth_defense=0.15, growth_res=0.05
    ),

    UnitClass.MAGE: ClassStats(
        base_hp=0, base_str=0, base_magic=5,
        base_skill=0, base_speed=2, base_luck=3,
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
    ),

    UnitClass.KNIGHT: ClassStats(
            base_hp=5, base_str=0, base_magic=0,
            base_skill=0, base_speed=0, base_luck=0,
            base_defense=10, base_res=0,

            growth_hp=0.25, growth_str=0.25, growth_magic=0,
            growth_skill=0.0, growth_speed=0.20,
            growth_luck=0.0, growth_defense=0.25, growth_res=0.0
        ),

    UnitClass.SWORDMASTER: ClassStats(
        base_hp=0, base_str=5, base_magic=0,
        base_skill=5, base_speed=10, base_luck=0,
        base_defense=0, base_res=0,

        growth_hp=0.0, growth_str=0.0, growth_magic=0,
        growth_skill=0.0, growth_speed=0.25,
        growth_luck=0.15, growth_defense=0.0, growth_res=0.0
    ),

    UnitClass.BERSERKER: ClassStats(
            base_hp=10, base_str=5, base_magic=0,
            base_skill=0, base_speed=0, base_luck=5,
            base_defense=0, base_res=0,

            growth_hp=0.20, growth_str=0.20, growth_magic=0,
            growth_skill=0.0, growth_speed=0.0,
            growth_luck=0.0, growth_defense=0.0, growth_res=0.0
        ),

    UnitClass.THIEF: ClassStats(
            base_hp=0, base_str=2, base_magic=0,
            base_skill=3, base_speed=8, base_luck=2,
            base_defense=0, base_res=0,

            growth_hp=0.0, growth_str=0.0, growth_magic=0.10,
            growth_skill=0.15, growth_speed=0.20,
            growth_luck=0.25, growth_defense=0.0, growth_res=0.0
        ),

    UnitClass.SOLIDER: ClassStats(
            base_hp=0, base_str=3, base_magic=0,
            base_skill=10, base_speed=3, base_luck=2,
            base_defense=2, base_res=0,

            growth_hp=0.10, growth_str=0.10, growth_magic=0.0,
            growth_skill=0.15, growth_speed=0.15,
            growth_luck=0.10, growth_defense=0.10, growth_res=0.0
        ),

    UnitClass.ARCHER: ClassStats(
            base_hp=0, base_str=3, base_magic=0,
            base_skill=7, base_speed=2, base_luck=5,
            base_defense=3, base_res=0,

            growth_hp=0.0, growth_str=0.15, growth_magic=0.0,
            growth_skill=0.20, growth_speed=0.15,
            growth_luck=0.10, growth_defense=0.10, growth_res=0.0
        ),

    UnitClass.PALADIN: ClassStats(
            base_hp=5, base_str=5, base_magic=0,
            base_skill=0, base_speed=5, base_luck=0,
            base_defense=0, base_res=5,

            growth_hp=0.0, growth_str=0.10, growth_magic=0.0,
            growth_skill=0.10, growth_speed=0.10,
            growth_luck=0.0, growth_defense=0.0, growth_res=0.10
        )
}