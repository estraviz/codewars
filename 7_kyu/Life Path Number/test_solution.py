import pytest
from solution import life_path_number, reduce


smart_dudes = [
    "Einstein",
    "Ada Lovelace",
    "Brendan Eich",
    "Leonardo da Vinci",
    "Charles Babbage",
    "Grace Hopper",
    "Alan Turing",
    "Steve Wozniak",
    "Guido van Rossum",
    "Yukihiro Matsumoto",
]
births = [
    ["1879-03-14", 6],
    ["1815-12-10", 1],
    ["1961-07-04", 1],
    ["1452-04-15", 4],
    ["1791-12-26", 2],
    ["1906-12-09", 1],
    ["1912-06-23", 6],
    ["1950-08-11", 7],
    ["1956-01-31", 8],
    ["1965-04-14", 3],
]


@pytest.mark.parametrize("birthdate, result", births)
def test_life_path_number(birthdate, result):
    assert life_path_number(birthdate) == result
