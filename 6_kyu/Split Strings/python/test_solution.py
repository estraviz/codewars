import pytest

from solution import solution


@pytest.mark.parametrize(
    "s, result",
    [
        ("asdfadsf", ["as", "df", "ad", "sf"]),
        ("asdfads", ["as", "df", "ad", "s_"]),
        ("", []),
        ("x", ["x_"]),
    ],
)
def test_solution(s, result):
    assert solution(s) == result
