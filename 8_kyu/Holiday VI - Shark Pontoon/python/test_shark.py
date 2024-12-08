from shark import shark


def test_shark():
    assert shark(12, 50, 4, 8, True) == "Alive!"
    assert shark(7, 55, 4, 16, True) == "Alive!"
    assert shark(24, 0, 4, 8, True) == "Shark Bait!"
    assert shark(40, 35, 3, 20, True) == "Shark Bait!"
    assert shark(7, 8, 3, 4, True) == "Alive!"
