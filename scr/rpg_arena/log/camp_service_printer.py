import time

class CampServicePrinter:
    def __init__(self, root_service: "RootService"):
        self.root_service = root_service


    def print_at_open_menu(self):
        print("\n======================================")
        print("You return to the camp after the battle.")
        print("\nWhat will you do?")
        print("1) Enter the arena")
        print("2) Manage equipment")
        print("3) Visit the merchant")
        print("4) Exit game")
        print("======================================\n")

    def print_at_open_item_manager(self):
        player = self.root_service.current_game.player
        convoy = self.root_service.current_game.convoy

        print("\n========================================")
        print("            ITEM MANAGEMENT")
        print("========================================")
        time.sleep(1)

        # --- Player Weapons ---
        print("\n--- Equipped / Inventory ---")
        time.sleep(1)

        if player.weapons:
            for index, weapon in enumerate(player.weapons, start=1):
                print(f"{index}) {weapon}")
        else:
            print("No weapons in inventory.")

        # --- Convoy Weapons ---
        print("\n--- Convoy Storage ---")
        time.sleep(1)

        if convoy:
            for index, weapon in enumerate(convoy, start=1):
                print(f"{index}) {weapon}")
        else:
            print("Convoy is empty.")

        print("\n----------------------------------------")
        print("What would you like to do?")
        print("1) Send item to convoy")
        print("2) Discard item")
        print("3) Leave item manager")
        print("========================================\n")
