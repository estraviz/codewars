from nickname_generator import nickname_generator


def test_nickname_generator():
    assert nickname_generator("Jimmy") == "Jim"
    assert nickname_generator("Samantha") == "Sam"
    assert nickname_generator("Sam") == "Error: Name too short"
    assert nickname_generator("Kayne") == "Kay"
    assert nickname_generator("Melissa") == "Mel"
    assert nickname_generator("James") == "Jam"
