from greet import greet


def test_greet():
    assert greet('english') == 'Welcome'
    assert greet('dutch') == 'Welkom'
    assert greet('IP_ADDRESS_INVALID') == 'Welcome'
    assert greet('finnish') == 'Tervetuloa'
    assert greet('') == 'Welcome'
    assert greet(2) == 'Welcome'
