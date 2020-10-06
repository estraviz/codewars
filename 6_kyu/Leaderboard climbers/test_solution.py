from solution import leaderboard_sort
import pytest


@pytest.mark.parametrize(
    "leaderboard, changes, expected", [
        [['John', 'Brian', 'Jim', 'Dave', 'Fred'],
         ['Dave +1', 'Fred +4', 'Brian -1'],
         ['Fred', 'John', 'Dave', 'Brian', 'Jim']],
        [['Bob', 'Larry', 'Kevin', 'Jack', 'Max'],
         ['Max +3', 'Kevin -1', 'Kevin +3'],
         ['Bob', 'Kevin', 'Max', 'Larry', 'Jack']]
    ]
)
def test_leaderboard_sort(leaderboard, changes, expected):
    assert leaderboard_sort(leaderboard, changes) == expected
