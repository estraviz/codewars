"""New season, new league"""


def premier_league_standings(teams):
    teams_sorted = [teams[1]] + sorted(t for i, t in teams.items() if i > 1)
    return dict((pos+1, team) for pos, team in enumerate(teams_sorted))
