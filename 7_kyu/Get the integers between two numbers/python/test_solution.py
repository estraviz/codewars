import pytest

from solution import function


tests = [
    (2, 9, [3, 4, 5, 6, 7, 8]),
    (6, 8, [7]),
    (2, 9, [3, 4, 5, 6, 7, 8]),
]


@pytest.mark.parametrize(
    "start_num, end_num, expected", tests
)
def test_should_get_the_integers_between_two_numbers(start_num, end_num, expected):
    assert function(start_num, end_num) == expected
