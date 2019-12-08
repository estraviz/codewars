"""
Count the smiley faces!
"""


def count_smileys(arr):
    return sum(1 for s in arr if is_a_smiley(s))


def is_a_smiley(s):
    eyes, noses, mouths = (':', ';'), ('-', '~', ''), (')', 'D')
    eye, nose, mouth = s[0], s[1:-1], s[-1]
    return True if eye in eyes and nose in noses and mouth in mouths else False
