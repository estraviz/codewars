import pytest

from solution import transform


data = [
    ([5, 7, 8, 9, 0, 5], "578905"),
    ([False, True, " d g--"], "FalseTrue d g--"),
    ([78, 0, None, []], "780None[]"),
    ([(), (), ()], "()()()"),
    ([(1, 2), (3, 4), (5, 6)], "(1, 2)(3, 4)(5, 6)"),
    ([(0.707), (3.1416), (2.718)], "0.7073.14162.718"),
    (["abc", "xyz", "jmw"], "abcxyzjmw"),
]


@pytest.mark.parametrize(
    "s, result", data
)
def test_transform(s, result):
    assert transform(s) == result
