import pytest

from solution import duty_free

data = [
    (10, 10, 500, 500),
    (12, 50, 1000, 166),
    (17, 10, 500, 294),
]

@pytest.mark.parametrize(
    "price, discount, holiday_cost, expected", data
)
def test_duty_free(price, discount, holiday_cost, expected):
    assert duty_free(price, discount, holiday_cost) == expected
