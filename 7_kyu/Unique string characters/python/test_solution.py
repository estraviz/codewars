import pytest

from solution import solve


@pytest.mark.parametrize(
    "a, b, result",
    [
        ("xyab", "xzca", "ybzc"),
        ("xyabb", "xzca", "ybbzc"),
        ("abcd", "xyz", "abcdxyz"),
        ("xxx", "xzca", "zca"),
    ],
)
def test_solve(a, b, result):
    assert solve(a, b) == result
