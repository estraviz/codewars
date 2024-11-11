from grow import grow


tests = [
    [6, [1, 2, 3]],
    [16, [4, 1, 1, 1, 4]],
    [64, [2, 2, 2, 2, 2, 2]],
]


def test_grow():
    for exp, inp in tests:
        assert grow(inp) == exp
