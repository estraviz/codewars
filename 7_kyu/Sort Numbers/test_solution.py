from solution import solution


def test_solution():
    assert solution([1, 2, 3, 10, 5]) == [1, 2, 3, 5, 10]
    assert solution(None) == []
    assert solution([]) == []
    assert solution([20, 2, 10]) == [2, 10, 20]
    assert solution([2, 20, 10]) == [2, 10, 20]
