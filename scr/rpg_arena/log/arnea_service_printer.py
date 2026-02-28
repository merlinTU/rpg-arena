
class ArneaServicePrinter():
    def __init__(self, root_service: "RootService"):
        self.root_service = root_service

    def print_after_make_attack(self, attacker, defender, has_hit, has_crit, damage):
        attacker_name = attacker.name
        defender_name = defender.name
        print(attacker_name, " attacks")

        if has_hit:
            print(defender_name, " takes", damage, " damage")
            if has_crit: print("Critical hit!")
            print(defender_name, " has ", defender.hp, " left")

    def print_after_arena_simulation(self):
        print("Fight over")