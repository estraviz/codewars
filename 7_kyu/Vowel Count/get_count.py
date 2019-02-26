"""Vowel Count
"""
VOWELS = 'aeiouAEIOU'


def get_count(inputStr):
    return sum(1 for letter in inputStr if letter in VOWELS)
