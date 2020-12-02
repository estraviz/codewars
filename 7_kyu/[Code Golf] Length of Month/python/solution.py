"""
[Code Golf] Length of Month
"""

import calendar


def last_day(yr, mth):
    return calendar.monthrange(yr, mth)[1]
