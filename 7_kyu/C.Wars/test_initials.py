from initials import initials


def test_initials():
    assert initials('code wars') == 'C.Wars'
    assert initials('Barack hussein obama') == 'B.H.Obama'
    assert initials('barack hussein Obama') == 'B.H.Obama'
