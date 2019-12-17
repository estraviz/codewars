from remove import remove


def test_remove():
    tests = [
        # [input, expected],
        ["Hi!", "Hi"],
        ["Hi!!!", "Hi"],
        ["!Hi", "!Hi"],
        ["!Hi!", "!Hi"],
        ["Hi! Hi!", "Hi! Hi"],
        ["Hi", "Hi"],
    ]

    for inp, exp in tests:
        assert remove(inp) == exp
