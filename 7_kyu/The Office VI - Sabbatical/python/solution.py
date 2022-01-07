# The Office VI - Sabbatical
from collections import Counter


def sabb(s, val, happiness):
    result = val + happiness + sum(v for k, v in Counter(s).items() if k in 'sabbatical')
    if result > 22:
        return 'Sabbatical! Boom!'
    else:
        return 'Back to your desk, boy.'
