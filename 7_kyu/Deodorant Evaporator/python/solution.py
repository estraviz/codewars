"""Deodorant Evaporator"""


def evaporator(content, evap_per_day, threshold):
    amount = 100
    num_days = 0
    while amount > threshold:
        amount *= (1 - evap_per_day/100)
        num_days += 1
    return num_days
