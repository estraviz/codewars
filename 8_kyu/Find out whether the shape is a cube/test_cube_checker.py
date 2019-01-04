from cube_checker import cube_checker


data = [((-12, 2),  False),
        ((8, 3),    False),
        ((8, 2),    True),
        ((-8, -2),  False),
        ((27, 3),   True),
        ((1, 5),    False),
        ((125, 5),  True),
        ((125, -5), False),
        ((0, 0),    False),
        ((0, 12),   False),
        ((12, -1),  False),
        ((1, 1),    True)]


def test_cube_checker():
    for ((v, s), exp) in data:
        assert cube_checker(v, s) == exp
