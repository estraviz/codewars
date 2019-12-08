"""
Count the smiley faces!
"""


def count_smileys(arr):
    count = 0
    if arr:
        eyes, noses, mouths = [{':', ';'}, {'-', '~'}, {')', 'D'}]
        for smiley in arr:
            if len(smiley) == 2 or len(smiley) == 3:
                eye, nose, mouth = smiley[0], smiley[1:-1], smiley[-1]
                if eye in eyes and mouth in mouths:
                    if nose:
                        if nose not in noses:
                            continue
                    count += 1
    return count
