from solution import rotate


def test_rotate():
    assert rotate("Hello") == ["elloH", "lloHe", "loHel", "oHell", "Hello"]
    assert rotate(" ") == [" "]
    assert rotate("") == []
    assert rotate("123") == ["231", "312", "123"]
