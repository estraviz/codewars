import pytest

from solution import find_children


tests = [
    ("abBA", "AaBb"),
    ("AaaaaZazzz", "AaaaaaZzzz"),
    ("CbcBcbaA", "AaBbbCcc"),
    ("xXfuUuuF", "FfUuuuXx"),
    ("", ""),
]


@pytest.mark.parametrize(
    "dancing_brigade, expected", tests
)
def test_find_children(dancing_brigade, expected):
    assert find_children(dancing_brigade) == expected
