import pytest

from solution import add_five

@pytest.mark.parametrize(
    "num, expected", [
        (5, 10),
        (0, 5),
        (-5, 0),
    ]
)
def test_add_five(num, expected):
    assert add_five(num) == expected
