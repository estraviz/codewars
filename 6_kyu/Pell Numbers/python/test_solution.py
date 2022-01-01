import pytest

from solution import Pell


basic_tests = [
    [1, 1],
    [2, 2],
    [3, 5],
    [4, 12],
]

pell = Pell()


@pytest.mark.parametrize(
    "inp, expected", basic_tests
)
def test_should_return_the_nth_Pell_number(inp, expected):
    assert pell.get(inp) == expected
