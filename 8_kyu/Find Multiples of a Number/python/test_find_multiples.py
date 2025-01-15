from find_multiples import find_multiples


def test_find_multiples():
    assert find_multiples(5, 25) == [5, 10, 15, 20, 25]
    assert find_multiples(1, 2) == [1, 2]
    assert find_multiples(5, 7) == [5]
    assert find_multiples(4, 27) == [4, 8, 12, 16, 20, 24]
    assert find_multiples(11, 54) == [11, 22, 33, 44]
