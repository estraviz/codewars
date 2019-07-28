"""
Tip Calculator
"""

from math import ceil


def calculate_tip(amount, rating):
    service = {'terrible': 0, 'poor': .05, 'good': .10, 'great': .15,
               'excellent': .20}
    tip = service.get(rating.lower(), 'Rating not recognised')
    return tip if isinstance(tip, str) else ceil(tip*amount)
