import pytest

from solution import how_many_light_sabers_do_you_own


data = [
    ("Zach", 18),
    ("Adam", 0),
    (None, 0),
    ("zach", 0),
]

@pytest.mark.parametrize(
    "name, result", data
)
def test_how_many_light_sabers_do_you_own(name, result):
    assert how_many_light_sabers_do_you_own(name) == result
