from solution import validate_pin


def test_should_return_False_for_pins_with_length_other_than_4_or_6():
    assert validate_pin("1") is False
    assert validate_pin("12") is False
    assert validate_pin("123") is False
    assert validate_pin("12345") is False
    assert validate_pin("1234567") is False
    assert validate_pin("-1234") is False
    assert validate_pin("1.234") is False
    assert validate_pin("00000000") is False


def test_should_return_False_for_pins_which_contain_chars_other_than_digits():
    assert validate_pin("a234") is False
    assert validate_pin(".234") is False
    assert validate_pin("-123") is False
    assert validate_pin("-1.234") is False


def test_should_return_True_for_valid_pins():
    assert validate_pin("1234") is True
    assert validate_pin("0000") is True
    assert validate_pin("1111") is True
    assert validate_pin("123456") is True
    assert validate_pin("098765") is True
    assert validate_pin("000000") is True
    assert validate_pin("123456") is True
    assert validate_pin("090909") is True
