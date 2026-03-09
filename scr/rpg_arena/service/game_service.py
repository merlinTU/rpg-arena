from rpg_arena.entity.game import Game
from rpg_arena.log.game_service_printer import GameServicePrinter
from rpg_arena.service.data.weapon_data import CLASS_WEAPON_MAP


class GameService:
    def __init__(self, root_service: "RootService"):
        self.root_service = root_service
        self.printer = GameServicePrinter(root_service)

    def start_game(self):
        self.root_service.current_game = Game()

        initial_units = self.root_service.roster_service.generate_initial_units()
        self.printer.print_after_start_game(initial_units)

        player_unit = self.root_service.player_action_service.choose_unit(initial_units)
        self.printer.print_after_choose_first_unit(player_unit)

        self.root_service.current_game.player = player_unit

        # set the initial weapons the player can buy in shop
        self.root_service.current_game.player_weapons = CLASS_WEAPON_MAP[player_unit.player_class]
        self.root_service.camp_service.open_camp()

    def start_arena(self):
        enemy_units = self.root_service.roster_service.generate_enemy_units()
        self.printer.print_after_start_frist_round(enemy_units)
