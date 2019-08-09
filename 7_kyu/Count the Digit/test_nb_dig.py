from nb_dig import nb_dig


def test_nb_dig():
    assert nb_dig(5750, 0) == 4700
    assert nb_dig(11011, 2) == 9481
    assert nb_dig(12224, 8) == 7733
    assert nb_dig(11549, 1) == 11905
    assert nb_dig(14550, 7) == 8014
    assert nb_dig(8304, 7) == 3927
    assert nb_dig(10576, 9) == 7860
    assert nb_dig(12526, 1) == 13558
    assert nb_dig(7856, 4) == 7132
    assert nb_dig(14956, 1) == 17267
    assert nb_dig(14956, 1) != -1
