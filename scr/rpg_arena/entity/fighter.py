from .unit_class import UnitClass
import random

from ..service.data.class_data import CLASS_DATA


class Fighter:
    def __init__(self,  player_class: UnitClass):
        self.name = None
        self.player_class = player_class
        self.level = 1

        stats = CLASS_DATA[player_class]

        self.max_hp = stats.base_hp
        self.hp = stats.base_hp
        self.strength = stats.base_str
        self.magic = stats.base_magic
        self.skill = stats.base_skill
        self.speed = stats.base_speed
        self.luck = stats.base_luck
        self.defense = stats.base_defense
        self.res = stats.base_res

        self.hp_growth = stats.growth_hp
        self.strength_growth = stats.growth_str
        self.magic_growth = stats.growth_magic
        self.skill_growth = stats.growth_skill
        self.speed_growth = stats.growth_speed
        self.luck_growth = stats.growth_luck
        self.defense_growth = stats.growth_defense
        self.res_growth = stats.growth_res

        self.equipped_weapon = None
        self.gold = 0
        self.exp = 0
        self.items = []

    def level_enemy(self, level: int):
        for _ in range(level):
            self.level += 1
            self.hp += self.hp_growth
            self.strength += self.strength_growth
            self.magic += self.magic_growth
            self.skill += self.skill_growth
            self.speed += self.speed_growth
            self.luck += self.luck_growth
            self.defense += self.defense_growth
            self.res_growth += self.res_growth

        self.hp = int(self.hp)
        self.strength = int(self.strength)
        self.magic = int(self.magic)
        self.skill = int(self.skill)
        self.speed = int(self.speed)
        self.luck = int(self.luck)
        self.defense = int(self.defense)
        self.res = int(self.res_growth)

    def level_up(self):
        """
        Level up the character: For each stat, roll against the growth rate.
        If successful, increase the stat by 1.
        Returns a list of stats that were increased.
        """
        increased_stats = []
        stats = [
            ("HP", "hp", "hp_growth"),
            ("Strength", "strength", "strength_growth"),
            ("Magic", "magic", "magic_growth"),
            ("Skill", "skill", "skill_growth"),
            ("Speed", "speed", "speed_growth"),
            ("Luck", "luck", "luck_growth"),
            ("Defense", "defense", "defense_growth"),
            ("Res", "res", "res_growth")
        ]

        for display_name, attr_name, growth_attr in stats:
            growth_chance = getattr(self, growth_attr)

            if random.random() < growth_chance:
                current_value = getattr(self, attr_name)
                setattr(self, attr_name, current_value + 1)
                if attr_name == "hp":
                    setattr(self, "max_hp", current_value + 1)
                increased_stats.append(display_name)

        return increased_stats

    def calc_hit(self):
        weapon_hit = self.items[0].accuracy
        return weapon_hit + self.skill * 2 + self.luck * 0.5

    def calc_avoid(self):
        return self.speed *  2 + self.luck

    def calc_crit(self):
        weapon_crit = self.items[0].crit
        return weapon_crit + self.skill * 0.5

    def calc_crit_avoid(self):
        return self.luck


