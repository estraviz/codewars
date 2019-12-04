from solution import solution


def test_solution():
    assert solution([1000, 1000, 100], ["g", "kg", "m"]) == 6.67e-12
    assert solution([1000, 1000, 100], ["kg", "kg", "cm"]) == 0.0000667
