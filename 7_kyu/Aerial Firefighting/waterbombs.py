"""
Aerial Firefighting
"""

from math import ceil

FIRE = 'x'
BUILDING = 'Y'


def waterbombs(fire, wide):
    """Function that returns the minimum required waterbombs to extinguish the
       fires in the array"""
    return sum(ceil(len(item) / wide) for item in fire.split(BUILDING))
