import pytest

from solution import remove_every_other

data = [
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 3, 5, 7, 9]),
]

@pytest.mark.parametrize(
    "my_list, result", data
)
def test_remove_every_other(my_list, result):
    assert remove_every_other(my_list) == result
