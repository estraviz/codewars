"""Fuel Calculator
"""


def fuel_price(litres, price_per_liter):
    discount_per_liter = get_discount_per_liter(litres//2)
    return round((price_per_liter - discount_per_liter)*litres, 2)


def get_discount_per_liter(n):
    return 0 if n == 0 else (0.05*n if n in range(1, 5) else 0.25)
