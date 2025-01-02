import pytest

from solution import lovefunc

data = [
    (1, 4, True),
    (2, 2, False),
    (0, 1, True),
    (0, 0, False),
]

@pytest.mark.parametrize(
    "flower1, flower2, result", data
)
def test_lovefunc(flower1, flower2, result):
    assert lovefunc(flower1, flower2) == result
