from title_case import title_case


def test_title_case():
    assert title_case('') == ''
    assert title_case('a clash of KINGS', 'a an the of') == 'A Clash of Kings'
    assert title_case('THE WIND IN THE WILLOWS',
                      'The In') == 'The Wind in the Willows'
    assert title_case('the quick brown fox') == 'The Quick Brown Fox'
    assert title_case('', '') == ''
    assert title_case('aBC deF Ghi', None) == 'Abc Def Ghi'
    assert title_case('ab', 'ab') == 'Ab'
    assert title_case('a bc', 'bc') == 'A bc'
    assert title_case('a bc', 'BC') == 'A bc'
    assert title_case('First a of in', 'an often into') == 'First A Of In'
    assert title_case('a clash of KINGS', 'a an the OF') == 'A Clash of Kings'
    assert title_case('the QUICK bRoWn fOX',
                      'xyz fox quick the') == 'The quick Brown fox'
