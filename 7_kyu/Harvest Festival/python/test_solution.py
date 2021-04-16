import pytest

from solution import plant


data = [
    (",", 3, 7, 25, "---,,,,,,,---,,,,,,,---,,,,,,,"),
    ("+", 1, 3, 15, "-+"),
    (";", 9, 10, 30, "---------;;;;;;;;;;---------;;;;;;;;;;---------;;;;;;;;;;---------;;;;;;;;;;---------;;;;;;;;;;---------;;;;;;;;;;---------;;;;;;;;;;---------;;;;;;;;;;---------;;;;;;;;;;"),
]


@pytest.mark.parametrize(
    "seed, water, fert, temp, expected", data
)
def test_plant(seed, water, fert, temp, expected):
    assert plant(seed, water, fert, temp) == expected
