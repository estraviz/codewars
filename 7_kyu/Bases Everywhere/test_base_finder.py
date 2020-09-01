from base_finder import base_finder


def test_base_finder():
    seq = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    assert base_finder(seq) == 10

    seq = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    assert base_finder(seq) == 10

    seq = ['1', '2', '3', '4', '5', '6', '10', '11', '12', '13']
    assert base_finder(seq) == 7

    seq = ['301', '302', '303', '304', '305', '310', '311', '312', '313', '314']
    assert base_finder(seq) == 6

    seq = ['50', '51', '61', '53', '54', '60', '52', '62', '55', '56']
    assert base_finder(seq) == 7
