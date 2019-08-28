from palindrome import palindrome


def test_should_return_true():
    assert palindrome(1221) is True
    assert palindrome(110011) is True
    assert palindrome(1456009006541) is True
    assert palindrome(1) is True


def test_should_return_false():
    assert palindrome(123322) is False
    assert palindrome(152) is False
    assert palindrome(9999) is True


def test_should_return_not_valid():
    assert palindrome("ACCDDCCA") == "Not valid"
    assert palindrome("1221") == "Not valid"
    assert palindrome(-450) == "Not valid"
    assert palindrome("@14AbC") == "Not valid"
