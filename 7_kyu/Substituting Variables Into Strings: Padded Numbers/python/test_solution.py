from solution import solution


def test_solution():
    assert solution(0) == "Value is 00000"
    assert solution(5) == "Value is 00005"
    assert solution(109) == "Value is 00109"
    assert solution(1204) == "Value is 01204"
