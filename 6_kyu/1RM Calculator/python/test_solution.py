import pytest

from .solution import calculate_1RM


data = [
    (135, 20, 282),
    (200, 8, 253),
    (270, 2, 289),
    (360, 1, 360),
    (400, 0, 0),
]


@pytest.mark.parametrize(
    "w, r, result", data
)
def test_calculate_1RM(w, r, result):
    assert calculate_1RM(w, r) == result
