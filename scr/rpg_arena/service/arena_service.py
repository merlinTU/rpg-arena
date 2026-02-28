from rpg_arena.entity.weapon_type import WeaponType
from rpg_arena.log.arnea_service_printer import ArneaServicePrinter
import random

class ArenaService:
    def __init__(self, root_service: "RootService"):
        self.root_service = root_service
        self.printer = ArneaServicePrinter(root_service)

    def start_arena(self, enemy: "Fighter"):
        self.arena_simulation(self.root_service.current_game.player, enemy)

    def caluclate_hit_chance(self, attacker: "Fighter", defender: "Fighter"):
        hit_chance = max(0, min(100, attacker.calc_hit() - defender.calc_avoid()))
        return hit_chance / 100

    def caluclate_crit_chance(self, attacker: "Fighter", defender: "Fighter"):
        crit_chance = max(0, min(100, attacker.calc_crit() - defender.calc_crit_avoid()))
        return crit_chance / 100

    def calculate_damage(self, attacker: "Fighter", defender: "Fighter"):
        weapon = attacker.weapons[0]
        if weapon.weapon_type == WeaponType.MAGIC:
            return max(0, weapon.strength + attacker.magic - defender.res)
        else:
            return max(0, weapon.strength + attacker.strength - defender.defense)

    def arena_simulation(self, player_unit: "Fighter", enemy_unit: "Fighter"):
        player_initiative = player_unit.speed + player_unit.skill
        enemy_initiative = enemy_unit.speed + enemy_unit.skill

        if player_initiative > enemy_initiative:
            attacker = player_unit
            defender = enemy_unit
        else:
            attacker = enemy_unit
            defender = player_unit

        while True:
            fight_res = self.make_arena_round(attacker, defender)
            if fight_res == -1:
                break
            # next fighters turn
            attacker, defender = defender, attacker

        self.printer.print_after_arena_simulation()





    def make_arena_round(self, first_unit: "Fighter", second_unit: "Fighter"):
        self.make_attack(first_unit, second_unit)
        if second_unit.hp > 0:
            self.make_attack(second_unit, first_unit)
        else:
            return -1

        if first_unit.hp == 0:
            return -1

        if first_unit.speed > second_unit.speed + 5:
            self.make_attack(first_unit, second_unit)
        elif second_unit.speed > first_unit.speed + 5:
            self.make_attack(second_unit, first_unit)

        if first_unit.hp == 0 or second_unit.hp == 0:
            return -1
        else:
            return 1


    def make_attack(self, attacker: "Fighter", defender: "Fighter"):
        hit_chance = self.caluclate_hit_chance(attacker, defender)
        damage = self.calculate_damage(attacker, defender)
        print(hit_chance)
        has_hit = random.random() < hit_chance

        if not has_hit:
            return

        crit_chance = self.caluclate_crit_chance(attacker, defender)
        has_crit = random.random() < crit_chance

        if has_crit:
            damage *= 3

        defender.hp -= damage
        attacker.weapons[0].uses -= 1

        self.printer.print_after_make_attack(attacker, defender, has_hit, has_crit, damage)

