"""Refactored Greeting"""


class Person:
    def __init__(self, name):
        self.name = name

    def greet(self, friend):
        return f"Hello {friend}, my name is {self.name}"
