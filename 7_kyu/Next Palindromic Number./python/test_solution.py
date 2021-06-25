import pytest

from solution import next_pal


tests = [
    (11, 22),
    (188, 191),
    (191, 202),
    (2541, 2552),
]


@pytest.mark.parametrize(
    "val, expected", tests
)
def test_should_calculate_next_palindrome(val, expected):
    assert next_pal(val) == expected
