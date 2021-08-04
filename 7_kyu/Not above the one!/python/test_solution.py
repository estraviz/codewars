import pytest

from solution import binary_cleaner


tests = [
    ([0, 1, 2, 1, 0, 2, 1, 1, 1, 0, 4, 5, 6, 2, 1, 1, 0],
     ([0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0], [2, 5, 10, 11, 12, 13])),
    ([0, 1, 1, 2, 0], ([0, 1, 1, 0], [3])),
    ([2, 2, 0], ([0], [0, 1])),
    ([0, 1, 2, 1, 0, 2, 1, 1], ([0, 1, 1, 0, 1, 1], [2, 5])),
    ([1], ([1], [])),
]


@pytest.mark.parametrize(
    "seq, expected", tests
)
def test_binary_cleaner(seq, expected):
    assert binary_cleaner(seq) == expected
