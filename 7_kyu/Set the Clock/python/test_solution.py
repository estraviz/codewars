import pytest

from solution import set_clock


tests = [
    ("9:21", ['M', 'M', 'M', 'M', 'H', 'H', 'M'], "11:26"),
    ("16:54", ['M', 'M', 'H', 'M', 'M', 'H', 'H', 'H', 'M', 'H', 'H', 'M', 'H', 'H'], "24:00"),
    ("24:59", ['M'], "24:00"),
    ("23:59", ['H', 'H'], "1:59"),
    ("10:00", ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'], "9:00"),
]


@pytest.mark.parametrize(
    "time, buttons, expected", tests
)
def test_set_clock(time, buttons, expected):
    assert set_clock(time, buttons) == expected
