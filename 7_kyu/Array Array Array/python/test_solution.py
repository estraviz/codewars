import pytest

from solution import explode


data = [
    (
        [9, 3],
        [
            [9, 3],
            [9, 3],
            [9, 3],
            [9, 3],
            [9, 3],
            [9, 3],
            [9, 3],
            [9, 3],
            [9, 3],
            [9, 3],
            [9, 3],
            [9, 3],
        ],
    ),
    (["a", 3], [["a", 3], ["a", 3], ["a", 3]]),
    ([6, "c"], [[6, "c"], [6, "c"], [6, "c"], [6, "c"], [6, "c"], [6, "c"]]),
    (["a", "b"], "Void!"),
    ([1, 0], [[1, 0]]),
]


@pytest.mark.parametrize("arr, result", data)
def test_explode(arr, result):
    assert explode(arr) == result
