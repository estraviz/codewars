from is_opposite import is_opposite


def test_is_opposite():
    assert is_opposite("ab", "AB") is True
    assert is_opposite("aB", "Ab") is True
    assert is_opposite("aBcd", "AbCD") is True
    assert is_opposite("AB", "Ab") is False
    assert is_opposite("", "") is False
