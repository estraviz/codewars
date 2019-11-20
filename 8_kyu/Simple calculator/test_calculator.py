from calculator import calculator


def test_calculator():
    assert calculator(6, 2, '+') == 8
    assert calculator(4, 3, '-') == 1
    assert calculator(5, 5, '*') == 25
    assert calculator(5, 4, '/') == 1.25
    assert calculator(6, 2, '&') == "unknown value"
