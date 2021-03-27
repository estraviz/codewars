import pytest

from solution import score


@pytest.mark.parametrize(
    "dice, result",
    [
        ([2, 3, 4, 6, 2], 0),
    ]
)
def test_worthless_case(dice, result):
    assert score(dice) == result


@pytest.mark.parametrize(
    "dice, result",
    [
        ([1, 1, 1, 3, 3], 1000),
        ([2, 2, 2, 3, 3], 200),
        ([3, 3, 3, 3, 3], 300),
        ([4, 4, 4, 3, 3], 400),
        ([2, 4, 4, 5, 4], 450),
        ([6, 6, 6, 3, 3], 600),
    ]
)
def test_base_cases(dice, result):
    assert score(dice) == result


@pytest.mark.parametrize(
    "dice, result",
    [
        ([1, 1, 1, 1, 3], 1100),
        ([1, 1, 1, 1, 5], 1150),
        ([2, 4, 4, 5, 4], 450),
        ([3, 4, 5, 3, 3], 350),
        ([1, 5, 1, 3, 4], 250),
    ]
)
def test_mixed_cases(dice, result):
    assert score(dice) == result
