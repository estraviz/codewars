"""UEFA EURO 2016"""


def uefa_euro_2016(teams, scores):
    teamA, teamB = teams
    scoreA, scoreB = scores
    if scoreA > scoreB:
        winner = teamA
    elif scoreA < scoreB:
        winner = teamB
    else:
        winner = None
    return f"At match {teamA} - {teamB}, {'teams played draw.' if winner is None else ' '.join([winner, 'won!'])}"
