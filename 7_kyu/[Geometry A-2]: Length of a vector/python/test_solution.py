import pytest

from solution import vector_length


tests = [
    ([[0, 1], [0, 0]], 1),
    ([[0, 3], [4, 0]], 5),
    ([[1, -1], [1, -1]], 0),
]


@pytest.mark.parametrize(
    "vector, expected", tests
)
def test_fixed_test_cases(vector, expected):
    assert vector_length(vector) == expected
