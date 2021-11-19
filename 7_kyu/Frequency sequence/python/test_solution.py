import pytest

from solution import freq_seq

tests = [
    ("hello world", "-", "1-1-3-3-2-1-1-2-1-3-1"),
    ("19999999", ":", "1:7:7:7:7:7:7:7"),
    ("^^^**$", "x", "3x3x3x2x2x1")
]


@pytest.mark.parametrize(
    "s, sep, expected", tests
)
def test_freq_seq(s, sep, expected):
    assert freq_seq(s, sep) == expected
