import pytest

from solution import infected


tests = [
    ("01000000X000X011X0X", 73.33333333333333),
    ("01X000X010X011XX", 72.72727272727273),
    ("XXXXX", 0),
    ("00000000X00X0000", 0),
    ("0000000010", 100),
    ("000001XXXX0010X1X00010", 100),
    ("X00X000000X10X0100", 42.857142857142854),
]


@pytest.mark.parametrize(
    "s, expected", tests
)
def test_infected(s, expected):
    assert infected(s) == expected
