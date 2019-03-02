from get_sum import get_sum


def test_get_sum_positive():
    assert get_sum(0, 1) == 1
    assert get_sum(1, 2) == 3
    assert get_sum(5, -1) == 14
    assert get_sum(505, 4) == 127759
    assert get_sum(321, 123) == 44178


def test_get_sum_negative():
    assert get_sum(0, -1) == -1
    assert get_sum(-50, 0) == -1275
    assert get_sum(-1, -5) == -15
    assert get_sum(-5, -5) == -5
    assert get_sum(-505, 4) == -127755
    assert get_sum(-321, 123) == -44055


def test_get_sum_zero():
    assert get_sum(0, 0) == 0


def test_get_sum_switch_min_max():
    assert get_sum(-5, -1) == -15
    assert get_sum(5, 1) == 15


def test_get_sum_equal():
    assert get_sum(-17, -17) == -17
    assert get_sum(17, 17) == 17
