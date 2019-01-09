from hotpo import hotpo


def test_hotpo():
    assert hotpo(1) == 0
    assert hotpo(5) == 5
    assert hotpo(6) == 8
    assert hotpo(23) == 15
