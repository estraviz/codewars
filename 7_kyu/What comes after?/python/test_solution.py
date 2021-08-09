import pytest

from solution import comes_after


tests = [
    ("Pirates say arrrrrrrrr.", 'r', 'arrrrrrrr'),
    ("Free coffee for all office workers!", 'F', 'rfeofi'),
    ("king kUnta is the sickest rap song ever kNown k!", 'k', 'iUeN'),
    ("p8tice makes pottery p0rfect!", 'p', 'o'),
    ("d8u d._ rly 2d1s", 'D', ''),
    ("nothing to be found here", 'z', ''),
    ("are you really learning Ruby?", 'r', 'eenu'),
    ("Every Sunday, she reads newspapers.", 's', 'uhp'),
]


@pytest.mark.parametrize(
    "st, letter, expected", tests
)
def test_comes_after(st, letter, expected):
    assert comes_after(st, letter) == expected
