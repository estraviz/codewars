from arithmetic import arithmetic


def test_arithmetic():
    assert arithmetic(1, 2, "add") == 3
    assert arithmetic(8, 2, "subtract") == 6
    assert arithmetic(5, 2, "multiply") == 10
    assert arithmetic(8, 2, "divide") == 4
