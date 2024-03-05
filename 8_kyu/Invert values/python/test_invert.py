from invert import invert


def test_invert():
    assert invert([1, 2, 3, 4, 5]) == [-1, -2, -3, -4, -5]
    assert invert([1, -2, 3, -4, 5]) == [-1, 2, -3, 4, -5]
    assert invert([]) == []
    assert invert([0]) == [0]
