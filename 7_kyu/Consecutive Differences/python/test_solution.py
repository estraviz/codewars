import pytest

from solution import differences


tests = [
    ([1, 2, 3], 0),
    ([1, 5, 2, 7, 8, 9, 0], 1),
    ([2, 3, 1], 1),
    ([-1, 2, 3], 2),
]


@pytest.mark.parametrize(
    "lst, expected", tests
)
def test_should_return_consecutive_differences(lst, expected):
    assert differences(lst) == expected
