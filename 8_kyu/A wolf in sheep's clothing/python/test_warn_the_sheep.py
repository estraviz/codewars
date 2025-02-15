from warn_the_sheep import warn_the_sheep


def test_warn_the_sheep():
    a = ['sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'wolf', 'sheep', 'sheep']
    b = 'Oi! Sheep number 2! You are about to be eaten by a wolf!'
    assert warn_the_sheep(a) == b

    a = ['sheep', 'wolf', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep']
    b = 'Oi! Sheep number 5! You are about to be eaten by a wolf!'
    assert warn_the_sheep(a) == b

    a = ['wolf', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep']
    b = 'Oi! Sheep number 6! You are about to be eaten by a wolf!'
    assert warn_the_sheep(a) == b

    a = ['sheep', 'wolf', 'sheep']
    b = 'Oi! Sheep number 1! You are about to be eaten by a wolf!'
    assert warn_the_sheep(a) == b

    a = ['sheep', 'sheep', 'wolf']
    b = 'Pls go away and stop eating my sheep'
    assert warn_the_sheep(a) == b
