from position import position


def test_position():
    tests = [
        # [input, expected]
        ["a", "Position of alphabet: 1"],
        ["z", "Position of alphabet: 26"],
        ["e", "Position of alphabet: 5"],
    ]

    for inp, exp in tests:
        assert position(inp) == exp
