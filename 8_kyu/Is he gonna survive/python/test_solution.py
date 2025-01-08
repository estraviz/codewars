import pytest

from solution import hero

data = [
    (10, 5, True),
    (7, 4, False),
    (4, 5, False),
    (100, 40, True),
    (1500, 751, False),
    (0, 1, False),
]

@pytest.mark.parametrize(
    "bullets, dragons, result", data
)
def test_hero(bullets, dragons, result):
    assert hero(bullets, dragons) == result
