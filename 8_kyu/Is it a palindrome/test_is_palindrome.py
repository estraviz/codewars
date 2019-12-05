from is_palindrome import is_palindrome


def test_sample_tests():
    assert is_palindrome('a') is True
    assert is_palindrome('aba') is True
    assert is_palindrome('Abba') is True
    assert is_palindrome('malam') is True
    assert is_palindrome('walter') is False
    assert is_palindrome('kodok') is True
    assert is_palindrome('Kasue') is False
