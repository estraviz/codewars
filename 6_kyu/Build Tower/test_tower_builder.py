from tower_builder import tower_builder


def test_basic():
    assert tower_builder(1) == ['*', ]
    assert tower_builder(2) == [' * ', '***']
    assert tower_builder(3) == ['  *  ', ' *** ', '*****']
