import pytest

from solution import generate_hashtag


def test_expected_an_empty_string_to_return_false():
    assert generate_hashtag('') is False


def test_expeted_a_Hashtag_at_the_beginning():
    assert generate_hashtag('Do We have A Hashtag')[0] == '#'


def test_should_handle_a_single_word():
    assert generate_hashtag('Codewars') == '#Codewars'


def test_should_handle_trailing_whitespace():
    assert generate_hashtag('Codewars      ') == '#Codewars'


def test_should_remove_spaces():
    assert generate_hashtag('Codewars Is Nice') == '#CodewarsIsNice'


def test_should_capitalize_first_letters_of_words():
    assert generate_hashtag('codewars is nice') == '#CodewarsIsNice'


def test_should_capitalize_all_letters_of_words_all_lower_case_but_the_first():
    assert generate_hashtag('CodeWars is nice') == '#CodewarsIsNice'


def test_should_capitalize_first_letters_of_words_even_when_single_letters():
    assert generate_hashtag('c i n') == '#CIN'


def test_should_deal_with_unnecessary_middle_spaces():
    assert generate_hashtag('codewars  is  nice') == '#CodewarsIsNice'


def test_should_return_false_if_the_final_word_is_longer_than_140_chars():
    assert generate_hashtag('Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat') is False
