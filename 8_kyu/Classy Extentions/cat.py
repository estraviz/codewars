"""Classy Extensions
"""


class Animal(object):
    def __init__(self, name):
        self.name = name

    def speak(self):
        return('{} makes a noise.'.format(self.name))


class Cat(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)

    def speak(self):
        return('{} meows.'.format(self.name))
