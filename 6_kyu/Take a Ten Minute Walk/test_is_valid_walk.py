from is_valid_walk import is_valid_walk


passwalk = [['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's'],
            ['e', 'w', 'e', 'w', 'n', 's', 'n', 's', 'e', 'w'],
            ['n', 's', 'e', 'w', 'n', 's', 'e', 'w', 'n', 's'],
            ['s', 'e', 'w', 'n', 'n', 's', 'e', 'w', 'n', 's']]

failwalk = [['n'],
            ['n', 's'],
            ['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's'],
            ['n', 's', 'e', 'w', 'n', 's', 'e', 'w',
             'n', 's', 'e', 'w', 'n', 's', 'e', 'w'],
            ['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 'n'],
            ['e', 'e', 'e', 'w', 'n', 's', 'n', 's', 'e', 'w']]


def test_should_return_false_if_walk_is_too_short():
    assert is_valid_walk(failwalk[0]) is False
    assert is_valid_walk(failwalk[1]) is False


def test_should_return_false_if_walk_is_too_long():
    assert is_valid_walk(failwalk[2]) is False
    assert is_valid_walk(failwalk[3]) is False


def test_should_return_false_if_walk_does_not_bring_you_back_to_start():
    assert is_valid_walk(failwalk[4]) is False
    assert is_valid_walk(failwalk[5]) is False


def test_should_return_true_for_a_valid_walk():
    assert is_valid_walk(passwalk[0]) is True
    assert is_valid_walk(passwalk[1]) is True
    assert is_valid_walk(passwalk[2]) is True
    assert is_valid_walk(passwalk[3]) is True
