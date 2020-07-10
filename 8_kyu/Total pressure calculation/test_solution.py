from solution import solution
from pytest import approx


def test_solution():
    assert solution(44, 30, 3, 2, 5, 50) == approx(
        0.7146511212121212, rel=1e-9, abs=1e-9)
    assert solution(60, 20, 10, 30, 10, 100) == approx(
        5.099716666666667, rel=1e-9, abs=1e-9)
