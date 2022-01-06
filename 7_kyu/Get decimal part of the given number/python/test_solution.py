from solution import get_decimal


def test_zero_test_case():
    assert get_decimal(10) == 0


def test_negative_test_case():
    assert get_decimal(-1.2) == 0.2


def test_positive_test_case():
    assert get_decimal(4.5) == 0.5
