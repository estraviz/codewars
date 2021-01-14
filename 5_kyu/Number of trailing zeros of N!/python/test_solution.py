import pytest

from solution import zeros


data = [
    (0, 0),
    (6, 1),
    (30, 7),
    (100, 24),
    (1000, 249),
    (100000, 24999),
    (1000000000, 249999998),
]


@pytest.mark.parametrize("n, result", data)
def test_should_pass_sample_tests(n, result):
    assert zeros(n) == result
