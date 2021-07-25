"""Greatest Common Factor of an Array"""

import math


def greatest_common_factor(seq):
    temp = seq[0]
    for k in seq[1:]:
        temp = math.gcd(temp, k)
    return temp


# Note: In Python 3.9 the whole list could be passed but CW's kata was for 3.8
