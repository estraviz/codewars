from divisions import divisions


def test_divisions():
    assert divisions(6, 2) == 2
    assert divisions(100, 2) == 6
    assert divisions(2450, 5) == 4
    assert divisions(9999, 3) == 8
    assert divisions(2, 3) == 0
    assert divisions(5, 5) == 1
