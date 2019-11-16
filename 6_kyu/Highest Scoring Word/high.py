"""
Highest Scoring Word
"""

from string import ascii_letters


def high(x):
    dic = {
        word: sum(ascii_letters.find(chr) + 1 for chr in word)
        for word in x.split()
    }
    return max(dic, key=dic.get)
