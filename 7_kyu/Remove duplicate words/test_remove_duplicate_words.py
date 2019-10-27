from remove_duplicate_words import remove_duplicate_words


def test_remove_duplicate_words():
    s = "alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta"
    assert remove_duplicate_words(s) == "alpha beta gamma delta"

    s = "my cat is my cat fat"
    assert remove_duplicate_words(s) == "my cat is fat"
