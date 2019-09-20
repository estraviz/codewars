from incrementer import incrementer


def test_fixed_tests():
    incrementer([]) == []
    incrementer([1, 2, 3]) == [2, 4, 6]
    incrementer([4, 6, 7, 1, 3]) == [5, 8, 0, 5, 8]
    incrementer([3, 6, 9, 8, 9]) == [4, 8, 2, 2, 4]
    incrementer([1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 9, 9,
                 8]) == [2, 4, 6, 8, 0, 2, 4, 6, 8, 9, 0, 1, 2, 2]
