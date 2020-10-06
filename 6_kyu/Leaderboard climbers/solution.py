"""Leaderboard climbers
"""


def leaderboard_sort(leaderboard, changes):
    for change in changes:
        name, pos = change.split()
        old_index = leaderboard.index(name)
        leaderboard.insert(old_index - int(pos), leaderboard.pop(old_index))
    return leaderboard
