"""
Holiday III - Fire on the boat
"""

import re


def fire_fight(s):
    return re.sub('Fire', '~~', s)
