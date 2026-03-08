import time

from rpg_arena.entity import Weapon


class ArneaServicePrinter():
    def __init__(self, root_service: "RootService"):
        self.root_service = root_service

    def print_after_make_attack(self, attacker, defender, has_hit, has_crit, damage, status):
        attacker_name = attacker.name
        defender_name = defender.name

        # Action Line
        match status:
            case 1:
                print(f"> {attacker_name} attacks!")
            case 2:
                print(f"> {attacker_name} strikes consecutively! (x2)")
            case 3:
                print(f"> {attacker_name} counters!")

        time.sleep(1)

        # Result
        if has_hit:
            if has_crit:
                print(">>> CRITICAL HIT! <<<")
                time.sleep(1)

            print(f"> {defender_name} takes {damage} damage.")
            time.sleep(1)

            print(f"> {defender_name} HP: {defender.hp}")
            time.sleep(3)
        else:
            print(f"> {defender_name} dodged the attack!")
            time.sleep(2)


    def print_at_start_round(self):
        print("\n========================================")
        print("        BATTLE START")
        print("========================================")
        time.sleep(1)


    def print_after_start_round(self, first_unit, second_unit):
        print("\n========================================")

        if first_unit == self.root_service.current_game.player:
            print("        YOUR TURN")
        else:
            print("        ENEMY TURN")

        print("========================================")

    def print_after_arena_simulation(self, winner, loser):
        print("\n================ FIGHT OVER ================\n")
        time.sleep(1)

        if winner != self.root_service.current_game.player:
            print("You have been defeated!")
            time.sleep(1)
            print("GAME OVER")
            return

        print(f"{loser.name} falls to the ground...")
        time.sleep(1)
        print(f"{loser.name} is defeated!")
        time.sleep(2)
        print("\n================ YOU WIN! =================\n")
        time.sleep(2)

    def print_at_open_fight_menu(self):
        """
        Prints all weapons in the player's items in a formatted, numbered box
        so the player can choose which weapon to use.
        """
        items = self.root_service.current_game.player.items
        weapons = [item for item in items if isinstance(item, Weapon)]

        print("\n========================================")
        print("           CHOOSE YOUR WEAPON")
        print("========================================")

        if not weapons:
            print("You have no weapons available!")
            print("========================================")
            return

        # Print numbered list of weapons
        for index, weapon in enumerate(weapons, start=1):
            print(f"{index}) {weapon}")

        print("========================================")

    def print_fight_preview(self):
        player_unit = self.root_service.current_game.player
        enemy_unit = self.root_service.arena_service.enemy
        arena = self.root_service.arena_service

        player_hit = arena.caluclate_hit_chance(player_unit, enemy_unit)
        player_crit = arena.caluclate_crit_chance(player_unit, enemy_unit)
        player_damage = arena.calculate_damage(player_unit, enemy_unit)

        enemy_hit = arena.caluclate_hit_chance(enemy_unit, player_unit)
        enemy_crit = arena.caluclate_crit_chance(enemy_unit, player_unit)
        enemy_damage = arena.calculate_damage(enemy_unit, player_unit)

        player_double = player_unit.speed > enemy_unit.speed + 5
        enemy_double = enemy_unit.speed > player_unit.speed + 5

        player_weapon_arrow = ""
        enemy_weapon_arrow = ""
        vantage_player = arena.check_weapon_vantage(player_unit.equipped_weapon, enemy_unit.equipped_weapon)
        if vantage_player == 1:
            player_weapon_arrow = " ↑"
        elif vantage_player == 2:
            player_weapon_arrow = " ↓"

        vantage_enemy = arena.check_weapon_vantage(enemy_unit.equipped_weapon, player_unit.equipped_weapon)
        if vantage_enemy == 1:
            enemy_weapon_arrow = " ↑"
        elif vantage_enemy == 2:
            enemy_weapon_arrow = " ↓"

        print("\n========================================")
        print("           FIGHT PREVIEW")
        print("========================================")

        name_width = 15
        hp_width = 5
        stat_width = 6
        weapon_width = 15

        # Player
        player_weapon_str = f"{player_unit.equipped_weapon.name:<{weapon_width - 1}}{player_weapon_arrow:>1}"
        player_info = (
            f"1) {player_unit.name:<{name_width}} | "
            f"{player_weapon_str} | "
            f"HP: {player_unit.hp:>{hp_width}} | "
            f"Hit: {round(player_hit * 100):>{stat_width}}% | "
            f"Dmg: {player_damage:>{stat_width}} | "
            f"Crit: {round(player_crit * 100):>{stat_width}}%"
        )
        if player_double:
            player_info += "  x2"
        print(player_info)

        # Enemy
        enemy_weapon_str = f"{enemy_unit.equipped_weapon.name:<{weapon_width - 1}}{enemy_weapon_arrow:>1}"
        enemy_info = (
            f"2) {enemy_unit.name:<{name_width}} | "
            f"{enemy_weapon_str} | "
            f"HP: {enemy_unit.hp:>{hp_width}} | "
            f"Hit: {round(enemy_hit * 100):>{stat_width}}% | "
            f"Dmg: {enemy_damage:>{stat_width}} | "
            f"Crit: {round(enemy_crit * 100):>{stat_width}}%"
        )
        if enemy_double:
            enemy_info += "  x2"
        print(enemy_info)

        print("========================================")


    def print_after_print_fight_preview(self):
        print("What do you want to do?")
        print("1) Attack")
        print("2) Choose another weapon")
        print("3) Cancel")
        print("========================================\n")

    def print_at_make_player_round_decsion(self):
        print("What do you want to do?")
        print("1) Attack")
        print("2) Check Inventory")
        print("3) Wait")
        print("4) Surrender")
        print("========================================\n")

    def print_inventory(self):
        player_unit = self.root_service.current_game.player

        print("\n====== Your Inventory ======\n")

        # mark equipped weapon
        if player_unit.equipped_weapon:
            print("Equipped Weapon:")
            print(f"{player_unit.equipped_weapon}")
            print("--------------------------------")

        # other items in inventory
        other_items = [item for item in player_unit.items if item != player_unit.equipped_weapon]

        if not other_items:
            print("No other items in inventory.")
            print("\n============================\n")
            self.print_inventar_choice()
            return

        for index, item in enumerate(other_items, start=1):
            print(f"{index}) {item}")

        print("============================")

        self.print_inventar_choice()

    def print_inventar_choice(self):
        time.sleep(1)
        print("What do you want to do?")
        print("equip <no>   - Equip weapon")
        print("use <no>     - Use item")
        print("exit")
        print("========================================\n")

    def print_after_use_item(self, unit: "Fighter"):
        print(">", unit.name, "used item")

    def print_at_end_fight(self, gold: int, exp: int):
        print("========================================")
        print("           BATTLE RESULTS")
        print("========================================")
        time.sleep(1)
        print(f"You earned {gold} Gold.")
        time.sleep(1)
        print(f"You gained {exp} EXP.")
        time.sleep(1)



    def print_level_up(self, level_up_stats: list):

        if level_up_stats:
            print("LEVEL UP! The following stats increased:")
            for stat in level_up_stats:
                print(f" - {stat} +1")
        else:
            print("No level up this time.")

        time.sleep(1)

    def print_after_surrender(self):
        player_unit = self.root_service.current_game.player
        print(">", player_unit.name, "surrendered.")

        print("========================================")
        print("           BATTLE RESULTS")
        print("========================================")
        time.sleep(1)
        print(f"You earned 0 Gold.")
        time.sleep(1)
        print(f"You gained 0 EXP.")
        time.sleep(1)

