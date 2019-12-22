"""
Are there any arrows left?
"""


def any_arrows(arrows):
    for arrow in arrows:
        if 'damaged' in arrow and arrow['damaged']:
            continue
        if 'damage' not in arrow:
            return True
    return False
