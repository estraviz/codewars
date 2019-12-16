from switcher import switcher


def test_switcher():
    arr = ['24', '12', '23', '22', '4', '26', '9', '8']
    assert switcher(arr) == 'codewars'

    arr = [
        '25', '7', '8', '4', '14', '23', '8', '25', '23', '29', '16', '16', '4'
    ]
    assert switcher(arr) == 'btswmdsbd kkw'

    assert switcher(['4', '24']) == 'wc'
    assert switcher(['12']) == 'o'

    arr = ['12', '28', '25', '21', '25', '7', '11', '22', '15']
    assert switcher(arr) == 'o?bfbtpel'
