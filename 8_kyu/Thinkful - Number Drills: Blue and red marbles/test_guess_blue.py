from guess_blue import guess_blue


def test_basic_guess_blue():
    assert guess_blue(5, 5, 2, 3) == 0.6
    assert guess_blue(5, 7, 4, 3) == 0.2
    assert guess_blue(12, 18, 4, 6) == 0.4
