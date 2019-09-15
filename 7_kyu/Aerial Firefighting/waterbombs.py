"""
Aerial Firefighting
"""

FIRE = 'x'
BUILDING = 'Y'


def waterbombs(fire, w):
    """Function that returns the minimum required waterbombs to extinguish the
       fires in the array"""
    num_waterbombs = 0
    for item in filter(None, fire.split(BUILDING)):
        if len(item) < w:
            num_waterbombs += 1
        else:
            num_waterbombs += len(item) // w + (1 if len(item) % w > 0 else 0)
    return num_waterbombs
