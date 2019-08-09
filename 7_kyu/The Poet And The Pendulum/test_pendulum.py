from pendulum import pendulum


def test_pendulum():
    values = [4, 6, 8, 7, 5]
    assert pendulum(values) == [8, 6, 4, 5, 7]

    values = [19, 30, 16, 19, 28, 26, 28, 17, 21, 17]
    assert pendulum(values) == [28, 26, 19, 17, 16, 17, 19, 21, 28, 30]

    values = [-9, -2, -10, -6]
    assert pendulum(values) == [-6, -10, -9, -2]

    values = [-19, -9, -5, -6, -15, -16, -5, -12]
    assert pendulum(values) == [-5, -9, -15, -19, -16, -12, -6, -5]

    values = [11, -16, -18, 13, -11, -12, 3, 18]
    assert pendulum(values) == [13, 3, -12, -18, -16, -11, 11, 18]
