import time
class ArneaServicePrinter():
    def __init__(self, root_service: "RootService"):
        self.root_service = root_service

    def print_after_make_attack(self, attacker, defender, has_hit, has_crit, damage, status):
        attacker_name = attacker.name
        defender_name = defender.name

        match status:
            case 1:
                print(attacker_name, "attacks")
            case 2:
                print(attacker_name, "strikes consecutively")
            case 3:
                print(attacker_name, "counters")
        time.sleep(1)

        if has_hit:
            print(defender_name, " takes", damage, " damage")
            if has_crit: print("Critical hit!")
            time.sleep(1)

            print(defender_name, " has ", defender.hp, " HP left")
            time.sleep(3)
        else:
            print(defender_name, " has dodged the attack")

    def print_at_start_round(self, attacker):
        print(attacker.name, "initialise combat")

    def print_after_start_round(self, first_unit, second_unit):
        if first_unit == self.root_service.current_game.player:
            print("Your turn ends. Enemy turn")
        else:
            print("Enemy turn over. Now its your turn")
        time.sleep(3)

    def print_after_arena_simulation(self, winner, loser):
        print("Fight over")
        if winner != self.root_service.current_game.player:
            print("You were defeated")
            print("GAME OVER")
            return

        print(loser.name, "falls to the ground")
        time.sleep(1)
        print(loser.name, "is defeated")
        time.sleep(3)
        print("You win!")