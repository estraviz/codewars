from numericals import numericals


def test_numericals():
    assert numericals("Hello, World!") == "1112111121311"
    assert numericals("Hello, World! It's me, JomoPipi!"
                      ) == "11121111213112111131224132411122"
    assert numericals("hello hello") == "11121122342"
    assert numericals("Hello") == "11121"
    assert numericals("aaaaaaaaaaaa") == "123456789101112"
    assert numericals("11111") == "12345"
    assert numericals("hope you 123456789 expected numbers in the string"
                      ) == "1111112121111111113212311414121151151262267232231"
    assert numericals(
        "In this string, I'll make sure the amounts of a character go over 9"
    ) == "11111112221221132112411115312263237221234482193101343525441123124155131"
