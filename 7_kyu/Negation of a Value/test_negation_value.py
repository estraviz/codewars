from negation_value import negation_value


def test_fixed_tests():
    assert negation_value("!", False) is True
    assert negation_value("!", True) is False
    assert negation_value("!!!", []) is True
