from excluding_vat_price import excluding_vat_price


def test_excluding_vat_price():
    assert excluding_vat_price(230.00) == 200.00
    assert excluding_vat_price(123) == 106.96
    assert excluding_vat_price(777) == 675.65
    assert excluding_vat_price(460.00) == 400.00
    assert excluding_vat_price(None) == -1
