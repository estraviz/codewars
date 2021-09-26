"""Lottery Ticket"""


def bingo(ticket, win):
    mini_wins = 0
    for code, number in ticket:
        for char in set(code):
            if ord(char) == number:
                mini_wins += 1
    return "Winner!" if mini_wins >= win else "Loser!"
