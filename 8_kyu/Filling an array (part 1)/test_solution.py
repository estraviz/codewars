from solution import arr


def test_solution():
    assert arr(4) == [0, 1, 2, 3]
    assert arr(0) == []
    assert arr() == []
