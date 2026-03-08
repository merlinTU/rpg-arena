class ShopActionService:
    def __init__(self, root_service: "RootService"):
        self.root_service = root_service

    def choose_shop_action(self):
        while True:
            choice = input(">> Choose an option (1-3): ")

            if choice == "exit" or choice == "e":
                self.root_service.camp_service.open_camp()

            if not choice.isdigit():
                print("Invalid input. Please enter a number.")
                continue
            choice = int(choice)

            match choice:
                case 1:
                    self.root_service.shop_service.open_buy_items_menu()
                    break
                case 2:
                    self.root_service.shop_service.open_sell_items_menu()
                    break
                case 3:
                    self.root_service.camp_service.open_camp()
                    break
                case _:
                    print("Invalid option. Please choose between 1-4.")

    def make_buy_items_decision(self):
        game = self.root_service.current_game
        player = game.player
        items = self.root_service.shop_service.shop_items

        while True:
            choice = input(">> Command: ").strip().lower()

            parts = choice.split()

            if choice == "exit" or choice == "e":
                self.root_service.shop_service.open_shop()
                break

            if len(parts) != 2:
                print("Invalid command. Use: buy <no> or exit")
                continue

            command, number = parts

            if not number.isdigit():
                print("Invalid item number.")
                continue

            number = int(number)

            if number > len(items):
                print("Invalid item number.")
                continue

            match command:
                case "buy":
                    item = items[number - 1]
                    if item.price > player.gold:
                        print("You do not have enough gold!")
                        continue

                    self.root_service.shop_service.buy_item(item)
                    continue

                case _:
                    print("Unknown command. Use send, take, use or exit.")

    def make_send_to_convoy_decision(self):
        player = self.root_service.current_game.player
        while True:
            choice = input(">> Choose an option: ")

            if not choice.isdigit():
                print("Invalid input. Please enter a number.")
                continue
            choice = int(choice)

            if choice < 0 or choice > len(player.items):
                print("Invalid input.")
                continue

            # send item to convoy
            game = self.root_service.current_game
            game.convoy.append(player.items.pop(choice - 1))

            break

    def make_sell_items_decision(self):
        game = self.root_service.current_game
        player = game.player
        items = self.root_service.shop_service.shop_items

        while True:
            choice = input(">> Command: ").strip().lower()

            parts = choice.split()

            if choice == "exit" or choice == "e":
                self.root_service.shop_service.open_shop()
                break

            if len(parts) != 2:
                print("Invalid command. Use: sell <no> or exit")
                continue

            command, number = parts

            if not number.isdigit():
                print("Invalid item number.")
                continue

            number = int(number)

            if number > len(items):
                print("Invalid item number.")
                continue

            match command:
                case "sell":
                    self.root_service.shop_service.sell_item(number - 1)
                    break

                case _:
                    print("Unknown command. Use sell or exit.")