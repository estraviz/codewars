from format_duration import format_duration


def test_now():
    assert format_duration(0) == "now"


def test_hours():
    assert format_duration(1) == "1 second"
    assert format_duration(62) == "1 minute and 2 seconds"
    assert format_duration(120) == "2 minutes"
    assert format_duration(3600) == "1 hour"
    assert format_duration(3662) == "1 hour, 1 minute and 2 seconds"


def test_years():
    result = "182 days, 1 hour, 44 minutes and 40 seconds"
    assert format_duration(15731080) == result

    result = "4 years, 68 days, 3 hours and 4 minutes"
    assert format_duration(132030240) == result

    result = "6 years, 192 days, 13 hours, 3 minutes and 54 seconds"
    assert format_duration(205851834) == result

    result = "8 years, 12 days, 13 hours, 41 minutes and 1 second"
    assert format_duration(253374061) == result

    result = "7 years, 246 days, 15 hours, 32 minutes and 54 seconds"
    assert format_duration(242062374) == result

    result = "3 years, 85 days, 1 hour, 9 minutes and 26 seconds"
    assert format_duration(101956166) == result

    result = "1 year, 19 days, 18 hours, 19 minutes and 46 seconds"
    assert format_duration(33243586) == result
