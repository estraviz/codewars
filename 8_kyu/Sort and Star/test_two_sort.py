from two_sort import two_sort


def test_two_sort():
    a = ["bitcoin", "take", "over", "the", "world", "maybe", "who", "knows",
         "perhaps"]
    assert two_sort(a) == 'b***i***t***c***o***i***n'

    a = ["turns", "out", "random", "test", "cases", "are", "easier", "than",
         "writing", "out", "basic", "ones"]
    assert two_sort(a) == 'a***r***e'

    a = ["lets", "talk", "about", "javascript", "the", "best", "language"]
    assert two_sort(a) == 'a***b***o***u***t'

    a = ["i", "want", "to", "travel", "the", "world", "writing", "code", "one",
         "day"]
    assert two_sort(a) == 'c***o***d***e'

    a = ["Lets", "all", "go", "on", "holiday", "somewhere", "very", "cold"]
    assert two_sort(a) == 'L***e***t***s'
