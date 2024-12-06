from close_compare import close_compare


def test_no_margin():
    assert close_compare(4, 5) == -1
    assert close_compare(5, 5) == 0
    assert close_compare(6, 5) == 1


def test_with_margin_of_3():
    assert close_compare(2, 5, 3) == 0
    assert close_compare(5, 5, 3) == 0
    assert close_compare(8, 5, 3) == 0
    assert close_compare(8.1, 5, 3) == 1
    assert close_compare(1.99, 5, 3) == -1
