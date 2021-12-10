# Alphabet war
def alphabet_war(fight):
    left = {
        'w': 4,
        'p': 3,
        'b': 2,
        's': 1
    }
    right = {
        'm': 4,
        'q': 3,
        'd': 2,
        'z': 1
    }
    left_power = 0
    right_power = 0
    for letter in fight:
        left_power += left.get(letter, 0)
        right_power += right.get(letter, 0)
    if left_power > right_power:
        return "Left side wins!"
    elif right_power > left_power:
        return "Right side wins!"
    return "Let's fight again!"
