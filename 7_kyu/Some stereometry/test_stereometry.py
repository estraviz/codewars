from stereometry import stereometry


def test_stereometry():
    assert stereometry(2, 1) == (50.265, 9.425, 10.883)
    assert stereometry(3, 2) == (113.097, 15.708, 14.05)
    assert stereometry(4, 3) == (201.062, 21.991, 16.624)
    assert stereometry(5, 4) == (314.159, 28.274, 18.85)
    assert stereometry(2.98, 1) == (111.594, 24.757, 17.638)
    assert stereometry(1.01, 0.5) == (12.819, 2.419, 5.514)
    assert stereometry(0.9, 0.8) == (10.179, 0.534, 2.591)
    assert stereometry(0.56, 0.43) == (3.941, 0.404, 2.254)
    assert stereometry(0.3, 0.2) == (1.131, 0.157, 1.405)
    assert stereometry(0.74, 0.52) == (6.881, 0.871, 3.308)
