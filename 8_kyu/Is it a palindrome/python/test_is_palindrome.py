from is_palindrome import is_palindrome


def test_sample_tests():
    assert is_palindrome('a') is True
    assert is_palindrome('aba') is True
    assert is_palindrome('Abba') is True
    assert is_palindrome('malam') is True
    assert is_palindrome('walter') is False
    assert is_palindrome('kodok') is True
    assert is_palindrome('Kasue') is False
    assert is_palindrome('hello') is False
    assert is_palindrome('Bob') is True
    assert is_palindrome('Madam') is True
    assert is_palindrome('AbBa') is True
    assert is_palindrome('') is True
    assert is_palindrome("LAGrALLyiclOaEowNvmU") is False
    assert is_palindrome("cWalaIYFGucHEhbnEH") is False
    assert is_palindrome("smlWLKQYCrRUcqOLYuGGuYLOqcURrCYQKLWlms") is True
    assert is_palindrome("dRjLeHcvvcHeLjRd") is True
    assert is_palindrome("wvvqHAfrFWkIYygRQHTR") is False
    assert is_palindrome("zuKWoAyeQNvhurRlYlUUlYlRruhvNQeyAoWKuz") is True
    assert is_palindrome("QtFpQMSYPMnnMPYSMQpFtQ") is True
    assert is_palindrome("muNcdggdcNum") is True
    assert is_palindrome("TUkKinLuE") is False
    assert is_palindrome("MaKeRSDisini") is False
