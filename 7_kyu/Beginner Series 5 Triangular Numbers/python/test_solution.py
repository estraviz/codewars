import pytest

from solution import is_triangular


data_true = [
    (1, True),
    (3, True),
    (6, True),
    (10, True),
    (15, True),
    (21, True),
    (28, True),
]


@pytest.mark.parametrize(
    "t, result", data_true
)
def test_returns_true_when_t_is_a_triangular_numer(t, result):
    assert is_triangular(t) == result


data_false = [
    (2, False),
    (7, False),
    (14, False),
    (27, False),
]


@pytest.mark.parametrize(
    "t, result", data_false
)
def test_returns_false_when_t_is_not_a_triangular_number(t, result):
    assert is_triangular(t) == result
