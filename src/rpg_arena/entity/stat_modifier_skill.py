from rpg_arena.entity.skill import Skill


class StatModifierSkill(Skill):
    def __init__(self, name, price, target, value, description):
        super().__init__(name, price, description)
        self.target = target
        self.value = value

    def __str__(self, index=None):
        """
        Return a formatted string for displaying the skill in the shop.

        Args:
            index (int | None, optional): Optional index number before the skill name.

        Returns:
            str: Formatted string with skill info.
        """
        index_str = f"{index}) " if index is not None else ""
        name_width = 20 - len(index_str)
        stat_width = 6

        return (
            f"{index_str}{self.name:<{name_width}} | "
            f"Price: {self.price:>{stat_width}} | "
            f"{getattr(self, 'description', '')}"
        )

    def modify_target(self, target_value, target_type):
        if target_type == "weight" and self.target == "weight":
            return 0

        if target_type == self.target:
            return target_value + self.value
        else:
            return target_value
