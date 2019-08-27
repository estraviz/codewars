from multiples import multiples


def test_sample_tests():
    assert multiples(3, 5) == [5, 10, 15]
    assert multiples(1, 3.14) == [3.14]
    assert multiples(5, -1) == [-1, -2, -3, -4, -5]
