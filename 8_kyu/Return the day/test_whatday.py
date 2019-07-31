from whatday import whatday


def test_return_weekday():
    assert whatday(1) == 'Sunday'
    assert whatday(2) == 'Monday'
    assert whatday(3) == 'Tuesday'
    assert whatday(4) == 'Wednesday'
    assert whatday(5) == 'Thursday'
    assert whatday(6) == 'Friday'
    assert whatday(7) == 'Saturday'
    assert whatday(0) == 'Wrong, please enter a number between 1 and 7'
    assert whatday(8) == 'Wrong, please enter a number between 1 and 7'
    assert whatday(20) == 'Wrong, please enter a number between 1 and 7'
