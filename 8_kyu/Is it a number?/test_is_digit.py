from is_digit import is_digit


def test_is_digit():
    assert is_digit("s2324") is False
    assert is_digit("-234.4") is True
    assert is_digit("3 4") is False
    assert is_digit("3-4") is False
    assert is_digit("3 4   ") is False
    assert is_digit("34.65") is True
    assert is_digit("-0") is True
    assert is_digit("0.0") is True
    assert is_digit("") is False
    assert is_digit(" ") is False
