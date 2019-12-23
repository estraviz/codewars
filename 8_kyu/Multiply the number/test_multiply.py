from multiply import multiply


def test_multiply():
    assert multiply(10) == 250
    assert multiply(5) == 25
    assert multiply(200) == 25000
    assert multiply(0) == 0
    assert multiply(-2) == -10
