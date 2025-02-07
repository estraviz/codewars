from bool_to_word import bool_to_word


def test_bool_to_word():
    assert bool_to_word(True) == 'Yes'
    assert bool_to_word(False) == 'No'
