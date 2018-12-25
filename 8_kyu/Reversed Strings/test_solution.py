from solution import solution


def test_solution():
    assert solution('world') == 'dlrow'
    assert solution('hello') == 'olleh'
    assert solution('') == ''
    assert solution('h') == 'h'
