import pytest

from solution import lets_test_it


@pytest.mark.parametrize(
    "list1, list2, expected",
    [
        ([0], [1], [0, 1]),
        ([1, 2], [3, 4], [1, 2, 3, 4]),
        ([1], [2, 3, 4], [1, 2, 3, 4]),
        ([1, 2, 3], [4], [1, 2, 3, 4]),
        ([1, 2], [1, 2], [1, 1, 2, 2]),
        ([1, 1], [2, 2], [1, 2]),
        ([1, 1, 1], [2, 2, 2], [1, 2]),
        ([1, 2, 1], [2, 1, 2], [1, 1, 2, 2]),
        ([1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1]),
    ],
)
def test_lets_test_it(list1, list2, expected):
    assert lets_test_it(list1, list2) == expected
