from converter import converter


def test_converter():
    assert converter(10) == 3.54
    assert converter(20) == 7.08
    assert converter(30) == 10.62
    assert converter(24) == 8.50
    assert converter(36) == 12.74
