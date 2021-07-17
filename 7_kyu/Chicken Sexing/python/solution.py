"""Chicken Sexing"""


def correctness(bobs_decisions, expert_decisions):
    points = 0
    for bobs, experts in zip(bobs_decisions, expert_decisions):
        if bobs == experts:
            points += 1
        elif bobs == '?' or experts == '?':
            points += 0.5
    return points
