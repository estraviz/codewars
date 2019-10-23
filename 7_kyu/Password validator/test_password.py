from password import password


def test_password():
    assert password("Abcd1234") is True
    assert password("Abcd123") is False
    assert password("abcd1234") is False
    assert password("AbcdefGhijKlmnopQRsTuvwxyZ1234567890") is True
    assert password("ABCD1234") is False
    assert password("Ab1!@#$%^&*()-_+={}[]|\:;?/>.<,") is True
    assert password("!@#$%^&*()-_+={}[]|\:;?/>.<,") is False
    assert password("") is False
    assert password(" aA1----") is True
    assert password("4aA1----") is True
