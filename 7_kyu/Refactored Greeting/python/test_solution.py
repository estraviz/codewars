from .solution import Person


def test_greet():
    jack = Person("Jack")
    jill = Person("Jill")

    assert jack.greet("Jill") == "Hello Jill, my name is Jack"
    assert jack.greet("Mary") == "Hello Mary, my name is Jack"
    assert jill.greet("Jack") == "Hello Jack, my name is Jill"
