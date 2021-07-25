import pytest

from solution import sum_of_integers_in_string


tests = [
    ("12.4", 16),
    ("h3ll0w0rld", 3),
    ("2 + 3 = ", 5),
    ("Our company made approximately 1 million in gross revenue last quarter.", 1),
    ("The Great Depression lasted from 1929 to 1939.", 3868),
    ("Dogs are our best friends.", 0),
    ("C4t5 are 4m4z1ng.", 18),
    ("The30quick20brown10f0x1203jumps914ov3r1349the102l4zy dog", 3635),
]


@pytest.mark.parametrize(
    "s, expected", tests
)
def test_sum_of_integers_in_string(s, expected):
    assert sum_of_integers_in_string(s) == expected
