from stack_height_2d import stack_height_2d


def test_stacked_height_2d():
    assert stack_height_2d(1) == 1.0
    assert stack_height_2d(2) == 1.866
    assert stack_height_2d(68) == 59.024
    assert stack_height_2d(51) == 44.301
    assert stack_height_2d(26) == 22.651
    assert stack_height_2d(67) == 58.158
    assert stack_height_2d(46) == 39.971
    assert stack_height_2d(33) == 28.713
    assert stack_height_2d(11) == 9.66
