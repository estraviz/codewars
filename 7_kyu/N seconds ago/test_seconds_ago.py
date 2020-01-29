from seconds_ago import seconds_ago


def test_seconds_ago():
    assert seconds_ago('2000-01-01 00:00:00', 1) == '1999-12-31 23:59:59'
    assert seconds_ago('0001-02-03 04:05:06', 7) == '0001-02-03 04:04:59'
