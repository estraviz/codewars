from numericals import numericals


def test_numericals():
    assert numericals("Hello, World!") == "1112111121311"
    assert numericals("Hello, World! It's me, JomoPipi!"
                      ) == "11121111213112111131224132411122"
    assert numericals("hello hello") == "11121122342"
    assert numericals("Hello") == "11121"
    assert numericals("aaaaaaaaaaaa") == "123456789101112"
