"""
Calculate Two People's Individual Ages
"""


def get_ages(sum_, difference):
    x1, x2 = (sum_ + difference) / 2, (sum_ - difference) / 2
    return None if (sum_ < 0 or difference < 0 or x1 < 0 or x2 < 0) else tuple(
        sorted((x1, x2), reverse=True))
