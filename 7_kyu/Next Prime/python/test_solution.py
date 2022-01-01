import pytest

from solution import next_prime


tests = [
    (0, 2),
    (2, 3),
    (3, 5),
    (13, 17),
    (181, 191),
    (911, 919),
]


@pytest.mark.parametrize(
    "n, expected", tests
)
def test_should_calculate_next_prime(n, expected):
    assert next_prime(n) == expected
