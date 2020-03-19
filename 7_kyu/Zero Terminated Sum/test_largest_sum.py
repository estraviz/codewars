from largest_sum import largest_sum


def test_sample():
    assert largest_sum("72102450111111090") == 11
    assert largest_sum("123004560") == 15
    assert largest_sum("0") == 0
