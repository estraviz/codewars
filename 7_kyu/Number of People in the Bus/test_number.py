from number import number


def test_number():
    assert number([[10, 0], [3, 5], [5, 8]]) == 5
    assert number([[3, 0], [9, 1], [4, 10], [12, 2], [6, 1], [7, 10]]) == 17
    assert number([[3, 0], [9, 1], [4, 8], [12, 2], [6, 1], [7, 8]]) == 21
    assert number([[0, 0]]) == 0
