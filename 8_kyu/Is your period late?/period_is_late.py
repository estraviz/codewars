"""Is your period late?
"""
from datetime import timedelta


def period_is_late(last, today, cycle_length):
    return True if today - last > timedelta(cycle_length) else False
