from solution import solution


def test_short_long_short():
    assert solution('45', '1') == '1451'
    assert solution('13', '200') == '1320013'
    assert solution('Soon', 'Me') == 'MeSoonMe'
    assert solution('U', 'False') == 'UFalseU'
