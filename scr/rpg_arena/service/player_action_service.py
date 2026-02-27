class PlayerActionService:
    def __init__(self, root_service: "RootService"):
        self.root_service = root_service

    def choose_unit(self, initial_units):
        while True:
            choice = input("Write your Fighter's name or number: ")

            if choice.isdigit():
                index = int(choice)

                if 0 <= index < len(initial_units):
                    player_unit = initial_units[index-1]
                    return player_unit
                else:
                    print("Invalid number. Try again.")

            else:
                index = self.search_unit_index(initial_units, choice)

                if index != -1:
                    player_unit = initial_units[index]
                    return player_unit
                else:
                    print("Name not found. Try again.")

    def search_unit_index(self, initial_units, choice: str):
            for i in range(0,len(initial_units)):
                if initial_units[i].name == choice: return i
            return -1