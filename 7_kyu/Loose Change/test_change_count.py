from change_count import change_count


def test_change_count():
    assert change_count('dime penny dollar') == '$1.11'
    assert change_count('dime penny nickel') == '$0.16'
    assert change_count('quarter quarter') == '$0.50'
    assert change_count('dollar penny dollar') == '$2.01'
    assert change_count(
        'dollar dollar dollar dollar dollar dollar dollar dollar dollar dollar penny'
    ) == '$10.01'
