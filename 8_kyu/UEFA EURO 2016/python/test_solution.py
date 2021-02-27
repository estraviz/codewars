import pytest

from solution import uefa_euro_2016

data = [
    (['Germany', 'Ukraine'], [2, 0], "At match Germany - Ukraine, Germany won!"),
    (['Belgium', 'Italy'], [0, 2], "At match Belgium - Italy, Italy won!"),
    (['Portugal', 'Iceland'], [1, 1], "At match Portugal - Iceland, teams played draw."),
    (['Albania', 'Switzerland'], [1, 2], "At match Albania - Switzerland, Switzerland won!"),
    (['Republic of Ireland', 'Sweden'], [0, 0], "At match Republic of Ireland - Sweden, teams played draw."),
]


@pytest.mark.parametrize(
    "teams, scores, result", data
)
def test_uefa_euro_2016(teams, scores, result):
    assert uefa_euro_2016(teams, scores) == result
