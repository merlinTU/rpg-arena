"""
Test module for the GameService class.

This module contains unit tests for the GameService which is responsible
for initializing and controlling the main game flow in the RPG Arena
application.

The tests focus on verifying that the GameService correctly interacts
with its dependent services (roster_service, camp_service, player_action_service)
and initializes the game state as expected.

External dependencies of GameService are replaced with mocks in order
to isolate the logic of the service under test.

Tested functionality:
- Starting a new game
- Starting the arena combat phase
"""

import pytest
from unittest.mock import MagicMock

from rpg_arena.entity.game import Game
from rpg_arena.service.game_service import GameService
from rpg_arena.service.data.weapon_data import CLASS_WEAPON_MAP
from rpg_arena.entity.unit_class import UnitClass
from rpg_arena.entity.fighter import Fighter  # Echte Fighter importieren


@pytest.fixture
def game_service_setup():
    """
    Create a fully mocked GameService test environment.

    Dependencies such as roster_service, player_action_service, and camp_service
    are mocked, but the units themselves are real Fighter objects.

    Returns:
        tuple:
            - game_service (GameService): The GameService instance under test.
            - root_service_mock (MagicMock): The mocked root service.
            - initial_unit (Fighter): The actual Fighter representing the starting character.
    """

    root_service_mock = MagicMock()

    # generate initial unit and enemy
    initial_unit = Fighter(UnitClass.MAGE)
    initial_unit.name = "TestMage"
    root_service_mock.roster_service.generate_initial_units.return_value = [initial_unit]

    enemy_unit = Fighter(UnitClass.THIEF)
    enemy_unit.name = "TestThief"
    root_service_mock.roster_service.generate_enemy_units.return_value = [enemy_unit]

    # Mock player_action_service to always select the initial_unit
    root_service_mock.player_action_service.choose_unit.return_value = initial_unit
    root_service_mock.camp_service.open_camp = MagicMock()

    game_service = GameService(root_service_mock)

    # Mock printer methods to avoid console output during testing
    game_service.printer.print_after_start_game = MagicMock()
    game_service.printer.print_after_choose_first_unit = MagicMock()
    game_service.printer.print_after_start_frist_round = MagicMock()

    return game_service, root_service_mock, initial_unit


def test_start_game(game_service_setup):
    """
    Verify that starting a new game initializes the game state correctly.

    Args:
        game_service_setup : tuple
            Fixture providing:
            - GameService instance
            - mocked root service
            - initial Fighter unit
    """

    game_service, root_service_mock, initial_unit = game_service_setup

    game_service.start_game()

    assert isinstance(root_service_mock.current_game, Game)
    assert root_service_mock.current_game.player == initial_unit
    assert root_service_mock.current_game.player_weapons == CLASS_WEAPON_MAP[UnitClass.MAGE]
    root_service_mock.camp_service.open_camp.assert_called_once()


def test_start_arena(game_service_setup):
    """
    Verify that the arena phase is started correctly.

    Args:
        game_service_setup : tuple
            Fixture providing:
            - GameService instance
            - mocked root service
    """

    game_service, root_service_mock, _ = game_service_setup

    game_service.start_arena()

    root_service_mock.roster_service.generate_enemy_units.assert_called_once()
    game_service.printer.print_after_start_frist_round.assert_called_once_with(
        root_service_mock.roster_service.generate_enemy_units.return_value
    )