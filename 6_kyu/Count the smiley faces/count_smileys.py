"""
Count the smiley faces!
"""


def count_smileys(arr):
    if not arr:
        return 0
    eyes = {':', ';'}
    noses = {'-', '~'}
    mouths = {')', 'D'}
    count = 0
    for smiley in arr:
        if smiley == '':
            continue
        eye = smiley[0]
        if eye not in eyes:
            continue
        if len(smiley) == 3:
            nose = smiley[1]
            if nose not in noses:
                continue
            mouth = smiley[2]
        else:
            mouth = smiley[1]
        if mouth not in mouths:
            continue
        count += 1
    return count
