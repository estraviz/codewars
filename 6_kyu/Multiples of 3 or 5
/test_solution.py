from solution import solution


def test_should_handle_basic_cases():
    assert solution(10) == 23
    assert solution(20) == 78


def test_should_handle_zeroes():
    assert solution(0) == 0
    assert solution(1) == 0


def test_should_handle_large_numbers():
    assert solution(200) == 9168
