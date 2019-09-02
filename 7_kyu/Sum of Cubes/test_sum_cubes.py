from sum_cubes import sum_cubes


def test_sum_cubes():
    assert sum_cubes(1) == 1
    assert sum_cubes(2) == 9
    assert sum_cubes(3) == 36
    assert sum_cubes(4) == 100
    assert sum_cubes(10) == 3025
    assert sum_cubes(123) == 58155876
