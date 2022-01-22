from solution import count_duplicates


def test_no_duplicates():
    name = ['John', 'Beth', 'Beth', 'Bill']
    age = [37, 23, 30, 46]
    height = [183, 170, 165, 175]
    assert count_duplicates(name, age, height) == 0


def test_one_entry_duplicate():
    name = ['John', 'Beth', 'Beth', 'Beth', 'Bill']
    age = [37, 23, 23, 23, 46]
    height = [183, 170, 170, 170, 175]
    assert count_duplicates(name, age, height) == 2


def test_multi_entry_duplicates():
    name = ['Jack', 'Ben', 'Jack', 'Ben', 'Jack', 'Jack']
    age = [25, 25, 34, 25, 25, 34]
    height = [180, 180, 200, 180, 180, 200]
    assert count_duplicates(name, age, height) == 3
