from palindrome import palindrome


def test_valid_cases():
    assert palindrome(6, 4) == [11, 22, 33, 44]
    assert palindrome(75, 1) == [77]
    assert palindrome(19, 3) == [22, 33, 44]
    assert palindrome(101, 2) == [101, 111]


def test_not_valid_cases():
    assert palindrome("ACCDDCCA", 3) == "Not valid"
    assert palindrome(773, "1551") == "Not valid"
    assert palindrome(-4505, 15) == "Not valid"
