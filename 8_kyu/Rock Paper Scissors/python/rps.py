PLAYER_1 = "Player 1 won!"
PLAYER_2 = "Player 2 won!"
DRAW = "Draw!"


def rps(p1, p2):
    play = {'paper': 0, 'scissors': 1, 'rock': 2}
    results = {1: PLAYER_1, -2: PLAYER_1, -1: PLAYER_2, 2: PLAYER_2, 0: DRAW}
    return results[play[p1] - play[p2]]
