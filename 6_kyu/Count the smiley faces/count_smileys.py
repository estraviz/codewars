"""
Count the smiley faces!
"""


def count_smileys(arr):
    count = 0
    if arr:
        eyes, noses, mouths = [{':', ';'}, {'-', '~'}, {')', 'D'}]
        for smiley in arr:
            if len(smiley) == 2:
                eye, mouth = list(smiley)
            elif len(smiley) == 3:
                eye, nose, mouth = list(smiley)
                if nose not in noses:
                    continue
            else:
                continue
            if eye not in eyes or mouth not in mouths:
                continue
            count += 1
    return count
