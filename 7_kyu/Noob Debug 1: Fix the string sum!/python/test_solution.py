import pytest

from solution import add

data = [
    ('a', 'b', 195)
]


@pytest.mark.parametrize(
    "s1, s2, result", data
)
def test_add(s1, s2, result):
    assert add(s1, s2) == result
