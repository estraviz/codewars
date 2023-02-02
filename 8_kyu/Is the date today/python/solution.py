from datetime import datetime


def is_today(date):
    return datetime.today().date() == date.date()
