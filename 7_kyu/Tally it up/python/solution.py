"""Tally it up"""


def score_to_tally(score):
    output = ""
    while True:
        if score <= 5:
            return output + ("e <br>" if score == 5 else "abcd"[score - 1])
        else:
            output += 'e <br>'
            score -= 5
