from well import well


def test_well():
    x = ['bad', 'bad', 'bad']
    assert well(x) == 'Fail!'

    x = ['good', 'bad', 'bad', 'bad', 'bad']
    assert well(x) == 'Publish!'

    x = ['good', 'bad', 'bad', 'bad', 'bad', 'good', 'bad', 'bad', 'good']
    assert well(x) == 'I smell a series!'
