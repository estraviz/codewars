from zero_fuel import zero_fuel


def test_zero_fuel():
    assert zero_fuel(50, 25, 2) is True
    assert zero_fuel(60, 30, 3) is True
    assert zero_fuel(70, 25, 1) is False
    assert zero_fuel(100, 25, 3) is False
