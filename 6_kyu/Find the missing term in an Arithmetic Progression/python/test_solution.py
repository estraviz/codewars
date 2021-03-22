import pytest

from solution import find_missing


data = [
    ([1, 2, 3, 4, 6, 7, 8, 9], 5),
    ([1, 3, 4, 5, 6, 7, 8, 9], 2),
]


@pytest.mark.parametrize(
    "sequence, result", data
)
def test_find_missing(sequence, result):
    assert find_missing(sequence) == result
