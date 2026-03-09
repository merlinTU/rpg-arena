import time

class InformationServicePrinter():
    def __init__(self, root_service: "RootService"):
        self.root_service = root_service

    def print_player(self):
        player = self.root_service.current_game.player
        self.root_service.game_service.printer.print_unit_stats(player, 1)

    def print_enemy(self):
        enemy = self.root_service.arena_service.enemy
        self.root_service.game_service.printer.print_unit_stats(enemy, 1)

    def print_weapon_info(self, weapon):
        print(weapon)

    def print_all_stats(self):
        print("\n========================================")
        print("              STAT GUIDE")
        print("========================================")

        stats = ["hp", "str", "mag", "skl", "spd", "luck", "def", "res"]

        for stat in stats:
            self.print_stat(stat)

        print("========================================\n")

    def print_stat(self, stat):
        explanations = {
            "hp": "HP (Health Points): Determines how much damage a unit can take before falling.",
            "str": "STR (Strength): Increases physical attack damage with swords, axes, lances and Bows.",
            "mag": "MAG (Magic): Increases damage dealt with magic.",
            "skl": "SKL (Skill): Improves hit rate and increases critical hit chance.",
            "spd": "SPD (Speed): Improves hit rate and chance to perform a double attack.",
            "luck": "LUCK: Reduces enemy critical chance and slightly improves hit rate.",
            "def": "DEF (Defense): Reduces incoming physical damage.",
            "res": "RES (Resistance): Reduces incoming magic damage."
        }

        stat = stat.lower()

        if stat in explanations:
            print(explanations[stat])
        else:
            print("Unknown stat.")

    def print_all_combat_stats(self):
        print("\n========================================")
        print("            COMBAT GUIDE")
        print("========================================")

        stats = ["hit", "avoid", "acc", "crit", "damage"]

        for stat in stats:
            self.print_combat_stat(stat)

        print("========================================\n")

    def print_combat_stat(self, stat):
        explanations = {
            "hit": (
                "HIT (Hit Rate): Chance that an attack will land.\n"
                "Formula: HIT = Weapon Accuracy + (SKL * 2) + LUCK - Enemy Avoid"
            ),
             "avoid": (
                "AVOID: Chance to dodge an enemy attack.\n"
                "Formula: AVOID = (SPD * 2) + LUCK"
            ),
            "acc": (
                "ACC (Accuracy): Weapon-based accuracy used in hit calculation.\n"
            ),
            "crit": (
                "CRIT (Critical Chance): Chance to deal triple damage.\n"
                "Formula: CRIT = Weapon Crit + (SKL * 0.5)"
            ),
            "damage": (
                "DAMAGE: Amount of HP removed when an attack hits.\n"
                "Physical Formula: DAMAGE = STR + Weapon Might - Enemy DEF\n"
                "Magic Formula: DAMAGE = MAG + Book Might - Enemy RES"
            )
        }

        stat = stat.lower()

        if stat in explanations:
            print(f"\n{explanations[stat]}")
        else:
            print("\nUnknown combat stat.")