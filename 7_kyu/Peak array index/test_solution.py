from solution import peak


def test_peak():
    assert peak([1, 2, 3, 5, 3, 2, 1]) == 3
    assert peak([1, 12, 3, 3, 6, 3, 1]) == 2
    assert peak([10, 20, 30, 40]) == -1
