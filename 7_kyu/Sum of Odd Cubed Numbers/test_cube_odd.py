from cube_odd import cube_odd


def test_cube_odd():
    assert cube_odd([1, 2, 3, 4]) == 28
    assert cube_odd([-3, -2, 2, 3]) == 0
    assert cube_odd(["a", 12, 9, "z", 42]) is None
