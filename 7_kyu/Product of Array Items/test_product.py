from product import product


def test_product():
    assert product([5, 4, 1, 3, 9]) == 540
    assert product([-2, 6, 7, 8]) == -672
    assert product([10]) == 10
    assert product([0, 2, 9, 7]) == 0
    assert product(None) is None
    assert product([]) is None
