import pytest

from solution import map, func


data = [
    ([1, 2, 3, "8"], func, [False, True, False, True]),
    ([77, 84, 18, 43, 16, 70, 53], func, [False, True, True, False, True, True, False]),
    ([1, 96, 37, 60, 7], "test", "given argument is not a function"),
    ([72, 12, 30, "q"], func, "array should contain only numbers"),
    ([9, 53], func, [False, False]),
    ([], func, []),
    (["31", "92", "5"], func, [False, True, False]),
    ([10, "str"], "str", "given argument is not a function"),
    (
        [40, 99, 86, 56, 51, 28, 51, 84, 68, 29, 20, 26],
        func,
        [True, False, True, True, False, True, False, True, True, False, True, True],
    ),
    ([1, 96, 37, 60, 7], func, [False, True, False, True, False]),
    ([39, 85, 34], func, [False, False, True]),
    ([58, 76, 40, 87, 64], func, [True, True, True, False, True]),
    ([1, 2, "num"], func, "array should contain only numbers"),
]


@pytest.mark.parametrize("array, function, result", data)
def test_map(array, function, result):
    assert map(array, function) == result
