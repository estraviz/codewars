'''Thinkful - Number Drills: Blue and red marbles
'''


def guess_blue(blue_start, red_start, blue_pulled, red_pulled):
    numerator = blue_start - blue_pulled
    denominator = blue_start - blue_pulled + red_start - red_pulled
    return numerator / denominator
