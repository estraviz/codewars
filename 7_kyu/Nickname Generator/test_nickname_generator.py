from nickname_generator import nickname_generator


def test_example_test_cases():
    assert nickname_generator("Jimmy") == "Jim"
    assert nickname_generator("Samantha") == "Sam"
    assert nickname_generator("Sam") == "Error: Name too short"
    assert nickname_generator("Kayne") == "Kay"
    assert nickname_generator("Melissa") == "Mel"
    assert nickname_generator("James") == "Jam"


def test_correct_names_general():
    assert nickname_generator("Gregory") == "Greg"
    assert nickname_generator("Jeannie") == "Jean"
    assert nickname_generator("Kimberly") == "Kim"
    assert nickname_generator("Timothy") == "Tim"
    assert nickname_generator("Dani") == "Dan"


def test_correct_names_vowel_checking():
    assert nickname_generator("Saamy") == "Saam"
    assert nickname_generator("Saemy") == "Saem"
    assert nickname_generator("Saimy") == "Saim"
    assert nickname_generator("Saomy") == "Saom"
    assert nickname_generator("Saumy") == "Saum"

    assert nickname_generator("Boyna") == "Boy", "'y' is not a vowel"
    assert nickname_generator("Kiyna") == "Kiy", "'y' is not a vowel"
    assert nickname_generator("Sayma") == "Say", "'y' is not a vowel"


def test_incorrect_names_too_short():
    assert nickname_generator("Ni") == "Error: Name too short"
    assert nickname_generator("Jam") == "Error: Name too short"
    assert nickname_generator("Suv") == "Error: Name too short"
