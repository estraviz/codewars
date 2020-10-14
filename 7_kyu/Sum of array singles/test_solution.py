import pytest
from solution import repeats


@pytest.mark.parametrize(
    "arr, result",
    [
        ([4, 5, 7, 5, 4, 8], 15),
        ([9, 10, 19, 13, 19, 13], 19),
        ([16, 0, 11, 4, 8, 16, 0, 11], 12),
        ([5, 17, 18, 11, 13, 18, 11, 13], 22),
        ([5, 10, 19, 13, 10, 13], 24),
    ],
)
def test_repeates(arr, result):
    assert repeats(arr) == result
