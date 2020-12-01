import pytest

from solution import balanced_num


@pytest.mark.parametrize(
    "number, result",
    [
        (7, "Balanced"),
        (959, "Balanced"),
        (13, "Balanced"),
        (432, "Not Balanced"),
        (424, "Balanced"),
    ],
)
def test_check_balanced_number(number, result):
    assert balanced_num(number) == result


@pytest.mark.parametrize(
    "number, result",
    [
        (1024, "Not Balanced"),
        (66545, "Not Balanced"),
        (295591, "Not Balanced"),
        (1230987, "Not Balanced"),
        (56239814, "Balanced"),
    ],
)
def test_check_large_number(number, result):
    assert balanced_num(number) == result
