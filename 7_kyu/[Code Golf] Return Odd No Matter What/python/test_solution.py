import pytest

from solution import always_odd


@pytest.mark.parametrize(
    "n, result",
    [
        (1, 1),
        (2, 1),
        (5, 5),
        (8, 7),
        (-3, -3),
        (-14, -15),
        (17, 17),
        (180, 179),
        (149, 149),
        (54, 53),
        (-33, -33),
        (-54, -55),
    ],
)
def test_always_odd(n, result):
    assert always_odd(n) == result
