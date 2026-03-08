import time

from .item import Item

class StatBooster(Item):
    def __init__(self, name, status: str, boost: int,  price):
        super().__init__(name, True, price)
        self.status = status
        self.boost = boost
        self.uses = 1

    def __str__(self, index = None):
        name_width = 20
        value_width = 5
        index_str = f"{index}) " if index is not None else ""
        name_width = name_width - len(index_str)

        boost_str = f"{self.status} +{self.boost}"

        line = (
            f"{index_str}{self.name:<{name_width}} | "
            f"Uses: {self.uses:>{value_width}} | "
            f"{self.status:<8} +{self.boost:<1} | "
        )

        return f"{line}"

    def copy(self):
        """Return a new StatBooster instance with the same stats."""
        return StatBooster(
            name=self.name,
            status=self.status,
            boost=self.boost,
            price=self.price
        )

    def use(self, player_unit, game, in_convoy = False):

        match self.status:
            case "HP":
                player_unit.hp += self.boost
                player_unit.max_hp += self.boost

            case "STR":
                player_unit.strength += self.boost

            case "MAG":
                player_unit.magic += self.boost

            case "SKL":
                player_unit.skill += self.boost

            case "SPD":
                player_unit.speed += self.boost

            case "LUCK":
                player_unit.luck += self.boost

            case "DEF":
                player_unit.defense += self.boost

            case "RES":
                player_unit.resistance += self.boost

            case _:
                print("Invalid stat type.")
                return

        self.uses -= 1
        if self.uses > 0:
            return

        if not in_convoy:
            player_unit.items.remove(self)
        else:
            game.convoy.remove(self)

        print(f"{player_unit.name}'s {self.status} increased by {self.boost}!")
        time.sleep(1)






