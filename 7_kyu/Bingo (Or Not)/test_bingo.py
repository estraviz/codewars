from bingo import bingo


def test_example_tests():
    assert bingo([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == "LOSE"
    assert bingo([20, 12, 23, 14, 6, 22, 12, 17, 2, 26]) == "LOSE"
    assert bingo([1, 2, 3, 7, 5, 14, 7, 15, 9, 10]) == "WIN"
    assert bingo([5, 2, 13, 7, 5, 14, 17, 15, 9, 10]) == "WIN"
