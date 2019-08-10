from generate_pairs import generate_pairs


def test_generate_pairs_two():
    solution = [[0, 0], [0, 1], [0, 2], [1, 1], [1, 2], [2, 2]]
    assert generate_pairs(2) == solution


def test_generate_pairs_zero():
    solution = [[0, 0]]
    assert generate_pairs(0) == solution
