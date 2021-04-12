import pytest

from solution import to_time


data = [
    (3600, '1 hour(s) and 0 minute(s)'),
    (3601, '1 hour(s) and 0 minute(s)'),
    (3500, '0 hour(s) and 58 minute(s)'),
    (323500, '89 hour(s) and 51 minute(s)'),
    (0, '0 hour(s) and 0 minute(s)'),
]


@pytest.mark.parametrize(
    "seconds, result", data
)
def test_to_time(seconds, result):
    assert to_time(seconds) == result
