from square_sum import square_sum


def test_square_sum():
    assert square_sum([1, 2]) == 5
    assert square_sum([0, 3, 4, 5]) == 50
    assert square_sum([]) == 0
    assert square_sum([-1, -2]) == 5
    assert square_sum([-1, 0, 1]) == 2
