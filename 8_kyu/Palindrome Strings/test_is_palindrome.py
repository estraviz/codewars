from is_palindrome import is_palindrome


def test_is_palindrome():
    assert is_palindrome("anna") is True
    assert is_palindrome("walter") is False
    assert is_palindrome(12321) is True
    assert is_palindrome(123456) is False
