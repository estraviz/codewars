from is_pangram import is_pangram


def test_is_pangram():
    pangram = "The quick, brown fox jumps over the lazy dog!"
    assert is_pangram(pangram) is True
