import pytest

from solution import fibonacci

data = [
    (70, 190392490709135),
    (60, 1548008755920),
    (50, 12586269025),
]


@pytest.mark.parametrize("n, result", data)
def test_fibonacci(n, result):
    assert fibonacci(n) == result
