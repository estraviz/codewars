from opposite import opposite


def test_opposite():
    assert opposite(1) == -1
    assert opposite(25.6) == -25.6
    assert opposite(0) == 0
    assert opposite(1425.2222) == -1425.2222
    assert opposite(-3.1458) == 3.1458
    assert opposite(-95858588225) == 95858588225
