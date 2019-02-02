"""Days in the year
"""


def year_days(year):
    return "{} has {} days".format(year,
                                   366 if (year % 4 == 0 and year % 100 != 0)
                                   or (year % 400 == 0) else 365)
