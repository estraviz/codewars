from digital_root import digital_root


def test_digital_root():
    assert digital_root(0) == 0
    assert digital_root(16) == 7
    assert digital_root(195) == 6
    assert digital_root(456) == 6
    assert digital_root(992) == 2
    assert digital_root(167346) == 9
    assert digital_root(999999999999) == 9
