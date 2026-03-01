from .item import Item

class HealingPotion(Item):
    def __init__(self, name, heal_amount, uses, price):
        super().__init__(name, True, price)
        self.heal_amount = heal_amount
        self.uses = uses