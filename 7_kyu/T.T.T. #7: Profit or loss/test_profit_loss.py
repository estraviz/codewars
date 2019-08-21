from profit_loss import profit_loss


def test_profit_loss():
    assert profit_loss([[60, 20], [60, -20]]) == -5
    assert profit_loss([[100, 20], [80, -20]]) == -3.33
    assert profit_loss([[60, 100], [60, -50]]) == -30
    assert profit_loss([[60, 0], [60, 0]]) == 0
