from .item import Item

class StatBooster(Item):
    def __init__(self, name, status: str, boost: int,  price):
        super().__init__(name, True, price)
        self.status = status
        self.boost = boost
        self.uses = 1

    def __str__(self):
        return f"{self.name} / Uses: {self.uses} / Boosts {self.status} by {self.boost}"