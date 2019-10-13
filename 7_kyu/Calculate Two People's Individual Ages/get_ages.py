"""
Calculate Two People's Individual Ages
"""


def get_ages(sum_, difference):
    x1, x2 = (sum_ + difference) / 2, (sum_ - difference) / 2
    return None if any(q < 0 for q in (sum_, difference, x1, x2)) else (x1, x2)
