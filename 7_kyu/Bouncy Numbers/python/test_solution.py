import pytest

from solution import is_bouncy


data = [
    (0, False),
    (99, False),
    (101, True),
    (120, True),
    (122, False),
    (221, False),
]


@pytest.mark.parametrize(
    "number, result", data
)
def test_is_bouncy(number, result):
    assert is_bouncy(number) == result
