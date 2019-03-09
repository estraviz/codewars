from xo import xo


def test_xo_True():
    assert xo('xo') is True
    assert xo('XO') is True
    assert xo('xo0') is True
    assert xo('') is True
    assert xo('xxxxxoooxooo') is True
    assert xo('xxxxxoooXooo') is True
    assert xo('abcdefghijklmnopqrstuvwxyz') is True


def test_xo_False():
    assert xo('xxxoo') is False
    assert xo('xXxXOoOoOo') is False
    assert xo('x') is False
    assert xo('O') is False
