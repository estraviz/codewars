from find_longest import find_longest


def test_find_longest():
    string = "The quick white fox jumped around the massive dog"
    assert find_longest(string) == 7

    assert find_longest("Take me to tinseltown with you") == 10
    assert find_longest("Sausage chops") == 7
    assert find_longest("Wind your body and wiggle your belly") == 6
    assert find_longest("Lets all go on holiday") == 7
