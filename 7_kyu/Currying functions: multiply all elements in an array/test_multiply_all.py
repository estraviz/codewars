from multiply_all import multiply_all


def test_must_return_an_array():
    assert isinstance(multiply_all([1])(1), list) is True


def test_array_has_correct_length():
    assert len(multiply_all([1, 2])(1)) == 2


def test_returned_array_has_correct_values():
    assert multiply_all([1, 2, 3])(1) == [1, 2, 3]
    assert multiply_all([1, 2, 3])(2) == [2, 4, 6]
    assert multiply_all([1, 2, 3])(0) == [0, 0, 0]
    assert multiply_all([])(10) == []
