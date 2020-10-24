from solution import is_it_possible


def test_is_it_possible():
    assert is_it_possible("XXX" + "XXX" + "XXX") is False
    assert is_it_possible("0XX" + "XX0" + "00X") is True
    assert is_it_possible("XXX" + "0_0" + "___") is True
    assert is_it_possible("___" + "___" + "___") is True
    assert is_it_possible("__0" + "___" + "___") is False
    assert is_it_possible("___" + "_X_" + "___") is True
    assert is_it_possible("XXX" + "000" + "___") is False
    assert is_it_possible("0X_" + "0X0" + "_X_") is False
    assert is_it_possible("0X0" + "0X0" + "__X") is False
    assert is_it_possible("XX_" + "X_X" + "000") is False
    assert is_it_possible("X00" + "0X0" + "XXX") is True
    assert is_it_possible("X_0" + "0X0" + "XX0") is True
