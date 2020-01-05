from whoseMove import whose_move


def test_sample_tests():
    assert whose_move('black', False) == 'white'
    assert whose_move('white', False) == 'black'
    assert whose_move('black', True) == 'black'
    assert whose_move('white', True) == 'white'
