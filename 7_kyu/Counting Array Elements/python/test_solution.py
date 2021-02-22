import pytest

from solution import count


data = [
    ([], {}),
    (['a'], {'a': 1}),
    (['a', 'a', 'b', 'b', 'b'], {'a': 2, 'b': 3}),
    (['a', 'b', 'b', 'b', 'a'], {'a': 2, 'b': 3}),
    (["", 'a', True, 15, "b", "b"], {'': 1, 'a': 1, 15: 1, 'b': 2, True: 1}),
]


@pytest.mark.parametrize(
    "array, result", data
)
def test_count(array, result):
    assert count(array) == result
