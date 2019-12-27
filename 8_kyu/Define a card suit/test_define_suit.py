from define_suit import define_suit


def test_define_suit():
    assert define_suit('3C') == 'clubs'
    assert define_suit('QS') == 'spades'
    assert define_suit('9D') == 'diamonds'
    assert define_suit('JH') == 'hearts'
