from name_value import name_value


def test_name_value():
    assert name_value(["abc", "abc", "abc", "abc"]) == [6, 12, 18, 24]
    assert name_value(["codewars", "abc", "xyz"]) == [88, 12, 225]
    assert name_value(["abc", "abc", "abc", "abc"]) == [6, 12, 18, 24]
    assert name_value(
        ["abcdefghijklmnopqrstuvwxyz", "stamford bridge",
         "haskellers"]), [351, 282, 330]
    assert name_value(["i love coding", "better than pizza",
                       "i got this"]) == [115, 382, 321]
    assert name_value(
        ["mercury", "venus", "earth mars", "jupiter saturn",
         "uranus neptune"]) == [103, 162, 309, 768, 945]
    assert name_value(["a cup", "some tea", "more coffee",
                       "one glass"]) == [41, 156, 273, 368]
    assert name_value(["a", "e", "i", "o", "u",
                       "the end"]) == [1, 10, 27, 60, 105, 336]
    assert name_value(["coding", "better pizza",
                       "i got this too"]) == [52, 296, 471]
