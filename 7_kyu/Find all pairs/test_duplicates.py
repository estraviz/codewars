from duplicates import duplicates


def test_duplicates():
    assert duplicates([1, 2, 5, 6, 5, 2]) == 2
    assert duplicates([1, 2, 2, 20, 6, 20, 2, 6, 2]) == 4
    assert duplicates([0, 0, 0, 0, 0, 0, 0]) == 3
    assert duplicates([1000, 1000]) == 1
    assert duplicates([]) == 0
    assert duplicates([54]) == 0
