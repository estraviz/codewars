from square_or_square_root import square_or_square_root


def test_square_or_square_root():
    tests = [
        [[4, 3, 9, 7, 2, 1], [2, 9, 3, 49, 4, 1]],
        [[100, 101, 5, 5, 1, 1], [10, 10201, 25, 25, 1, 1]],
        [[1, 2, 3, 4, 5, 6], [1, 4, 9, 2, 25, 36]],
    ]

    for inp, exp in tests:
        assert square_or_square_root(inp) == exp
