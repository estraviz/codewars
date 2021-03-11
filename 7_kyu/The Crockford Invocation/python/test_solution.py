import pytest

from solution import add, subtract, multiply, apply


data_basic = [
    (add, 3, 4, 7),
    (subtract, 3, 4, -1),
    (multiply, 3, 4, 12),
]


@pytest.mark.parametrize(
    "fun, a, b, result", data_basic
)
def test_basic(fun, a, b, result):
    assert fun(a)(b) == result


data_complex = [
    (add, 3, 4, 7),
    (subtract, 3, 4, -1),
    (multiply, 3, 4, 12),
]


@pytest.mark.parametrize(
    "fun, a, b, result", data_complex
)
def test_complex(fun, a, b, result):
    assert apply(fun)(a)(b) == result
