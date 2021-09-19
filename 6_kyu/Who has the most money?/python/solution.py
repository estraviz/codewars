"""Who has the most money?"""

from enum import IntEnum
from typing import List


class Student:
    def __init__(self, name, fives, tens, twenties):
        self.name = name
        self.fives = fives
        self.tens = tens
        self.twenties = twenties


class Coins(IntEnum):
    FIVES = 5
    TENS = 10
    TWENTIES = 20


def most_money(students: List[Student]) -> str:
    amounts = {
        student.name: get_student_amount(student) for student in students
    }
    if len(students) == 1:
        return students[0].name
    elif len(set(amounts.values())) == 1:
        return "all"
    else:
        return max(amounts, key=amounts.get)


def get_student_amount(student: Student) -> int:
    return Coins.FIVES * student.fives + \
           Coins.TENS * student.tens + \
           Coins.TWENTIES * student.twenties
