from is_pangram import is_pangram


def test_is_pangram():
    pangram = "The quick, brown fox jumps over the lazy dog!"
    assert is_pangram(pangram) is True

    pangram = "Cwm fjord bank glyphs vext quiz"
    assert is_pangram(pangram) is True

    pangram = "Pack my box with five dozen liquor jugs."
    assert is_pangram(pangram) is True

    pangram = "How quickly daft jumping zebras vex."
    assert is_pangram(pangram) is True

    pangram = "ABCD45EFGH,IJK,LMNOPQR56STUVW3XYZ"
    assert is_pangram(pangram) is True


def test_is_not_a_pangram():
    pangram = "This isn't a pangram!"
    assert is_pangram(pangram) is False

    pangram = "abcdefghijklmopqrstuvwxyz"
    assert is_pangram(pangram) is False
