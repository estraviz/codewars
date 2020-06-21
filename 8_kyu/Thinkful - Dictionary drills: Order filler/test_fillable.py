from fillable import fillable


stock = {
    'football': 4,
    'boardgame': 10,
    'leggos': 1,
    'doll': 5,
}


def test_basic_tests():
    assert fillable(stock, 'football', 3) is True
    assert fillable(stock, 'leggos', 2) is False
    assert fillable(stock, 'action figure', 1) is False
