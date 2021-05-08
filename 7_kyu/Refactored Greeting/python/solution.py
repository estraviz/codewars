"""Refactored Greeting"""


class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def greet(self, friend):
        return "Hello %s, my name is %s" % (Person(friend).name, self._name)
