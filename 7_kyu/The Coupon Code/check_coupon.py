"""
The Coupon Code
"""

from dateutil.parser import parse


def check_coupon(entered_code, correct_code, current_date, expiration_date):
    return True if parse(current_date) <= parse(
        expiration_date) and entered_code == correct_code and type(
            entered_code) == type(correct_code) else False
