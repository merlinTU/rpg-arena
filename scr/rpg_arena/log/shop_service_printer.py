from rpg_arena.entity.healing_potion import HealingPotion
from rpg_arena.entity.stat_booster import StatBooster
import time


class ShopServicePrinter:
    def __init__(self, root_service: "RootService"):
        self.root_service = root_service

    def print_at_open_shop(self):
        print("========================================")
        print("           Merchant")
        print("========================================")
        print("What do you want to do?")
        print("1) Buy Items")
        print("2) Sell Items")
        print("3) Exit")
        print("========================================\n")

    def print_at_open_buy_items_menu(self, items):
        first_heal = True
        first_booster = True

        print("\n--- Weapons ---")
        time.sleep(1)
        for i, item in enumerate(items, start=1):
            if first_heal and isinstance(item, HealingPotion):
                print("\n--- Healing Potions ---")
                first_heal = False
                time.sleep(1)

            if first_booster and isinstance(item, StatBooster):
                print("\n--- Stat Boosters ---")
                first_booster = False
                time.sleep(1)

            print(item.__str__(i), f"Price: {item.price:>{6}}")


        self.print_buy_items_decision()


    def print_at_open_sell_items_menu(self):
        player = self.root_service.current_game.player
        convoy = self.root_service.current_game.convoy

        print("--- Inventory ---")

        index = 1
        if player.items:
            for item in player.items:
                print(item.__str__(index), f"Price: {item.price:>{6}}")
                index += 1
        else:
            print("No weapons in inventory.")

        # --- Convoy Weapons ---
        print("\n--- Convoy Storage ---")
        time.sleep(1)

        if convoy:
            for item in convoy:
                print(item.__str__(index), f"Price: {item.price:>{6}}")
        else:
            print("Convoy is empty.")

        self.print_sell_items_decision()

    def print_buy_items_decision(self):
        print("========================================")
        print("What do you want to do?")
        print("buy <no>    - Buy item")
        print("exit        - Leave shop")
        print("========================================\n")

    def print_sell_items_decision(self):
        print("========================================")
        print("What do you want to do?")
        print("sell <no>   - sell item")
        print("exit        - Leave shop")
        print("========================================\n")


    def print_at_full_inventory(self):
        player = self.root_service.current_game.player
        print("Your inventory is full!")
        time.sleep(1)
        print("--- Inventory ---")

        for index, weapon in enumerate(player.items, start=1):
            print(f"{index}) {weapon}")

        print("========================================")
        print("Write the number o the item you want to send to the convoy")
        print("========================================\n")

    def print_buy_items_decision(self):
        print("========================================")
        print("What do you want to do?")
        print("buy <no>    - Buy item")
        print("exit        - Leave shop")
        print("========================================\n")