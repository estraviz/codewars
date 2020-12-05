import pytest

from solution import make_new_list


@pytest.mark.parametrize(
    "lst, res",
    [([1, 1, 1, 1], [2, 2, 2]), ([1, 2, 3, 4], [3, 5, 7]), ([1, 10, 100], [11, 110])],
)
def test_make_new_list(lst, res):
    assert make_new_list(lst) == res
