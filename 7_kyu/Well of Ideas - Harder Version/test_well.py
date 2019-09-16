from well import well


def test_well():
    assert well([['bad', 'bAd', 'bad'], ['bad', 'bAd', 'bad'],
                 ['bad', 'bAd', 'bad']]) == 'Fail!'
    assert well([['gOOd', 'bad', 'BAD', 'bad', 'bad'], ['bad', 'bAd', 'bad'],
                 ['GOOD', 'bad', 'bad', 'bAd']]) == 'Publish!'
    assert well([['gOOd', 'bAd', 'BAD', 'bad', 'bad', 'GOOD'], ['bad'],
                 ['gOOd', 'BAD']]) == 'I smell a series!'
