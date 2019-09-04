from movie import movie


def test_movie():
    assert movie(500, 15, 0.9) == 43
    assert movie(100, 10, 0.95) == 24
    assert movie(0, 10, 0.95) == 2
    assert movie(250, 20, 0.9) == 21
    assert movie(500, 20, 0.9) == 34
    assert movie(2500, 20, 0.9) == 135
