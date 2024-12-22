from bin_to_decimal import bin_to_decimal


def test_bin_to_decimal():
    tests = [("1", 1), ("0", 0), ("1001001", 73)]
    for t in tests:
        inp, exp = t
        assert bin_to_decimal(inp) == exp
