class Class:
    def __init__(self,
                 name: str,
                 base_hp: int,
                 base_str: int,
                 base_magic: int,
                 base_skill: int,
                 base_speed: int,
                 base_luck: int,
                 base_defense: int,
                 base_res: int,

                 growth_hp: float,
                 growth_str: float,
                 growth_magic: float,
                 growth_skill: float,
                 growth_speed: float,
                 growth_luck: float,
                 growth_defense: float,
                 growth_res: float):

        self.name = name
        self.base_hp = base_hp
        self.base_str = base_str
        self.base_magic = base_magic
        self.base_skill = base_skill
        self.base_speed = base_speed
        self.base_luck = base_luck
        self.base_str = base_str
        self.base_defense = base_defense
        self.base_res = base_res

        self.growth_hp = growth_hp
        self.growth_str = growth_str
        self.growth_magic = growth_magic
        self.growth_skill = growth_skill
        self.growth_speed = growth_speed
        self.growth_luck = growth_luck
        self.growth_defense = growth_defense
        self.growth_res = growth_res