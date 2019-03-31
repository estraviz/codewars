from persistence import persistence


def test_persistence():
    assert persistence(39) == 3
    assert persistence(4) == 0
    assert persistence(25) == 2
    assert persistence(999) == 4
    assert persistence(444) == 3
