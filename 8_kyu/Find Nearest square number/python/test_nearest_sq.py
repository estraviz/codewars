from nearest_sq import nearest_sq


def test_nearest_sq():
    assert nearest_sq(1) == 1
    assert nearest_sq(2) == 1
    assert nearest_sq(10) == 9
    assert nearest_sq(111) == 121
    assert nearest_sq(9999) == 10000
