from solution import solution


def test_duplicate_arguments():
    assert solution(1, 2, 3, 1, 2) is True
    assert solution() is False
    assert solution(1, 1) is True
    assert solution(1, 0) is False
    assert solution('a', 'b') is False
    assert solution('a', 'b', 'a') is True
    assert solution(1, 2, 42, 3, 4, 5, 42) is True
    assert solution('a', 'b', 'c', 'd') is False
    assert solution('a', 'b', 'c', 'd') is False
    assert solution('a', 'b', 'c', 'c') is True
    assert solution('a', 'b', 'c', 'd', 'e', 'f', 'f', 'b') is True
