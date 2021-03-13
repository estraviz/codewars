import pytest

from solution import generate


data = [
    (len(generate(0)), 0),
    (len(generate(1)), 1),
    (len(generate(16)), 16),
    (len(generate(32)), 32),
    (len(generate(64)), 64),
    (len(generate(10000)), 10000),
    (len(generate(1000000)), 1000000),
]


@pytest.mark.parametrize(
    "_len, result", data
)
def test_should_respect_the_given_length(_len, result):
    assert _len == result
