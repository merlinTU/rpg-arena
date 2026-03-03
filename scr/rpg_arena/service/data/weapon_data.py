from rpg_arena.entity.weapon import Weapon
from rpg_arena.entity.weapon_type import WeaponType
from rpg_arena.entity.unit_class import UnitClass


iron_sword = Weapon(
    name="Iron Sword",
    weapon_type=WeaponType.SWORD,
    strength=8,
    accuracy=100,
    uses=40,
    crit=5,
    weight=5.0,
    price=100
)

iron_axe = Weapon(
    name="Iron Axe",
    weapon_type=WeaponType.AXE,
    strength=12,
    accuracy=85,
    uses=35,
    crit=5,
    weight=7,
    price=120
)

iron_bow = Weapon(
    name="Iron Bow",
    weapon_type=WeaponType.BOW,
    strength=7,
    accuracy=115,
    uses=30,
    crit=5,
    weight=4,
    price=90
)

fire_magic = Weapon(
    name="Fire",
    weapon_type=WeaponType.MAGIC,
    strength=5,
    accuracy=100,
    uses=25,
    crit=5,
    weight=0,
    price=150
)

WEAPONS = {
    "Iron Sword": iron_sword,
    "Iron Axe": iron_axe,
    "Iron Bow": iron_bow,
    "Fire": fire_magic
}

CLASS_WEAPON_MAP = {
    UnitClass.FIGHTER: [WeaponType.SWORD, WeaponType.AXE],
    UnitClass.MERCENARY: [WeaponType.SWORD, WeaponType.AXE],
    UnitClass.MAGE: [WeaponType.MAGIC]
}