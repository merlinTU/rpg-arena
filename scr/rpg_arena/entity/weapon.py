from .weapon_type import WeaponType
from .item import Item

class Weapon(Item):
    def __init__(self, name, weapon_type: WeaponType, strength: int, accuracy:int,
                 uses: int, crit: int, weight: int, price: int):
        super().__init__(name, False, price)
        self.weapon_type = weapon_type
        self.strength = strength
        self.accuracy = accuracy
        self.uses = uses
        self.crit = crit
        self.weight = weight

    def __str__(self):
        return (f"{self.name} ({self.weapon_type.name}) / "
                f"STR: {self.strength} / ACC: {self.accuracy} / "
                f"CRIT: {self.crit} / WEIGHT: {self.weight} / "
                f"USES: {self.uses}")