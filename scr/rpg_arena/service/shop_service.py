import time

from rpg_arena.entity.healing_potion import HealingPotion
from rpg_arena.entity.stat_booster import StatBooster
from rpg_arena.log.shop_service_printer import ShopServicePrinter
from rpg_arena.service.shop_action_service import ShopActionService

from rpg_arena.service.data.item_data import ITEMS
from rpg_arena.service.data.weapon_data import WEAPONS


class ShopService:
    def __init__(self, root_service: "RootService"):
        self.root_service = root_service
        self.printer = ShopServicePrinter(root_service)
        self.action_service = ShopActionService(root_service)

        self.shop_items = []

    def open_shop(self):
        player_weapons = self.root_service.current_game.player_weapons
        self.generate_shop_weapons(player_weapons)
        self.generate_shop_items()

        self.printer.print_at_open_shop()
        self.action_service.choose_shop_action()

    def open_buy_items_menu(self):
        self.printer.print_at_open_buy_items_menu(items=self.shop_items)
        self.action_service.make_buy_items_decision()

    def open_sell_items_menu(self):
        player = self.root_service.current_game.player
        convoy = self.root_service.current_game.convoy

        if not player.items and not convoy.items:
            print("You have no items to sell.")
            self.open_shop()
            return

        self.printer.print_at_open_sell_items_menu()
        self.action_service.make_sell_items_decision()

    def generate_shop_weapons(self, player_weapons):

        shop_weapons = [
            w for w in WEAPONS.values() if w.weapon_type in player_weapons
        ]

        for w in shop_weapons:
            self.shop_items.append(w.copy())

    def generate_shop_items(self):
        # add healing items first
        for item in ITEMS.values():
            if isinstance(item, HealingPotion):
                self.shop_items.append(item.copy())

        for item in ITEMS.values():
            if isinstance(item, StatBooster):
                self.shop_items.append(item.copy())

    def buy_item(self, item):
        game = self.root_service.current_game
        player = game.player

        player.gold -= item.price

        print(player.name, "bought ", item.name)
        print("You habe", player.gold, "gold left")

        # send item to inventory
        player.items.append(item.copy())

        if len(player.items) > game.max_items:
            self.printer.print_at_full_inventory()
            self.action_service.make_send_to_convoy_decision()

        self.printer.print_buy_items_decision()

    def sell_item(self, number):
        game = self.root_service.current_game
        player = game.player

        if number > len(player.items):
            number -= len(player.items)
            item = game.convoy.pop(number)
        else:
            item = player.items.pop(number)

        player.gold += item.price

        print(player.name, "sold", item.name, f"and gained {item.price}.")
        print("You have", player.gold, "gold now.")

        self.open_sell_items_menu()


