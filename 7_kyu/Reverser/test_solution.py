from solution import reverse


def test_reverse():
    assert reverse(321) == 123
    assert reverse(1234) == 4321
    assert reverse(10987) == 78901
    assert reverse(1020) == 201
