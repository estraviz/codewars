import pytest

from solution import paperwork

data = [
    (5, 5, 25, "Failed at Paperwork(5,5)"),
    (1, 2, 2, "Failed at Paperwork(1,2)"),
    (-5, 5, 0, "Failed at Paperwork(-5,5)"),
    (5, -5, 0, "Failed at Paperwork(5,-5)"),
    (-5, -5, 0, "Failed at Paperwork(-5,-5)"),
    (5, 0, 0, "Failed at Paperwork(5,0)"),
]


@pytest.mark.parametrize(
    "n, m, expected, error_msg", data
)
def test_paperwork(n, m, expected, error_msg):
    assert paperwork(n, m) == expected, error_msg
