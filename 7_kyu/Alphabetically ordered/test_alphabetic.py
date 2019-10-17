from alphabetic import alphabetic


def test_alphabetic():
    assert alphabetic('asd') is False
    assert alphabetic('codewars') is False
    assert alphabetic('door') is True
    assert alphabetic('cell') is True
    assert alphabetic('z') is True
    assert alphabetic('') is True
