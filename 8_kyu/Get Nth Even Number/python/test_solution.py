import pytest

from solution import nth_even


data = [
    (1, 0),
    (2, 2),
    (3, 4),
    (100, 198),
    (1298734, 2597466),
]


@pytest.mark.parametrize(
    "n, expected", data
)
def test_solution(n, expected):
    assert nth_even(n) == expected
