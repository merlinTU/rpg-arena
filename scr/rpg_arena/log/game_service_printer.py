import time

class GameServicePrinter():
    def __init__(self, root_service: "RootService"):
        self.root_service = root_service

    def print_after_start_game(self, initial_units):
        print("\n======================================")
        print("🔥  Welcome to the Arena!  🔥")
        print("======================================\n")
        time.sleep(1)

        print("The crowd roars as warriors from across the lands gather.")
        print("Only the strongest will survive the trials of the arena.")
        print("Choose your champion wisely!\n")
        time.sleep(2)

        print("\n========================================")
        print("           Choose Your Fighter")
        print("========================================")
        time.sleep(2)
        self.print_initial_units(initial_units)

    def print_after_choose_first_unit(self, player_unit):
        print("You chose: ", player_unit.name, "the ", player_unit.player_class.name)

    def print_after_start_frist_round(self, enemy_units):
        print("========================================")
        print("           THE ARENA AWAITS")
        print("========================================")

        print("Three gladiators stand before you.\n")
        time.sleep(0.5)
        self.print_enemy_units(enemy_units)
        enemy_unit = self.root_service.player_action_service.choose_enemy(enemy_units)
        self.root_service.arena_service.start_arena(enemy_unit)


    def print_enemy_units(self, enemy_units):
        i = 1
        for unit in enemy_units:
            self.print_enemy_stats(unit, i)
            i += 1


    def print_initial_units(self, initial_units):
        i = 0
        for unit in initial_units:
            self.print_unit_stats(unit, i + 1)
            i += 1

    def print_unit_stats(self, unit, number: int):

        name_width = 15
        print(f"{number}) {unit.name:<{name_width}} ({unit.player_class.value})")

        # Stats
        stat_width = 6
        stats_line = (
            "Stats:   "
            f"HP: {unit.hp:>{stat_width}} | "
            f"STR: {unit.strength:>{stat_width}} | "
            f"MAG: {unit.magic:>{stat_width}} | "
            f"SKL: {unit.skill:>{stat_width}} | "
            f"SPD: {unit.speed:>{stat_width}} | "
            f"LUCK: {unit.luck:>{stat_width}} | "
            f"DEF: {unit.defense:>{stat_width}} | "
            f"RES: {unit.res:>{stat_width}}"
        )
        print(stats_line)

        # Growths
        growth_line = (
            "Growths: "
            f"HP: {unit.hp_growth:>{stat_width}.2f} | "
            f"STR: {unit.strength_growth:>{stat_width}.2f} | "
            f"MAG: {unit.magic_growth:>{stat_width}.2f} | "
            f"SKL: {unit.skill_growth:>{stat_width}.2f} | "
            f"SPD: {unit.speed_growth:>{stat_width}.2f} | "
            f"LUCK: {unit.luck_growth:>{stat_width}.2f} | "
            f"DEF: {unit.defense_growth:>{stat_width}.2f} | "
            f"RES: {unit.res_growth:>{stat_width}.2f}"
        )
        print(growth_line)

        # Items
        item_names = [item.name for item in unit.items] if unit.items else []
        items_line = "Items:   " + ", ".join(item_names) if item_names else "Items: None"
        print(items_line)

        time.sleep(1)
        print("========================================")

    def print_enemy_stats(self, unit, number: int):

        name_width = 15
        print(f"{number}) {unit.name:<{name_width}} ({unit.player_class.value})")

        stat_width = 6
        stats_line = (
            f"LVL: {unit.level:>{stat_width}} | "
            f"GOLD: {unit.gold:>{stat_width}}"
        )
        print(stats_line)


        item_names = [item.name for item in unit.items] if unit.items else []
        items_line = "Items:   " + ", ".join(item_names) if item_names else "Items: None"
        print(items_line)

        time.sleep(1)
        print("========================================")

