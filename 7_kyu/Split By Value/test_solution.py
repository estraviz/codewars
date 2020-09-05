from solution import split_by_value
import pytest


@pytest.mark.parametrize(
    "k, elements, result",
    [[5, [1, 3, 5, 7, 6, 4, 2], [1, 3, 4, 2, 5, 7, 6]],
     [0, [5, 2, 7, 3, 2], [5, 2, 7, 3, 2]],
     [6, [6, 4, 10, 10, 6], [4, 6, 10, 10, 6]]]
)
def test_split_by_value(k, elements, result):
    assert split_by_value(k, elements) == result
