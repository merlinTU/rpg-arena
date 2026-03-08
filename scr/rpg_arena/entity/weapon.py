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

    def copy(self):
        """Return a new Weapon instance with the same stats."""
        return Weapon(
            name=self.name,
            weapon_type=self.weapon_type,
            strength=self.strength,
            accuracy=self.accuracy,
            uses=self.uses,
            crit=self.crit,
            weight=self.weight,
            price=self.price
        )

    def __str__(self):
        name_width = 20
        stat_width = 6

        return (
            f"{self.name:<{name_width}} | "
            f"STR: {self.strength:>{stat_width}} | "
            f"ACC: {self.accuracy:>{stat_width}} | "
            f"CRIT: {self.crit:>{stat_width}} | "
            f"WEIGHT: {self.weight:>{stat_width}} | "
            f"USES: {self.uses:>{stat_width}}"
        )