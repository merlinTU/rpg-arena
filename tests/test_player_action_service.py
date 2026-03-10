"""
Test module for the PlayerActionService class.

This module contains unit tests for the PlayerActionService which is responsible
for handling user input when selecting units or enemies during gameplay.

The tests focus on verifying that the PlayerActionService correctly interprets
user input and returns the appropriate Fighter instance.

External dependencies such as the RootService and the information_service
are replaced with mocks to isolate the behavior of the PlayerActionService.

Tested functionality:
- Selecting a unit by name
- Selecting a unit by number
- Handling invalid input and retry logic
- Interaction with the information service
"""

import pytest
from unittest.mock import MagicMock, patch

from rpg_arena.service.player_action_service import PlayerActionService
from rpg_arena.entity.unit_class import UnitClass
from rpg_arena.entity.fighter import Fighter


@pytest.fixture
def player_action_service_setup():
    """
    Create a PlayerActionService with a mocked RootService.

    The information_service is mocked so that it never intercepts
    the user input during normal tests.

    returns:
        A tuple containing:
            - service (PlayerActionService): The service instance under test.
            - root_service_mock (MagicMock): Mocked root service dependency.
    """

    root_service_mock = MagicMock()
    root_service_mock.information_service.check_information_service_call.return_value = False

    service = PlayerActionService(root_service_mock)

    return service, root_service_mock


def test_choose_unit_by_name(player_action_service_setup):
    """
    Verify that a unit can be selected by entering its name.

    This test ensures that the PlayerActionService correctly
    matches the entered name with the corresponding unit.

    Args:
        player_action_service_setup : tuple
            Fixture providing the PlayerActionService and mocked RootService.
    """

    service, _ = player_action_service_setup

    unit1 = Fighter(UnitClass.FIGHTER)
    unit1.name = "Alice"

    unit2 = Fighter(UnitClass.FIGHTER)
    unit2.name = "Bob"

    units = [unit1, unit2]

    with patch("builtins.input", side_effect=["Bob"]):
        selected = service.choose_unit(units)

    assert selected == unit2


def test_choose_unit_by_number(player_action_service_setup):
    """
    Verify that a unit can be selected by entering its list number.

    Args:
        player_action_service_setup : tuple
            Fixture providing the PlayerActionService and mocked RootService.
    """

    service, _ = player_action_service_setup

    unit1 = Fighter(UnitClass.FIGHTER)
    unit1.name = "Alice"

    unit2 = Fighter(UnitClass.FIGHTER)
    unit2.name = "Bob"

    units = [unit1, unit2]

    with patch("builtins.input", side_effect=["2"]):
        selected = service.choose_unit(units)

    assert selected == unit2


def test_choose_unit_invalid_then_valid(player_action_service_setup):
    """
    Verify that invalid input triggers a retry until a valid selection is made.

    Args:
        player_action_service_setup : tuple
            Fixture providing the PlayerActionService and mocked RootService.
    """

    service, _ = player_action_service_setup

    unit1 = Fighter(UnitClass.FIGHTER)
    unit1.name = "Alice"

    unit2 = Fighter(UnitClass.FIGHTER)
    unit2.name = "Bob"

    units = [unit1, unit2]

    # First input invalid, second valid
    with patch("builtins.input", side_effect=["Charlie", "1"]):
        selected = service.choose_unit(units)

    assert selected == unit1


def test_choose_enemy_by_name(player_action_service_setup):
    """
    Verify that an enemy can be selected by entering its name.

    Args:
        player_action_service_setup : tuple
            Fixture providing the PlayerActionService and mocked RootService.
    """

    service, _ = player_action_service_setup

    enemy1 = Fighter(UnitClass.FIGHTER)
    enemy1.name = "Gladiator1"

    enemy2 = Fighter(UnitClass.FIGHTER)
    enemy2.name = "Gladiator2"

    enemies = [enemy1, enemy2]

    with patch("builtins.input", side_effect=["Gladiator2"]):
        selected = service.choose_enemy(enemies)

    assert selected == enemy2


def test_choose_enemy_by_number(player_action_service_setup):
    """
    Verify that an enemy can be selected by entering its list number.

    Args:
        player_action_service_setup : tuple
            Fixture providing the PlayerActionService and mocked RootService.
    """

    service, _ = player_action_service_setup

    enemy1 = Fighter(UnitClass.FIGHTER)
    enemy1.name = "Gladiator1"

    enemy2 = Fighter(UnitClass.FIGHTER)
    enemy2.name = "Gladiator2"

    enemies = [enemy1, enemy2]

    with patch("builtins.input", side_effect=["1"]):
        selected = service.choose_enemy(enemies)

    assert selected == enemy1


def test_choose_enemy_invalid_then_valid(player_action_service_setup):
    """
    Verify that invalid enemy input results in a retry.

    Args:
        player_action_service_setup : tuple
            Fixture providing the PlayerActionService and mocked RootService.
    """

    service, _ = player_action_service_setup

    enemy1 = Fighter(UnitClass.FIGHTER)
    enemy1.name = "Gladiator1"

    enemy2 = Fighter(UnitClass.FIGHTER)
    enemy2.name = "Gladiator2"

    enemies = [enemy1, enemy2]

    with patch("builtins.input", side_effect=["xxx", "2"]):
        selected = service.choose_enemy(enemies)

    assert selected == enemy2


def test_choose_unit_information_service_continue():
    """
    Verify that the information service can intercept input and
    that the selection continues afterwards.
    """

    root_service = MagicMock()

    # Information service returns True first, then False
    root_service.information_service.check_information_service_call = MagicMock(
        side_effect=[True, False]
    )

    service = PlayerActionService(root_service)

    unit = Fighter(UnitClass.FIGHTER)
    unit.name = "Hero"
    units = [unit]

    # First input triggers information service, second selects the unit
    with patch("builtins.input", side_effect=["info stats", "1"]):
        result = service.choose_unit(units)

    assert root_service.information_service.check_information_service_call.call_count == 2
    assert result == unit


def test_choose_enemy_invalid_number_print(capsys):
    """
    Verify that an invalid numeric selection prints an error message
    before allowing the user to retry.
    """

    root_service = MagicMock()
    root_service.information_service.check_information_service_call.return_value = False

    service = PlayerActionService(root_service)

    enemy = Fighter(UnitClass.FIGHTER)
    enemy.name = "Gladiator"

    enemies = [enemy]

    # First number invalid, second valid
    with patch("builtins.input", side_effect=["5", "1"]):
        result = service.choose_enemy(enemies)

    captured = capsys.readouterr()

    assert "Invalid number. Try again." in captured.out
    assert result == enemy