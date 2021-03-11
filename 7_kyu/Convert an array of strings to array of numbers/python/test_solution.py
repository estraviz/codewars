import pytest

from solution import to_float_array


data = [
    (["1.1", "2.2", "3.3"], [1.1, 2.2, 3.3]),
]


@pytest.mark.parametrize(
    "arr, result", data
)
def test_to_float_array(arr, result):
    assert to_float_array(arr) == result
