from remove import remove


tests = [
    # [input, [expected]],
    ["Hi!", "Hi"],
    ["Hi!!!", "Hi!!"],
    ["!Hi", "!Hi"],
    ["!Hi!", "!Hi"],
    ["Hi! Hi!", "Hi! Hi"],
    ["Hi", "Hi"],
    ["", ""],
]


def test_remove():
    for inp, exp in tests:
        assert remove(inp) == exp
