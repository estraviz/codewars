from high_and_low import high_and_low


def test_high_and_low():
    assert high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6") == "542 -214"
    assert high_and_low("10 2 -2 -10") == "10 -10"
    assert high_and_low("1 -1") == "1 -1"
    assert high_and_low("1 1") == "1 1"
    assert high_and_low("-1 -1") == "-1 -1"
    assert high_and_low("1 -1 0") == "1 -1"
    assert high_and_low("1 1 0") == "1 0"
    assert high_and_low("-1 -1 0") == "0 -1"
    assert high_and_low("42") == "42 42"
