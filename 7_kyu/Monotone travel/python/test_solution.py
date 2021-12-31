from solution import is_monotone


def test_should_work_on_increasing_lists():
    assert is_monotone(list(range(1, 11))) is True


def test_should_work_on_constant_lists():
    assert is_monotone([5, 5, 5, 5, 5, 5, 5]) is True


def test_should_work_on_empty_list():
    assert is_monotone([]) is True


def test_shold_work_on_size_1_list():
    assert is_monotone([1]) is True


def test_should_return_false_on_decreasing_list():
    assert is_monotone(list(range(5, 0, -1))) is False
    assert is_monotone(list(range(5, -40, -1))) is False
