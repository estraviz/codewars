from elements_sum import elements_sum


def test_elements_sum():
    assert elements_sum([[3, 2, 1, 0], [4, 6, 5, 3, 2], [9, 8, 7, 4]]) == 16
    assert elements_sum([[3], [4, 6, 5, 3, 2], [9, 8, 7, 4]]) == 15
    assert elements_sum([[3, 2, 1, 0], [4, 6, 5, 3, 2], []]) == 7
    assert elements_sum([[3, 2, 1, 0], [4, 6, 5, 3, 2], []], 5) == 12
    assert elements_sum([[3, 2], [4], []]) == 0
