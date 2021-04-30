import pytest

from solution import number_of_occurrences


sample = [0, 1, 2, 2, 3]

data = [
    (0, sample, 1),
    (4, sample, 0),
    (2, sample, 2),
    (3, sample, 1),
    (4, [], 0),
    (4, [4, 0, 4], 2),
    (1024, [1024, 1024, 2056, 512, 256, 4096, 1024], 3),
    (9, range(1, 10), 1),
    ("abc", ["abc", "123", "123", "abc"], 2),
]


@pytest.mark.parametrize(
    "element, sample, expected", data
)
def test_number_of_ocurrences(element, sample, expected):
    assert number_of_occurrences(element, sample) == expected
