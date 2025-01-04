import pytest

from solution import cockroach_speed

data = [
    (1.08, 30),
    (1.09, 30),
    (0, 0),
]

@pytest.mark.parametrize("s, result", data)
def test_cockroach_speed(s, result):
    assert cockroach_speed(s) == result
