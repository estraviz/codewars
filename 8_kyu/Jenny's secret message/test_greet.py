from greet import greet


def test_greet_normal():
    assert greet("James") == "Hello, James!"
    assert greet("Jane") == "Hello, Jane!"
    assert greet("Jim") == "Hello, Jim!"


def test_greet_special():
    assert greet("Johnny") == "Hello, my love!"
