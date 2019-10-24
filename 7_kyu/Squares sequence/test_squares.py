from squares import squares


def test_squares():
    assert squares(2, 5) == [2, 4, 16, 256, 65536]
    assert squares(3, 3) == [3, 9, 81]
    assert squares(5, 3) == [5, 25, 625]
    assert squares(10, 4) == [10, 100, 10000, 100000000]
    assert squares(2, 0) == []
    assert squares(2, -4) == []
