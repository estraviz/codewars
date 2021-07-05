from solution import is_matching


def test_is_matching():
    assert is_matching("bouh", "0", "buh") is False
    assert is_matching("kitten", "t", "eink") is False
    assert is_matching("mentalist", "l.st", "metan") is False
    assert is_matching("impressionistic", "isis isi", "precomnt") is True
    assert is_matching("email box", "bail", "moxe") is True
    assert is_matching("detail", "tlei", "dai") is False
