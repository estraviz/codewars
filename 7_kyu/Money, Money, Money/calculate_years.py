"""
Money, Money, Money
"""


def calculate_years(principal, interest, tax, desired):
    if principal < desired:
        return 1 + calculate_years(
            principal * (1 + interest) - principal * interest * tax, interest,
            tax, desired)
    return 0
