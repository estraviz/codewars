from open_or_senior import open_or_senior


def test_open_or_senior():
    result = ['Open', 'Senior', 'Open', 'Senior']
    assert open_or_senior([[45, 12], [55, 21], [19, -2], [104, 20]]) == result

    result = ['Open', 'Open', 'Open', 'Open']
    assert open_or_senior([[3, 12], [55, 1], [91, -2], [54, 23]]) == result

    result = ['Senior', 'Open', 'Open', 'Open']
    assert open_or_senior([[59, 12], [55, -1], [12, -2], [12, 12]]) == result

    result = ['Senior', 'Open', 'Open', 'Open']
    assert open_or_senior([[74, 10], [55, 6], [12, -2], [68, 7]]) == result

    result = ['Open', 'Open', 'Senior', 'Open']
    assert open_or_senior([[16, 23], [56, 2], [56,  8], [54, 6]]) == result
