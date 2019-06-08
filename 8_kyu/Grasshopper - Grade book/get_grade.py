"""Grasshopper - Grade book
"""
from statistics import mean


def get_grade(s1, s2, s3):
    grades = {100: 'A', 90: 'A', 80: 'B', 70: 'C', 60: 'D', 0: 'F'}
    return grades.get((mean([s1, s2, s3])//10)*10, 'F')
