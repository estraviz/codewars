import pytest

from solution import first_non_repeating_letter


@pytest.mark.parametrize(
    "s, result",
    [
        ('a', 'a'),
        ('stress', 't'),
        ('moonmen', 'e'),
    ]
)
def test_should_handle_simple_tests(s, result):
    assert first_non_repeating_letter(s) == result


@pytest.mark.parametrize(
    "s, result",
    [
        ('', ''),
    ]
)
def test_should_handle_empty_strings(s, result):
    assert first_non_repeating_letter(s) == result


@pytest.mark.parametrize(
    "s, result",
    [
        ('abba', ''),
        ('aa', ''),
    ]
)
def test_should_handle_all_repeating_strings(s, result):
    assert first_non_repeating_letter(s) == result


@pytest.mark.parametrize(
    "s, result",
    [
        ('~><#~><', '#'),
        ('hello world, eh?', 'w'),
    ]
)
def test_should_handle_odd_characters(s, result):
    assert first_non_repeating_letter(s) == result


@pytest.mark.parametrize(
    "s, result",
    [
        ('sTreSS', 'T'),
        ('Go hang a salami, I\'m a lasagna hog!', ','),
    ]
)
def test_should_handle_letter_cases(s, result):
    assert first_non_repeating_letter(s) == result
