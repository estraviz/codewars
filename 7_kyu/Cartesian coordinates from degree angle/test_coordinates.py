from coordinates import coordinates


def test_coordinates():
    assert coordinates(90, 1) == (0.0, 1.0)
    assert coordinates(90, 2) == (0.0, 2.0)
    assert coordinates(0, 1),  (1.0, 0.0)
    assert coordinates(45, 1) == (0.7071067812, 0.7071067812)
    assert coordinates(1090, 10000) == (9848.0775301221, 1736.4817766693)
    assert coordinates(-270, 1) == (0.0, 1.0)
