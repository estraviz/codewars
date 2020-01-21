"""
Calculate Meal Total
"""


def calculate_total(subtotal, tax, tip):
    return round(subtotal * (1 + (tax + tip) / 100), 2)
