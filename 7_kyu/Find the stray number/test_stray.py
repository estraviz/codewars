from stray import stray

tests = [
    [[1, 1, 1, 1, 1, 1, 2], 2],
    [[2, 3, 2, 2, 2], 3],
    [[3, 2, 2, 2, 2], 3],
]


def test_stray():
    for inp, exp in tests:
        assert stray(inp) == exp
