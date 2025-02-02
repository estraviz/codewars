from math import ceil

def duty_free(price, discount, holiday_cost):
    return holiday_cost // (price * discount / 100)
