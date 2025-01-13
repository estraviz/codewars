from remove_char import remove_char


def test_remove_char():
    assert remove_char('eloquent') == 'loquen'
    assert remove_char('country') == 'ountr'
    assert remove_char('person') == 'erso'
    assert remove_char('place') == 'lac'
    assert remove_char('ok') == ''
