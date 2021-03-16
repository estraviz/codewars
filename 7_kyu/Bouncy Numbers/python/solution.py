"""Bouncy Numbers"""


def is_bouncy(number):
    if number < 100:
        return False
    increase, decrease = False, False
    prev = None
    for i, digit in enumerate(str(number)):
        if i != 0:
            if increase and decrease:
                return True
            else:
                if int(digit) > prev:
                    increase = True
                elif int(digit) < prev:
                    decrease = True
        prev = int(digit)

    if increase and decrease:
        return True
    else:
        return False
