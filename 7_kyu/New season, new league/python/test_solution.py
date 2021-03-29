import pytest

from solution import premier_league_standings


data = [
    ({1: "Arsenal"}, {1: "Arsenal"}),
    ({2: "Arsenal", 3: "Accrington Stanley", 1: "Leeds United"}, {3: "Arsenal", 2: "Accrington Stanley", 1: "Leeds United"}),
    ({1: "Leeds United", 2: "Liverpool", 3: "Manchester City", 4: "Coventry", 5: "Arsenal"}, {1: "Leeds United", 2: "Arsenal", 3: "Coventry", 4: "Liverpool", 5: "Manchester City"}),
]


@pytest.mark.parametrize(
    "teams, result", data
)
def test_premier_league_standings(teams, result):
    assert premier_league_standings(teams) == result
