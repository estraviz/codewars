"""
Are there any arrows left?
"""


def any_arrows(arrows):
    return True if any(('damaged' not in arrow or arrow['damaged'] is False)
                       for arrow in arrows) else False
