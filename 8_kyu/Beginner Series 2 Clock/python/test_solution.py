import pytest

from solution import past

data = [
    (0, 1, 1, 61000),
    (1, 1, 1, 3661000),
    (0, 0, 0, 0),
    (1, 0, 1, 3601000),
    (1, 0, 0, 3600000),
]

@pytest.mark.parametrize(
    "h, m, s, result", data
)
def test_past(h, m, s, result):
    assert past(h, m, s) == result
