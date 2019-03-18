from cup_volume import cup_volume


def test_cup_volume():
    assert cup_volume(1, 1, 1) == 0.79
    assert cup_volume(10, 8, 10) == 638.79
    assert cup_volume(1000, 1000, 1000) == 785398163.4
    assert cup_volume(13.123, 123.12, 1) == 4436.57
    assert cup_volume(5, 12, 31) == 1858.51
