import pytest

from solution import evaporator


data = [
    (10, 10, 10, 22),
    (10, 10, 5, 29),
    (100, 5, 5, 59),
    (50, 12, 1, 37),
    (47.5, 8, 8, 31),
    (100, 1, 1, 459),
    (10, 1, 1, 459),
    (100, 1, 5, 299),
]


@pytest.mark.parametrize(
    "content, evap_per_day, threshold, result", data
)
def test_evaporator(content, evap_per_day, threshold, result):
    assert evaporator(content, evap_per_day, threshold) == result
