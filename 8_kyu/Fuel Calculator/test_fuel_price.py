from fuel_price import fuel_price


def test_fuel_price():
    assert fuel_price(10, 21.5) == 212.5
    assert fuel_price(40, 10) == 390
    assert fuel_price(15, 5.83) == 83.7
