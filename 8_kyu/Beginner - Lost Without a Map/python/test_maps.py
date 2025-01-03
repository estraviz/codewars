from maps import maps


def test_maps():
    tests = [
        [[1, 2, 3], [2, 4, 6]],
        [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]],
        [[], []]
    ]

    for inp, exp in tests:
        assert maps(inp) == exp
