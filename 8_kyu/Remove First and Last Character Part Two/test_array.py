from array import array


def test_array():
    assert array('') is None
    assert array('1') is None
    assert array('1, 3') is None
    assert array('1,2,3') == '2'
    assert array('1,2,3,4') == '2 3'
