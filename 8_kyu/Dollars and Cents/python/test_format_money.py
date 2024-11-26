from format_money import format_money


def test_format_money():
    assert format_money(39.99) == '$39.99'
    assert format_money(3) == '$3.00'
    assert format_money(3.1) == '$3.10'
