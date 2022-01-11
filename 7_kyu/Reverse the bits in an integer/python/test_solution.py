import pytest

from solution import reverse_bits


tests = [
    (417, 267),
    (267, 417),
    (0, 0),
    (2017, 1087),
    (1023, 1023),
    (1024, 1),
]


@pytest.mark.parametrize(
    "n, expected", tests
)
def test_reverse_bits(n, expected):
    assert reverse_bits(n) == expected
