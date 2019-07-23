"""
Grader
"""

from math import floor


def grader(score):
    grades = {1: 'A', .9: 'A', .8: 'B', .7: 'C', .6: 'D'}
    return 'F' if score > 1 else grades.get(floor(score*10)/10, 'F')
