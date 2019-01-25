"""Finish Guess the Number Game
"""


class Guesser:
    def __init__(self, number, lives):
        self.number = number
        self.lives = lives

    def guess(self, n):
        if self.lives < 1:
            raise Exception("EXCEPTION RAISED")
        if n == self.number:
            return True
        self.lives -= 1
        return False
