from palindrome import palindrome_chain_length


def test_palindrome():
    assert palindrome_chain_length(87) == 4
    assert palindrome_chain_length(1) == 0
    assert palindrome_chain_length(88) == 0
    assert palindrome_chain_length(89) == 24
    assert palindrome_chain_length(10) == 1
