import pytest

from solution import solve


basic_tests = [
    (2, 256, True),
    (2, 253, False),
    (9, 243, True),
    (15, 12, False),
    (21, 2893401, True),
    (21, 2893406, False),
    (54, 2834352, True),
    (54, 2834359, False),
    (1000013, 7187761, True),
    (1000013, 7187762, False),
]


@pytest.mark.parametrize(
    "a, b, expected", basic_tests
)
def test_should_solve_for_basic_tests(a, b, expected):
    assert solve(a, b) == expected
