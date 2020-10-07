from solution import mirror
import pytest


@pytest.mark.parametrize(
    "data, result",
    [
        ([], []),
        ([1], [1]),
        ([2, 1], [1, 2, 1]),
        ([1, 3, 2], [1, 2, 3, 2, 1]),
        ([-8, 42, 18, 0, -16], [-16, -8, 0, 18, 42, 18, 0, -8, -16])
    ]
)
def test_mirror(data, result):
    assert mirror(data) == result
