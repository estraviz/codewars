from guesser import Guesser
import pytest


def test_correct_guess():
    guesser = Guesser(10, 2)
    guesser.guess(10)
    guesser.guess(10)
    guesser.guess(10)
    guesser.guess(10)
    assert guesser.guess(10) is True


def test_wrong_guess():
    guesser = Guesser(10, 2)
    guesser.guess(1)
    assert guesser.guess(1) is False


def test_lives_ran_out():
    guesser = Guesser(10, 2)
    guesser.guess(1)
    guesser.guess(2)

    with pytest.raises(Exception, match="EXCEPTION RAISED"):
        assert guesser.guess(10)
        pytest.fail("DID NOT RAISE")
