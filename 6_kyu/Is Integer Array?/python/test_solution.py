import pytest

from solution import is_int_array


tests = [
    ([], True),
    ([1, 2, 3, 4], True),
    ([-11, -12, -13, -14], True),
    ([1.0, 2.0, 3.0], True),
    ([1, 2, None], False),
    (None, False),
    ("", False),
    ([None], False),
    ([1.0, 2.0, 3.0001], False),
    (["-1"], False),
    ([1.2, 1.8, 3], False),
]


@pytest.mark.parametrize(
    "arr, expected", tests
)
def test_is_int_array(arr, expected):
    assert is_int_array(arr) == expected
