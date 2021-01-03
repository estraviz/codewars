import pytest

from solution import sexy_name


data_not_too_sexy = [
    ("GUV", "NOT TOO SEXY"),
    ("PHUG", "NOT TOO SEXY"),
    ("FFFFF", "NOT TOO SEXY"),
    ("", "NOT TOO SEXY"),
    ("PHUG", "NOT TOO SEXY"),
]


@pytest.mark.parametrize("name, result", data_not_too_sexy)
def test_not_too_sexy(name, result):
    assert sexy_name(name) == result


data_pretty_sexy = [
    ("BOB", "PRETTY SEXY"),
    ("JLJ", "PRETTY SEXY"),
    ("HHHHHU", "PRETTY SEXY"),
    ("BOB", "PRETTY SEXY"),
    ("WWWWWU", "PRETTY SEXY"),
]


@pytest.mark.parametrize("name, result", data_pretty_sexy)
def test_pretty_sexy(name, result):
    assert sexy_name(name) == result


data_very_sexy = [
    ("YOU", "VERY SEXY"),
    ("FABIO", "VERY SEXY"),
    ("ARUUUUUUUUU", "VERY SEXY"),
]


@pytest.mark.parametrize("name, result", data_very_sexy)
def test_very_sexy(name, result):
    assert sexy_name(name) == result


data_the_ultimate_sexiest = [
    ("ROBBY", "THE ULTIMATE SEXIEST"),
    ("SAMANTHA", "THE ULTIMATE SEXIEST"),
    ("DONALD TRUMP", "THE ULTIMATE SEXIEST"),
    ("BILL GATES", "THE ULTIMATE SEXIEST"),
    ("SCARLETT JOHANSSON", "THE ULTIMATE SEXIEST"),
    ("CODEWARS", "THE ULTIMATE SEXIEST"),
    ("PAMELA ANDERSON", "THE ULTIMATE SEXIEST"),
]


@pytest.mark.parametrize("name, result", data_the_ultimate_sexiest)
def test_the_ultimate_sexiest(name, result):
    assert sexy_name(name) == result


data_lowercase_letters = [("you", "VERY SEXY"), ("Codewars", "THE ULTIMATE SEXIEST")]


@pytest.mark.parametrize("name, result", data_lowercase_letters)
def test_lowercase_letters(name, result):
    assert sexy_name(name) == result
