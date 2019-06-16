"""
Duck Duck Goose
"""


def duck_duck_goose(players, goose):
    return players[(goose - 1) % (len(players))].name
