import pytest

from solution import shared_bits


@pytest.mark.parametrize(
    "a, b, result",
    [
        (1, 2, False),
        (16, 8, False),
        (1, 1, False),
        (2, 3, False),
        (7, 10, False),
        (43, 77, True),
        (7, 15, True),
        (23, 7, True),
    ],
)
def test_shared_bits(a, b, result):
    assert shared_bits(a, b) is result
