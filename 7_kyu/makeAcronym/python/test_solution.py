from solution import make_acronym


def test_make_acronym():
    assert make_acronym('My aunt sally') == 'MAS'
    assert make_acronym('Please excuse my dear aunt Sally') == 'PEMDAS'

    s = 'How much wood would a woodchuck chuck if a woodchuck could chuck wood'
    assert make_acronym(s) == 'HMWWAWCIAWCCW'

    assert make_acronym('Unique New York') == 'UNY'
    assert make_acronym('a42') == 'Not letters'
    assert make_acronym('1111') == 'Not letters'
    assert make_acronym(64) == 'Not a string'
    assert make_acronym([]) == 'Not a string'
    assert make_acronym({}) == 'Not a string'
    assert make_acronym("") == ''
