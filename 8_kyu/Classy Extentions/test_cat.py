from cat import Cat, Animal
from random import randint


def test_fixed():
    cat = Cat('Mr Whiskers')
    assert cat.speak() == 'Mr Whiskers meows.'

    cat = Cat('Lamp')
    assert cat.speak() == 'Lamp meows.'

    cat = Cat('$$Money Bags$$')
    assert cat.speak() == '$$Money Bags$$ meows.'


def test_random():
    names = ['Mr Whiskers', 'Lamp', '$$Money Bags$$', 'meowmeow',
             'mirou', 'milo', 'spots', 'dog', 'llama', 'code', 'wars',
             'stripes', 'dug', 'barf', "Jury", "Luk", "Bea", "Felix"]

    for _ in range(40):
        name = names[randint(0, len(names) - 1)]
        cat = Cat(name)
        assert cat.speak() == name + " meows."


def test_noise():
    animal = Animal('noise')
    assert animal.speak() == 'noise makes a noise.'
