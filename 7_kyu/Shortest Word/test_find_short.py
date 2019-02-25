from find_short import find_short


def test_find_short():
    text = "bitcoin take over the world maybe who knows perhaps"
    assert find_short(text) == 3

    text = "turns out random test cases are easier than writing out basic ones"
    assert find_short(text) == 3

    text = "lets talk about javascript the best language"
    assert find_short(text) == 3

    text = "i want to travel the world writing code one day"
    assert find_short(text) == 1

    text = "Lets all go on holiday somewhere very cold"
    assert find_short(text) == 2
