"""Tally it up"""


def score_to_tally(score):
    return (score // 5) * 'e <br>' + (score % 5 != 0) * "abcd"[score % 5 - 1]
