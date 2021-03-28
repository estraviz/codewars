import pytest

from solution import pattern


data = [
    (1, "1"),
    (4, "1234\n2341\n3412\n4123"),
    (0, ""),
    (7, "1234567\n2345671\n3456712\n4567123\n5671234\n6712345\n7123456"),
    (-25, ""),
]


@pytest.mark.parametrize(
    "n, result", data
)
def test_pattern(n, result):
    assert pattern(n) == result
