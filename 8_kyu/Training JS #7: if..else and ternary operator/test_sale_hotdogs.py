from sale_hotdogs import sale_hotdogs


def test_sale_hotdogs():
    assert sale_hotdogs(0) == 0
    assert sale_hotdogs(1) == 100
    assert sale_hotdogs(2) == 200
    assert sale_hotdogs(3) == 300
    assert sale_hotdogs(4) == 400
    assert sale_hotdogs(5) == 475
    assert sale_hotdogs(9) == 855
    assert sale_hotdogs(10) == 900
    assert sale_hotdogs(11) == 990
    assert sale_hotdogs(100) == 9000
