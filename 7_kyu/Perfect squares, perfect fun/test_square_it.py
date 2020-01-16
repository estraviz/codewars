from square_it import square_it


def test_square_it():
    assert square_it(1) == "1"
    assert square_it(222) == "Not a perfect square!"
    assert square_it(234562342342) == "Not a perfect square!"
    assert square_it(88989) == "Not a perfect square!"
    assert square_it(112141568) == "112\n141\n568"
