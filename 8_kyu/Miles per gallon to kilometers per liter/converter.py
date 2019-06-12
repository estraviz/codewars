"""
Miles per gallon to kilometers per liter
"""
IMP_GALLON_IN_LITRES = 4.54609188
MILE_IN_KMS = 1.609344


def converter(mpg):
    return round((mpg / IMP_GALLON_IN_LITRES) * MILE_IN_KMS, 2)
