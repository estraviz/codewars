from calculator import calculator


def test_simple():
    assert calculator(6, 2, '+') == 8
    assert calculator(4, 3, '-') == 1
    assert calculator(5, 5, '*') == 25
    assert calculator(5, 4, '/') == 1.25


def test_error():
    assert calculator(6, 2, '&') == "unknown value"
    assert calculator(6, "$", '+') == "unknown value"
    assert calculator(6, 2, '&') == "unknown value"
    assert calculator(4, 3, '\\') == "unknown value"
    assert calculator("a", 3, "+") == "unknown value"
    assert calculator(6, 2, '=') == "unknown value"
    assert calculator(6, 2, '\t') == "unknown value"
    assert calculator(":", ",", '+') == "unknown value"
