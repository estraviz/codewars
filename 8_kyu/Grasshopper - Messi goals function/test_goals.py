from goals import goals
from random import randint


def test_goals_basic():
    assert goals(0, 0, 0) == 0
    assert goals(5, 10, 2) == 17


def test_goals_random():
    for i in range(50):
        laLiga = randint(0, 50)
        copaDelRey = randint(0, 20)
        championsLeague = randint(0, 10)
        assert goals(laLiga, copaDelRey,
                     championsLeague) == laLiga + copaDelRey + championsLeague
