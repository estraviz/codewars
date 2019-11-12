"""
The Coupon Code
"""

from dateutil.parser import parse


def check_coupon(entered_code, correct_code, current_date, expiration_date):
    return True if valid_date(current_date, expiration_date) and valid_coupon(
        entered_code, correct_code) else False


def valid_date(date1, date2):
    return parse(date1) <= parse(date2)


def valid_coupon(coupon1, coupon2):
    return coupon1 == coupon2 and type(coupon1) == type(coupon2)
