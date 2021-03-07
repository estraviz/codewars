import pytest

from solution import doubleton


data = [
    (120, 121),
    (1234, 1311),
    (10, 12),
    (1, 10),
    (111, 112),
]


@pytest.mark.parametrize(
    "num, result", data
)
def test_doubleton(num, result):
    assert doubleton(num) == result
