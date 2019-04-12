from array_diff import array_diff


def test_array_diff():
    assert array_diff([1, 2], [1]) == [2]
    assert array_diff([1, 2, 2], [1]) == [2, 2]
    assert array_diff([1, 2, 2], [2]) == [1]
    assert array_diff([1, 2, 2], []) == [1, 2, 2]
    assert array_diff([], [1, 2]) == []
