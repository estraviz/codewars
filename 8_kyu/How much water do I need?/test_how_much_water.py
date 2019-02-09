from how_much_water import how_much_water


def test_how_much_water():
    assert how_much_water(10, 10, 21) == 'Too much clothes'
    assert how_much_water(10, 10, 2) == 'Not enough clothes'
    assert how_much_water(10, 11, 20) == 23.58
    assert how_much_water(50, 15, 29) == 189.87
    assert how_much_water(50, 15, 15) == 50
