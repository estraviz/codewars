import pytest
from solution import max_number


@pytest.mark.parametrize(
    "n, result",
    [[213, 321], [7389, 9873], [63792, 97632], [566797, 977665], [1000000, 1000000]],
)
def test_max_number(n, result):
    assert max_number(n) == result
