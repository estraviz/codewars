from solution import Person


def test_person():
    matz = Person("Yukihiro", "Matsumoto", 47)
    assert matz.full_name == "Yukihiro Matsumoto"
    assert matz.age == 47

    joe = Person("Joe", "Smith", 30)
    assert joe.full_name == "Joe Smith"
    assert joe.age == 30
