from abacaba import abacaba


def test_abacaba():
    assert abacaba(1) == "a"
    assert abacaba(2) == "b"
    assert abacaba(3) == "a"
    assert abacaba(4) == "c"
    assert abacaba(5) == "a"
    assert abacaba(6) == "b"
    assert abacaba(7) == "a"
    assert abacaba(8) == "d"
    assert abacaba(12) == "c"
    assert abacaba(16) == "e"
