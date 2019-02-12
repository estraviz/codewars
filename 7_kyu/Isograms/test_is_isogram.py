from is_isogram import is_isogram


def test_is_isogram():
    assert is_isogram("Dermatoglyphics") is True
    assert is_isogram("isogram") is True
    assert is_isogram("aba") is False
    assert is_isogram("moOse") is False
    assert is_isogram("isIsogram") is False
    assert is_isogram("") is True
