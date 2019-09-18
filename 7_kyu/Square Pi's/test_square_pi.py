from square_pi import square_pi


def test_square_pi():
    for i in range(2):
        assert square_pi([5, 10][i]) == [8, 15][i]
