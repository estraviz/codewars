from growing_plant import growing_plant


def test_growing_plant():
    assert growing_plant(100, 10, 910) == 10
    assert growing_plant(10, 9, 4) == 1
    assert growing_plant(5, 2, 0) == 1
    assert growing_plant(5, 2, 5) == 1
    assert growing_plant(5, 2, 6) == 2
