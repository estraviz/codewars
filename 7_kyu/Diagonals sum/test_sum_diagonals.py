from sum_diagonals import sum_diagonals


def test_0x0():
    matrix = []
    assert sum_diagonals(matrix) == 0


def test_1x1():
    matrix = [[4]]
    assert sum_diagonals(matrix) == 8


def test_2x2():
    matrix = [[1, 2], [3, 4]]
    assert sum_diagonals(matrix) == 1 + 2 + 3 + 4


def test_3x3():
    assert sum_diagonals([[1, 2, 3], [4, 5, 6], [7, 8,
                                                 9]]) == 1 + 5 + 9 + 3 + 5 + 7


def test_4x4():
    matrix = [[-2, 5, 3, 2], [9, -6, 5, 1], [3, 2, 7, 3], [-1, 8, -4, 8]]
    assert sum_diagonals(matrix) == -2 - 6 + 7 + 8 + 2 + 5 + 2 - 1
