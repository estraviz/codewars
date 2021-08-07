import pytest

from solution import player_manager


tests = [
    ("John Doe, 8167238327, Jane Doe, 8163723827",
     [{"player": "John Doe", "contact": 8167238327},
      {"player": "Jane Doe", "contact": 8163723827}]),
    ("", []),
    ("a, 5", [{"player": "a", "contact": 5}]),
    ("jane, 801, dave, 123",
     [{"player": "jane", "contact": 801}, {"player": "dave", "contact": 123}]),
    ("Amelia, 8165254325, Jessie, 9187162345, Marcus Kaine, 8018273245",
    [{"player": "Amelia", "contact": 8165254325},
     {"player": "Jessie", "contact": 9187162345},
     {"player": "Marcus Kaine", "contact": 8018273245}]),
    (None, []),
]


@pytest.mark.parametrize(
    "players, expected", tests
)
def test_player_manager(players, expected):
    assert player_manager(players) == expected
