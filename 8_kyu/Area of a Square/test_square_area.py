from square_area import square_area


def test_square_area():
    assert square_area(2) == 1.62
    assert square_area(0) == 0
    assert square_area(14.05) == 80
    assert square_area(1) == 0.41
    assert square_area(100) == 4052.85
