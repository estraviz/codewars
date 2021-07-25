import pytest

from solution import greatest_common_factor


tests = [
    ([1, 8], 1),
    ([16, 4, 8], 4),
    ([46, 14, 20, 88], 2),
    ([468, 156, 806, 312, 442], 26),
    ([48, 99, 18], 3),
    ([32, 96, 120, 80], 8),
    ([91, 143, 234, 52], 13),
    ([171, 45, 297, 342], 9),
]


@pytest.mark.parametrize(
    "seq, expected", tests
)
def test_greatest_common_factor(seq, expected):
    assert greatest_common_factor(seq) == expected
