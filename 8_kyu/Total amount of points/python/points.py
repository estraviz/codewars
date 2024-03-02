"""Total amount of points
"""


def points(games):
    points = 0
    for result in games:
        home, away = result.split(':')
        if home > away:
            points += 3
        elif home < away:
            points += 0
        else:
            points += 1
    return points
