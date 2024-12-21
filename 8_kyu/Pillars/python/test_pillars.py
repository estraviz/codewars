from pillars import pillars


def test_basic_tests():
    assert pillars(0, 1, 1) == 0
    assert pillars(1, 10, 10) == 0
    assert pillars(2, 20, 25) == 2000
    assert pillars(11, 15, 30) == 15270
