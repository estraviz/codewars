from solution import Cipher


def test_cipher_basic():
    map1 = "abcdefghijklmnopqrstuvwxyz"
    map2 = "etaoinshrdlucmfwypvbgkjqxz"

    cipher = Cipher(map1, map2)
    assert cipher.encode("abc") == "eta"
    assert cipher.encode("xyz") == "qxz"
    assert cipher.encode("aeiou") == "eirfg"
    assert cipher.decode("eta") == "abc"
    assert cipher.decode("qxz") == "xyz"
    assert cipher.decode("eirfg") == "aeiou"
    assert cipher.decode("erlang") == "aikcfu"


def test_cipher_basic_but_changed_map2():
    map1 = "abcdefghijklmnopqrstuvwxyz"
    map2 = 'tfozcivbsjhengarudlkpwqxmy'
    cipher = Cipher(map1, map2)
    assert cipher.encode('abc') == 'tfo'
    assert cipher.decode('tfo') == 'abc'
    assert cipher.encode('tjuukf') == 'kjpphi'
    assert cipher.decode('kjpphi') == 'tjuukf'
    assert cipher.decode('tjuukf') == 'ajqqtb'
    assert cipher.encode('ajqqtb') == 'tjuukf'


def test_cipher_special_characters():
    map1 = "abcdefghijklmnopqrstuvwxyz"
    map2 = 'tfozcivbsjhengarudlkpwqxmy'
    cipher = Cipher(map1, map2)
    assert cipher.encode('a_bc&*83') == 't_fo&*83'
    assert cipher.decode('t_fo*&83') == 'a_bc*&83'
