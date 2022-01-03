from solution import pair_zeros


def test_should_validate_empty_array():
    assert pair_zeros([]) == []


def test_should_work_with_array_without_zeros():
    assert pair_zeros([1]) == [1]
    assert pair_zeros([1, 2, 3]) == [1, 2, 3]


def test_should_work_with_array_with_zeros():
    assert pair_zeros([0]) == [0]
    assert pair_zeros([0, 0]) == [0]
    assert pair_zeros([0, 0, 0]) == [0, 0]


def test_should_work_with_array_with_zeros_and_other_numbers_combined():
    assert pair_zeros([1, 0, 1, 0, 2, 0, 0]) == [1, 0, 1, 2, 0]
    assert pair_zeros([1, 0, 1, 0, 2, 0, 0, 3, 0]) == [1, 0, 1, 2, 0, 3, 0]


def test_should_handle_large_arrays():
    assert pair_zeros([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0, 0]
    assert pair_zeros([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0, 0, 0]
