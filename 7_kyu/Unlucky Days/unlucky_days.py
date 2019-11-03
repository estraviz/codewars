"""
Unlucky Days
"""

from datetime import datetime


def unlucky_days(year):
    return sum(1 for month in range(1, 13)
               if datetime(year, month, 13).weekday() == 4)
